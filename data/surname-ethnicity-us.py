#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Download, extract, parse and import U.S. Census data on
the ethnicity of common surnames
"""

import os, sys
import sqlite3

# TODO: split these generalized functions into their own module
# and consolidate smiliar calls in other files

def download(url, filename):
    if os.path.exists(filename):
        # TODO: add checksumming
        print(('-- %s exists' % (filename)))
    else:
        import urllib.request, urllib.parse, urllib.error
        def reporthook(a,b,c):
            print(("% 3.1f%% of %d bytes\r" % \
                (min(100, float(a * b) / c * 100), c)), end='')
            sys.stdout.flush()
        print(('-- %s ->  %s' % (url, filename)))
        urllib.request.urlretrieve(url, filename, reporthook)
    # TODO: check success of urlretrieve
    return True

def extract(filename, destdir):
    import subprocess
    print('/*')
    sys.stdout.flush()
    subprocess.call(['unzip', '-d', destdir, '-u', filename])
    print('*/')

def create_table(conn):
    c = conn.cursor()
    c.executescript("""
    DROP TABLE IF EXISTS surname_ethnicity_us_2000;
    CREATE TABLE surname_ethnicity_us_2000 (
        name TEXT NOT NULL PRIMARY KEY,
        likely_eth TEXT NOT NULL,
        likely_pct REAL NOT NULL,
        total INTEGER NOT NULL,
        pctwhite REAL NOT NULL,
        pctblack REAL NOT NULL,
        pctapi REAL NOT NULL,
        pctasian REAL NOT NULL,
        pct2race REAL NOT NULL,
        pcthispanic REAL NOT NULL
    );""")
    c.close()

def parse(conn, csvfilename):
    # "(S)" means what exactly? Just return 0
    def float_or_s(txt):
        try:
            return float(txt)
        except:
            return 0.0
    import csv
    rd = csv.reader(open(csvfilename, 'r'))
    # hmmm python csv reader doesn't handle field title lines?
    next(rd) # discard header line
    fields = ['name','rank','count','prop100k','cum_prop100k','pctwhite','pctblack','pctapi','pctasian','pct2prace','pcthispanic']
    create_table(conn)
    c = conn.cursor()
    c.execute('BEGIN TRANSACTION')
    cnt = 0
    for r in rd:
        row = [r[0], int(r[1]), int(r[2])] + list(map(float_or_s, r[3:]))
        d = dict(list(zip(fields,row)))
        # calculate most likely ethnicity
        e = [(k,d[k]) for k in fields[5:]]
        d['eth'],d['ethpct'] = max(e,key=lambda x:x[1])
        d['eth'] = d['eth'][3:].upper()
        c.execute('INSERT INTO surname_ethnicity_us_2000' + \
'(name,likely_eth,likely_pct,total,pctwhite,pctblack,pctapi,pctasian,pct2race,pcthispanic)VALUES(?,?,?,?,?,?,?,?,?,?)',
            (d['name'], d['eth'], d['ethpct'], d['count'],
             d['pctwhite'], d['pctblack'], d['pctapi'], d['pctasian'], d['pct2prace'], d['pcthispanic']))
        cnt += 1
    #c.execute('COMMIT')
    c.close()
    return cnt

if __name__ == '__main__':

    Url = 'http://www.census.gov/genealogy/www/data/2000surnames/names.zip'
    Filename = 'surname-ethnicity-us-names-2000.zip'
    Extractdir = 'surname-ethnicity-us-names-2000/'
    CsvFilename = Extractdir + 'app_c.csv'

    download(Url, Filename)
    extract(Filename, Extractdir)

    with sqlite3.connect('./names.sqlite3') as conn:
        cnt = parse(conn, CsvFilename)
        print(('imported', cnt, 'surname/ethnicity records'))

