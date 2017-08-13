#!/usr/bin/env python

__author__    = 'Geng'
__version__   = '0.1.2'

import re
import sys
import subprocess
import time
import os

import MySQLdb
import sys
import gc
import csv
import datetime
import json
import yaml

from pprint import pprint

import datetime
from time import mktime

class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))

        return json.JSONEncoder.default(self, obj)

class InfraDB():
    """Class to model the DB.

    This class intends to provide one stop lib for manipulating the DB.
    """

    def __init__(self, dbhost = 'infradb-1-vip.example.com', dbport=3306, table='infradb_flat', columns='*', limit = 18446744073709551615):
        """initialize a db object"""
        # set up some variables
        self.dbhost=dbhost
        self.dbport=dbport
        self.rouser='infradb_ro'
        self.ropassword='ropass'
        self.rwuser='infradb_rw'
        self.rwpassword='kasDFjgr7234DGher78'
        self.database='infradb'
        self.table=table
        self.row_start = 0
        self.row_end = limit
        #self.row_end=18446744073709551615   # grab all rows
        self.columns = columns                   # grab all colums

        try:
            # infradbdb
            self.conn = MySQLdb.connect(host=self.dbhost, port=self.dbport, user=self.rwuser, passwd=self.rwpassword, db=self.database)
            self.conn.autocommit(False)

            with self.conn:
                try:
                    self.cur = self.conn.cursor(MySQLdb.cursors.DictCursor)

                except Exception, e:
                    print "Error %d: %s" % (e.args[0],e.args[1])

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            self.conn.rollback()
            self.cur.close()
            self.conn.close()
            # print lengthy error description!!
            sys.exit(2)


