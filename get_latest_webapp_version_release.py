#!/usr/bin/python

__author__    = 'gengwg'
__copyright__ = ""
__version__   = 0.1

"""
A Script to get the latest version of webapp in Nexus given a particular release.
Jacob notes it's better to implement it in requests.
"""

import urllib,sys
import urllib2, base64
import threading
import os
import argparse

from xml.etree import ElementTree
from xml.etree import ElementPath

import json
import logging
from logging import log
import time


config = {}
execfile("nexus.conf", config)

def get_latest_webapp_version(url):
    """
    Function to get the latest version of webapp in Nexus given a particular release
    """
    release = config['release']
    username = config['username']
    password = config['password']
    values = { 'username': username,'password': password }
    myval = urllib.urlencode(values)

    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, username, password)
    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(authhandler)
    urllib2.install_opener(opener)

    try:
        data = urllib2.urlopen(url).read()
        log(logging.INFO, "Logging in as user" + username)
    except IOError, e:
        log(logging.ERROR, "Couldn't open url: %s %s" %(url, e.strerror))
        sys.exit(1)

    doc = ElementTree.XML( data )

    versions = []
    for ver in doc.iter('version'):
        if str(release) not in ver.text:
            log(logging.WARN, "Release has not been built yet. Try again later.")
            sys.exit(2)
        else:
            if 'aws' in ver.text:
                versions.append(ver.text)

    print versions[-1]
    log(logging.INFO, "Done getting latest version")

def daemonize():
    pid = os.fork()
    if pid > 0:
        sys.exit(0)

    os.setsid()

    pid = os.fork()
    if pid > 0:
        sys.exit(0)

    stdin = file(os.devnull, 'r')
    stdout = file(os.devnull, 'a')
    stderr = file(os.devnull, 'a', 0)

    os.dup2(stdin.fileno(), sys.stdin.fileno())
    os.dup2(stdout.fileno(), sys.stdout.fileno())
    os.dup2(stderr.fileno(), sys.stderr.fileno())

if __name__ == "__main__":

    try:
        if not os.path.exists("./logs"):
            os.mkdir("logs")
    except OSError, e:
        log(logging.ERROR, "Couldn't create logs directory.")

    logging.basicConfig(level=logging.INFO, filename="logs/my.log")

    threads = []
    t = threading.Thread(target=get_latest_webapp_version, args=(config['url'],))
    threads.append(t)
    t.start()
    sys.exit(0)

