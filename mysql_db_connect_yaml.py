#!/usr/bin/python
# connect mysql db using yaml file to store credentials

import yaml
import MySQLdb

db_info_cfg = './data/db_info.yaml'
def db_connect(key):
    with open(db_info_cfg, 'r') as f:
        db_info = yaml.safe_load(f)
        db_host = db_info[key]['host']
        db_user = db_info[key]['user']
        db_pass = db_info[key]['pass']
        database = db_info[key]['db']
    return MySQLdb.connect(host=db_host, user=db_user, passwd=db_pass, db=database)

def main():
    print 'This file should only be used as an import'

if __name__ == '__main__':
    main()