#        finally:
#
#            if self.db:
#                pass
#                #db.close()
#            gc.collect()

    def __del__(self):
        """clean up"""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        gc.collect()
        #print self.database, 'died'

    def __str__(self):
        mystring = "Welcome!"
        mystring += "\nYou are using db host: \t\t" + self.dbhost
        mystring += "\nYou are using db: \t\t" + self.database
        mystring += "\nYou are using db table: \t" + self.table
        return mystring

    def get_data(self):
        """Main function to fetch fata from mysql database.
        """

        self.cur.execute("SELECT " + self.columns +\
                " FROM " + self.table + \
                " LIMIT " + str(self.row_start) + "," + str(self.row_end) )
        self.conn.commit()

        data = self.cur.fetchall()

        return data

    def get_dbuser_name(self):
        """function to get table name.
        e.g. for debug purpose.
        """
        self.cur.execute("SELECT USER()")
        dbuser = self.cur.fetchone()['USER()']

        return dbuser

    def get_database_name(self):
        """function to get table name.
        e.g. for debug purpose.
        """
        self.cur.execute("SELECT DATABASE()")
        dbname = self.cur.fetchone()['DATABASE()']

        return dbname

    def get_tables(self):
        """function to get data base name.
        e.g. for debug purpose.
        """
        self.cur.execute("SHOW tables")
        tables = self.cur.fetchall()

        return tables

    def get_schema(self):
        """function to get data base name.
        e.g. for debug purpose.
        """
        self.cur.execute("DESCRIBE " + self.table)
        schema = self.cur.fetchall()

        return schema

    def get_gateway(self, vlanid):
        """function to get gateway from existing records given vlan id.
        """

        for row in self.get_data():
            if str(vlanid) == str(row['vlan_id']):
                return row['gateway']

        return None

    def get_netmask(self, vlanid):
        """function to get netmask from existing records given vlan id.
        """

        for row in self.get_data():
            if str(vlanid) == str(row['vlan_id']):
                return row['netmask']

        return None

    def get_hosts(self):
        """function to get a list of all hosts
        """

        hosts = []
        for row in self.get_data():
            hosts.append(row['host'])

        return hosts

    def get_ids(self):
        """function to get a list of all ids
        """

        ids = []
        for row in self.get_data():
            ids.append(row['id'])

        return ids

    def get_id(self, host):
        """function to get id
        """
        for row in self.get_data():
            if host == row['host']:
                return row['id']

        return None

    def get_ips(self):
        """function to get a list of all ips
        """

        ips = []
        for row in self.get_data():
            ips.append(row['ip_address'])

        return ips

    def get_lom_ips(self):
        """function to get a list of all lom ips
        """

        ips = []
        for row in self.get_data():
            ips.append(row['lom_ip'])

        return ips

    def get_macs(self):
        """function to get a list of all macs
        """

        macs = []
        for row in self.get_data():
            macs.append(row['host'])

        return macs

    def get_hosts_by_rack(self, rack):
        """function to get a list of hosts given rack id.
        """

        hosts = []
        print('sku', 'port', 'host', 'ip_address', 'stamp_created')
        for row in self.get_data():
            if row['rack'] == rack:
                host = (row['sku'], row['port'], row['host'], row['ip_address'], row['mac'])
                hosts.append(host )

        return hosts

    def get_host_by_name(self, fqdn):
        """function to get host given fqdn.
        Returns a tuple.
        """

        for row in self.get_data():
            if fqdn == row['host']:
                #host = (row['sku'], row['port'], row['host'], row['ip_address'], row['mac'])
                return row

        return None

    def get_hosts_by_vlan(self, vlan_id):
        """function to get a list of hosts given rack id.
        Takesa a numerical
        Returns a list.
        """

        hosts = []

        for row in self.get_data():
            if vlan_id == row['vlan_id']:
                host = (row['sku'], row['port'], row['host'], row['ip_address'], row['mac'])
                hosts.append(host )

        return hosts

    def get_hosts_by_pod(self, pod):
        """function to get a list of hosts given pod.
        Returns a list.
        """

        hosts = []

        for row in self.get_data():
            if pod == row['pod']:
                #host = (row['sku'], row['port'], row['host'], row['ip_address'], row['mac'])
                #host = (row['host'], row['ip_address'])
                host = row
                hosts.append(host )

        return hosts


    def dump_json(self):
        """Function to dump JSON.
        """

        result = []

        for row in self.get_data():
            result.append(row)

        result_dict = {'count': len(result), 'previous': 'null', 'results': result}

        return json.dumps(result_dict, cls = MyEncoder)

    def get_spares(self):
        """function to get spares reports.
        """

        self.cur.execute("SELECT count(1), sku " + \
                " FROM " + self.table + \
                " WHERE vlan_name = 'SPARE' group by sku" + \
                " LIMIT " + str(self.row_start) + "," + str(self.row_end) )
        spares = self.cur.fetchall()

        return spares

        for row in spares:
            #pprint (row)
            if row['count(1)'] > 20:
                print 'OK: We still have ' + str(row['count(1)']) + ' spares left for ' + row['sku']
                #inventory += 'OK: We still have ' + str(row['count(1)']) + ' spares left for ' + row['sku'] + '\n'
            else:
                print 'WARN: We have only ' + str(row['count(1)']) + ' machines left for ' + row['sku'] + '!!!\n'
                #inventory += 'WARN: We have only ' + str(row['count(1)']) + ' machines left for ' + row['sku'] + '!!!<---\n'

    def get_spares_count_by_sku(self, sku):
        """function to get number of hosts in a certan given SKU.
        :param sku: hardware class SKU given
        :return:    number of hosts in a certain SKU
        """

        for row in self.get_spares():
            if sku == row['sku']:
                return row['count(1)']
                #print row


    def get_total_count(self):
        """function to get total number of machines in infradb.
        """
        query = "SELECT count(*) AS TotalNumMachines" + " FROM " + self.table + " LIMIT " + str(self.row_start) + "," + str(self.row_end)
        self.cur.execute(query)
        #self.cur.execute("SELECT count(*) AS TotalNumMachines" + " FROM " + self.table + " LIMIT " + str(self.row_start) + "," + str(self.row_end) )
        total = self.cur.fetchone()['TotalNumMachines']

        return total

    def get_cur(self):
        """function to get total number of machines in infradb.
        """
        return self.cur

    def get_vlans(self):
        """function to get a list of vlans / networks.
        """
        query = "select * from vlans"
        self.cur.execute(query)
        return self.cur.fetchall()


    def get_new_hosts(self):
        """function to get hosts that have been assigned using the new_hosts table
        """
        query = """select p.id, p.host, p.vlan_id, p.rack, p.port, n.status
                from infradb_flat p, new_hosts n
                where p.host = n.host
                order by n.status, p.id"""

        self.cur.execute(query)
        return self.cur.fetchall()



    def get_unkicked_hosts(self):
        """function to get hosts that have been assigned that have not been kicked
        """
        query = """select p.id, p.host, p.rack, n.status
from infradb_flat p, new_hosts n
where p.host = n.host
  and n.status not like 'KICKED'
order by n.status, p.id"""
        self.cur.execute(query)
        return self.cur.fetchall()


    def get_unkicked_hosts_count(self):
        """function to get how many new hosts, status have not been kicked
        """
        query = """select host, status from new_hosts
where status not like 'KICKED'
  and status not like 'VLAN'
"""
        self.cur.execute(query)
        return self.cur.fetchall()


    def get_available_skus_per_rack_in_bench(self):
        """function to get distribution of available skus per rack in bench
        """
        query = """
select count(1), sku, rack from infradb_flat
where vlan_name = 'SPARE'
  and host like 'spare%'
  and pod = 'bench'
group by sku, rack
order by rack
"""
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_count_assigned_hosts_per_rack(self):
        """function to get count of assigned hosts per rack
        """
        query = """select count(1) c, p.rack
from infradb_flat p, new_hosts n
where p.host = n.host
  and n.status = 'KICKED'
group by p.rack
order by c desc
"""

        self.cur.execute(query)
        return self.cur.fetchall()


    def dump_mysql(self, backup_dir=''):
        """
        used for mysql database backup
        Returns: None

        """
        DB_HOST = 'infradb.example.com'
        DB_USER = self.rwuser
        DB_USER_PASSWORD = self.rwpassword
        DB_NAME = self.database

        BACKUP_PATH = '/tmp/'
        # Getting current datetime to create seprate backup folder
        DATETIME = time.strftime('%Y%m%d-%H%M%S')
        TODAYBACKUPPATH = BACKUP_PATH + DATETIME

        if backup_dir:
            TODAYBACKUPPATH=backup_dir

        # Checking if backup folder already exists or not. If not exists will create it.
        if not os.path.exists(TODAYBACKUPPATH):
            os.makedirs(TODAYBACKUPPATH)


        dumpcmd = "mysqldump --host=" + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " > " + TODAYBACKUPPATH + "/" + DB_NAME + ".sql"

        os.system(dumpcmd)

        print "Your backups has been created in '" + TODAYBACKUPPATH + "' directory."

    def get_ip(self, gateway, netmask):
        """get spare ip"""
        p = subprocess.Popen(["./allocate_ip", "-g", gateway, "-n", netmask], stdout=subprocess.PIPE)
        return p.communicate()[0].rstrip()


    def set_host_conf(self, id, host, vlan, vlanid, ip, netmask, gateway):
        """set host config"""
        p = subprocess.Popen(["./conf", id, host, vlan, vlanid, ip, netmask, gateway], stdout=subprocess.PIPE)
        #print p.communicate()[0]

    def set_host_vlan(self, id):
        """set host vlan config on switch a/b"""
        p = subprocess.Popen(["./vlan3", id])
        #print p.communicate()[0]

    def do_evil(self):
        """dns, dhcp, cobbler, etc"""
        p = subprocess.Popen(["./evil", "-f"])
        #print p.communicate()[0]

    def kick(self, id):
        """Finally we are ready to kick the host"""
        p = subprocess.Popen(["./kick", id])
        #print p.communicate()[0]

    #def unprovision(self, id):
    def unprovision(self, host):
        #id = str(id)
        id = str(self.get_id(host))
        vlan='SPARE'
        vlanid='501'
        gateway='10.193.16.1'
        netmask='255.255.240.0'
        host='spare-0-' + str(id) + '.none.example.com'

        ip = self.get_ip(gateway, netmask)

        print 'Unprovisioning ' + str((id, host, vlan, vlanid, ip, netmask, gateway))

        self.set_host_conf(id, host, vlan, vlanid, ip, netmask, gateway)
        time.sleep(3)
        self.set_host_vlan(id)
        time.sleep(3)
        self.set_host_vlan(id)
        time.sleep(3)
        self.do_evil()
        time.sleep(3)
        self.kick(id)


