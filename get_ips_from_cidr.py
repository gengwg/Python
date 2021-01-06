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

# from netaddr import IPNetwork
from ipaddress import ip_network
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("cidr")
args = parser.parse_args()
cidr = args.cidr

print("Possible IPs for CIDR {}:".format(cidr))

# Set strict to False: the host bits are masked out
# to determine the appropriate network address.
# Otherwise get error:
#     ValueError: 10.65.36.23/29 has host bits set
for ip in ip_network(cidr, False):
    print(ip)
