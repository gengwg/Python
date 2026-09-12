#!/usr/bin/python

__author__    = 'gengwg'
__copyright__ = ""
__version__   = 0.1

"""
A Script to get the latest version of webapp in Nexus given a particular release.
Jacob notes it's better to implement it in requests.
"""

import sys
import urllib.parse
import urllib.request
import base64
import threading
import os
import argparse

from xml.etree import ElementTree
from xml.etree import ElementPath

import json
import logging
import time


config = {}
with open("nexus.conf") as f:
    exec(compile(f.read(), "nexus.conf", "exec"), config)

def get_latest_webapp_version(url):
    """
    Function to get the latest version of webapp in Nexus given a particular release
    """
    release = config['release']
    username = config['username']
    password = config['password']
    values = { 'username': username,'password': password }
    myval = urllib.parse.urlencode(values)

    passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, username, password)
    authhandler = urllib.request.HTTPBasicAuthHandler(passman)
    opener = urllib.request.build_opener(authhandler)
    urllib.request.install_opener(opener)

    try:
        data = urllib.request.urlopen(url).read()
        logging.info("Logging in as user %s", username)
    except OSError as e:
        logging.error("Couldn't open url: %s %s", url, e.strerror)
        sys.exit(1)

    doc = ElementTree.XML( data )

    versions = []
    for ver in doc.iter('version'):
        if str(release) not in ver.text:
            logging.warning("Release has not been built yet. Try again later.")
            sys.exit(2)
        else:
            if 'aws' in ver.text:
                versions.append(ver.text)

    print(versions[-1])
    logging.info("Done getting latest version")

def daemonize():
    pid = os.fork()
    if pid > 0:
        sys.exit(0)

    os.setsid()

    pid = os.fork()
    if pid > 0:
        sys.exit(0)

    stdin = open(os.devnull)
    stdout = open(os.devnull, 'a')
    stderr = open(os.devnull, 'a')

    os.dup2(stdin.fileno(), sys.stdin.fileno())
    os.dup2(stdout.fileno(), sys.stdout.fileno())
    os.dup2(stderr.fileno(), sys.stderr.fileno())

if __name__ == "__main__":

    try:
        if not os.path.exists("./logs"):
            os.mkdir("logs")
    except OSError as e:
        logging.error("Couldn't create logs directory.")

    logging.basicConfig(level=logging.INFO, filename="logs/my.log")

    threads = []
    t = threading.Thread(target=get_latest_webapp_version, args=(config['url'],))
    threads.append(t)
    t.start()
    sys.exit(0)

