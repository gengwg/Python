# preparation work:
# export db on pxe; and copy it in this directory.

import os
import subprocess
import unittest

import sys
sys.path.insert(0, '../..')
from infradb.infradb import InfraDB
#from ... import infradb

from nose_parameterized import parameterized

infradb = InfraDB(dbhost='localhost', dbport=48824)
data = infradb.get_data()

class TestInfraDB(unittest.TestCase):
    def setUp(self):
        self.infradb = InfraDB(dbhost='localhost', dbport=48824)
        self.infradb = InfraDB()
        self.data = self.infradb.get_data()

    def tearDown(self):
        pass

    def test_success(self):
        """Mock test success"""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_fail(self):
        """Mock test fail"""
        x = 2 * 2
        self.assertEqual(x,8,"DID NOT MATCH")

    @parameterized.expand([
        row['host'] for row in data
    ])
    def disable_test_host_pingable(self, host=''):
        """Test if host is pingable"""

        print host
    	#host = self.data[0]['host']

        with open(os.devnull, 'wb') as devnull:
            cmd = 'ping -c 1'.split() + [ host ]
            try:
                mycall = subprocess.check_call(cmd, stdout=devnull, stderr=subprocess.STDOUT)
                response = 0
            except subprocess.CalledProcessError as e:
                output = e.output
                response = e.returncode

        self.assertEqual(response, 0, host + ": Not Pinable!!")

    def test_db_connect(self):
        """Test if db is connected"""
        cur = self.infradb.get_cur()

        self.assertIsNotNone(cur, 'database not connected')


    def test_duplicate_hostnames(self):
        """Test if hostname is duplicated"""
        hosts = self.infradb.get_hosts()
        self.assertIsNotNone(hosts)

        self.assertTrue( len(hosts) == len(set(hosts)) )

    def test_duplicate_ips(self):
        """Test if ip is duplicated"""
        ips = self.infradb.get_ips()
        self.assertIsNotNone(ips)

        self.assertTrue( len(ips) == len(set(ips)) )

    def test_duplicate_lom_ips(self):
        """Test if lom ip is duplicated"""
        lom_ips = self.infradb.get_lom_ips()
        self.assertIsNotNone(lom_ips)

        #print len(lom_ips)
        #print len(set(lom_ips))
        self.assertTrue( len(lom_ips) == len(set(lom_ips)) )

    def test_duplicate_macs(self):
        """Test if lom ip is duplicated"""
        macs = self.infradb.get_macs()
        self.assertIsNotNone(macs)

        #print len(macs)
        #print len(set(macs))
        self.assertTrue( len(macs) == len(set(macs)) )


if __name__ == '__main__':
    unittest.main()
