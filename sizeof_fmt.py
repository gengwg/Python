#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
convert bytes to human readable units.

example:
$ ./sizeof_fmt.py 1048576
1.0MiB
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("bytes", type=int)
args = parser.parse_args()

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

print sizeof_fmt(args.bytes)
