#!/usr/bin/env python3

# get both ipv4 and ipv6 addresses given hostname
# usage:
# $ ./get_ips_from_hostname.py qq.com
# 58.250.137.36
# 64:ff9b::3af7:d62f
# $ ./get_ips_from_hostname.py 163.com
# 123.58.180.8
# 64:ff9b::7b3a:b407
# $ ./get_ips_from_hostname.py google.com
# 64.233.180.139
# 2607:f8b0:4003:c0b::8a


import socket


def get_ip6(host, port=0):
    try:
        # search only for the wanted v6 addresses
        result = socket.getaddrinfo(host, port, socket.AF_INET6)
    except socket.gaierror:
        return ""
    return result[0][4][0]  # just returns the first answer and only the address


def get_ip4(host):
    return socket.gethostbyname(host)


def test():
    print(get_ip4("163.com"))
    print(get_ip6("163.com"))


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("hostname", type=str)
    args = parser.parse_args()

    print(get_ip4(args.hostname))
    print(get_ip6(args.hostname))


if __name__ == "__main__":
    # test()
    main()
