#!/usr/bin/env python
"""
Get Possible IPs for a specific CIDR

Example:
$ ./get_ips_from_cidr.py 10.65.36.23/29
Possible IPs for CIDR 10.65.36.23/29:
10.65.36.16
10.65.36.17
10.65.36.18
10.65.36.19
10.65.36.20
10.65.36.21
10.65.36.22
10.65.36.23
"""

from netaddr import IPNetwork
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("cidr")
args = parser.parse_args()
cidr = args.cidr

print "Possible IPs for CIDR {}:".format(cidr)
for ip in IPNetwork(cidr):
    print ip


