#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import OAparser

if sys.argv[1]:
    logfile = sys.argv[1]

parser = OAparser.Parser(logfile)

for i in parser.log:
    print(i, parser.log[i])
