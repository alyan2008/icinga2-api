#!/usr/bin/python
import argparse
import sys
import MySQLdb 
import requests
import os

parser = argparse.ArgumentParser(description='Delete server from Icinga2')
 
parser.add_argument('host',
    help="Host Name")

parser.add_argument('mod_args',
    choices=['address', 'display_name', 'vars.service', 'vars.production', 'vars.datacenter', 'vars.app', 'vars.type', 'vars.cpu'],
    help="Args which should be modified")

parser.add_argument('args_value',
    help="IP address or hostname")

args = parser.parse_args()

os.system('curl -k -s -u icinga:icinga -H \'Accept: application/json\' -X POST \'https://192.168.253.134:5665/v1/objects/hosts/%s\' -d \'{ "templates": [ "generic-host" ], "attrs": { "%s": "%s"} }\'' % (args.host, args.mod_args, args.args_value))
