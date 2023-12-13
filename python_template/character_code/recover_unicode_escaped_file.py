#!/usr/bin/python

import sys
import codecs

fname = sys.argv[1]

with open(fname, 'r') as f:
    with open(fname + '_decoded', 'w') as f_w:
        line = f.readline()
        line_decoded = codecs.decode(line, 'unicode_escape')
        f_w.write(line_decoded)

sys.exit()
