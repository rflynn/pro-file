#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# FIXME: given names need to be case-normalized(!)

import sqlite3
import time
import stats # custom

CurrentYear = time.localtime().tm_year

"""
TODO: create a separate gender table and just pre-calculate everything, much faster
"""
def gender(conn, name, cc='US'):
    c = conn.cursor()
    c.execute("""
        select gender,sum(total)
        from givenname_birthyear
        where name=?
        group by name,gender
        """, (name,))
    g = dict(list(c.fetchall()))
    total = float(sum(list(g.values())))
    g2 = {k:g[k]/total for k in g.keys()};
    # ensure both common genders present
    for k in ('F','M'):
        if not k in g2:
            g2[k] = 0.
    return g2


def name_birth_totals(conn, name, cc='US'):
    c = conn.cursor()
    c.execute("""
    select n.year,
        sum(n.total * p.factor1900 * lt.prob) as fcnt
    from givenname_birthyear n
    join population p on p.year = n.year
    join life_table_us lt on lt.year = n.year
    where name=?
    group by name, n.year""", (name,))
    d = dict(c.fetchall())
    # fill in gap years with zero, simplifies graphing
    fill = [(y, d[y] if y in d else 0.)
            for y in range(1900, CurrentYear+1)]
    return fill

"""
return the most-likely contiguous time period of 'span' years in which
someone with 'name' was born in country 'cc'
"""
def birthspan(conn, name, span=30, cc='US'):
    birthcnt = name_birth_totals(conn, name, cc)
    cnts = [cnt for year,cnt in birthcnt]
    (ylo,yhi),pct = stats.range_size(cnts, span)
    return ((ylo+1900, yhi+1900),pct)

"""
return the most-likely contiguous time period during which someone
with 'name' was born in country 'cc' with born within 'pct' likelihood
"""
def birthspan_pct(conn, name, pct=80, cc='US'):
    birthcnt = name_birth_totals(conn, name, cc)
    cnts = [cnt for year,cnt in birthcnt]
    ylo,yhi = stats.range_pct(cnts, pct / 100.)
    return (ylo+1900, yhi+1900)

import names
import givenname_origin

def lookup(conn, givennames):
    for name in givennames:
        norm = names.normalize(name)
        g = gender(conn, norm)
        pct, span = 70, 20
        plo,phi = birthspan_pct(conn, norm, pct)
        (slo,shi),spct = birthspan(conn, norm, span)
        hints = givenname_origin.classify(norm)
        print('%-15s %3.0f%%%s %2.0f%%@%.0fyr=%d-%d %.0f%%=%d-%d %s' % \
            (name, max(g.values())*100.,
            'F' if g['F'] >= g['M'] else 'M',
            spct, span, slo, shi, pct, plo, phi, hints))

def test(conn):
    lookup(conn, 'Non-existent Ruth James Robin Ryan Britney Tyler Austin'.split(' '))

if __name__ == '__main__':
    import sys
    with sqlite3.connect('./names.sqlite3') as conn:
        if sys.argv[1:] != []:
            lookup(conn, sys.argv[1:])
        else:
            test(conn)

