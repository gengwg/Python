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

$ ./get_ips_from_cidr.py 12:3456:78:90ab:cd:ef01:23:30/125
Possible IPs for CIDR 12:3456:78:90ab:cd:ef01:23:30/125:
12:3456:78:90ab:cd:ef01:23:30
12:3456:78:90ab:cd:ef01:23:31
12:3456:78:90ab:cd:ef01:23:32
12:3456:78:90ab:cd:ef01:23:33
12:3456:78:90ab:cd:ef01:23:34
12:3456:78:90ab:cd:ef01:23:35
12:3456:78:90ab:cd:ef01:23:36
12:3456:78:90ab:cd:ef01:23:37
"""

# from netaddr import IPNetwork
import ipaddress
from ipaddress import ip_network
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("cidr")
args = parser.parse_args()
cidr = args.cidr

# Set strict to False: the host bits are masked out
# to determine the appropriate network address.
# Otherwise get error:
#     ValueError: 10.65.36.23/29 has host bits set
net = ip_network(cidr, False)

# An IP address and network address can be specified together as an IP interface.
inet = ipaddress.ip_interface(cidr)
net = inet.network

print("INET: {}".format(cidr))
print("CIDR: {}".format(net))
print("IP ADDR: {}".format(inet.ip))
print("Total number of IPs: {}".format(net.num_addresses))
print("Possible IPs are:")
for ip in net:
    print(ip)
