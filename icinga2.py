#!/usr/bin/python
import argparse
import sys
import MySQLdb 
import requests
import os

parser = argparse.ArgumentParser(description='Add server to Icinga2')
 
parser.add_argument('host',
    help="Host Name")

parser.add_argument('address',
    help="IP address or hostname")

parser.add_argument('display_name',
    help="display_name")

parser.add_argument('vars_service',
    choices=['service1', 'service2', 'service3'],
    help="Service Name")

parser.add_argument('vars_role',
    choices=['role1', 'role2', 'role3'],
    help="Service Name")
 
parser.add_argument('vars_production',
    choices=['YES', 'NO'],
    help="Production Server")

parser.add_argument('vars_datacenter',
    choices=['datacenter1', 'datacenter2'],
    help="Datacenter Name")

parser.add_argument('vars_app',
    choices=['app1', 'app2'],
    help="App Name")

parser.add_argument('vars_type',
    choices=['type1', 'type2'],
    help="Type Name")

parser.add_argument('vars_cpu',
    choices=['cpu_load_0_20', 'cpu_load_0_30'],
    help="CPU thresholds")

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

os.system('curl -k -s -u icinga:icinga -H \'Accept: application/json\' -X PUT \'https://192.168.253.134:5665/v1/objects/hosts/%s\' -d \'{ "templates": [ "generic-host" ], "attrs": { "address": "%s", "check_command": "hostalive", "display_name" : "%s", "vars.service" : "%s", "vars.production" : "%s", "vars.datacenter" : "%s", "vars.app" : "%s", "vars.type" : "%s", "vars.role" : "%s", "vars.cpu" : "%s"} }\'' % (args.host, args.address, args.display_name, args.vars_service, args.vars_production, args.vars_datacenter, args.vars_app, args.vars_type, args.vars_role, args.vars_cpu))
