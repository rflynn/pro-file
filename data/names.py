#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Operations common to names
"""

import re

# normalize spaces, case and apostrophes, but leave accented characters alone
def strip(name):
    name = re.sub('\s+', '', name) # remove spaces
    name = re.sub("['’]", '', name) # nuke apostrophes
    name = name.upper()
    return name

# completely normalize name
def normalize(name):
    name = strip(name)
    # de-accent whacky foreign characters
    for (r,p) in [
        ('A', '[ÀÁÂÄÃẦĀ]'),
        ('C', '[Ç]'),
        ('E', '[ÈÉÊËỄỆ]'),
        ('I', '[ÌÍÎÏĪÍ]'),
        ('O', '[ÒÓÔÕÖỖƠŌ]'),
        ('N', '[Ñ]'),
        ('U', '[ÙÚÛÜŨƯ]'),
        ('Y', '[ÝŸỲ]') ]:
        name = re.sub(p, r, name, re.UNICODE)
    return name