# Tests
if __name__ == '__main__':

    # Examples

    infradb = InfraDB()
    #infradb = InfraDB(dbhost = 'localhost')

    #pprint( infradb.get_data() )
    pprint( infradb.get_gateway(501) )
    pprint( infradb.get_netmask(501) )

    sys.exit(0)
    #print infradb.get_rack(103)
    pprint( infradb.get_hosts_by_rack(103) )

    print infradb.get_dbuser_name()
    print infradb.get_tables()
    print infradb.get_database_name()
    pprint (infradb.get_schema() )

    #print infradb.dump_json()

    print infradb

    infradb.get_spares()
    print infradb.get_spares_count_by_sku('Database001')
    print infradb.get_total_count()

    print infradb.get_cur()
    print infradb.get_hosts()
    #pprint (infradb.get_vlans())
    pprint (infradb.get_new_hosts())
    print('------------')
    print infradb.get_unkicked_hosts()
    print('------------')

    print infradb.get_unkicked_hosts()
    print('------------')

    print infradb.get_unkicked_hosts()
    print('------------')

    pprint(infradb.get_available_skus_per_rack_in_bench())
    print('---------------------')

    pprint(infradb.get_count_assigned_hosts_per_rack())
    print('---------------------')

    print infradb.dump_mysql()
    print('----------------------')

    print infradb.get_ids()
    sys.exit(0)
