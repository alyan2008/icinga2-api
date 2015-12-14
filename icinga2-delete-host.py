#!/usr/bin/python
import argparse
import sys
import MySQLdb 
import requests
import os

parser = argparse.ArgumentParser(description='Delete server from Icinga2')
 
parser.add_argument('host',
    help="Host Name")

args = parser.parse_args()

#conn = MySQLdb.connect(host= "localhost",
#                  user="root",
#                  passwd="Alyan2757622",
#                  db="icinga")
#x = conn.cursor()
#try:
#   x.execute("""INSERT INTO icinga_general (host, address, display_name, vars_service, vars_production, vars_datacenter, vars_app, vars_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(args.host, args.address, args.display_name, args.vars_service, args.vars_production, args.vars_datacenter, args.vars_app, args.vars_type))
#   conn.commit()
#except:
#   conn.rollback()
#conn.close()

print(args.host)

os.system('curl -k -s -u icinga:icinga -H \'Accept: application/json\' -X DELETE \'https://192.168.253.134:5665/v1/objects/hosts/%s?cascade=1\'' % (args.host))
