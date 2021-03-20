# coding=utf-8


import re


import subprocess
import os
import shutil
import hashlib
import logging
import socket
import yaml
import sys


def writeNetconnectdPassword(newPassword):
	# with open('/etc/netconnectd.yaml') as f:
	# 	doc = yaml.load(f)
	# 	doc['psk'] = str(newPassword)

	# with open('/etc/netconnectd.yaml', 'w') as f:
	# 	yaml.dump(doc, f)


	file_name = "/etc/netconnectd.yaml"
	with open(file_name) as f:
		doc = yaml.safe_load(f)
	# print str(doc)
	# print str(newPassword)
	# print str(sys.argv[0])
	# # self._logger.info(str(doc))
	# self._logger.info(type(doc))
	# doc['ap']['psk'] = newPassword['password']
	doc['ap']['psk'] = str(sys.argv[0])
	doc['ap']['psk'] = newPassword.strip()
	# self._logger.info(str(doc))
	with open(file_name, 'w') as f:
		yaml.safe_dump(doc, f, default_flow_style=False)

writeNetconnectdPassword(str(sys.argv[1]))
#print str(sys.argv[1])
# print str(sys.stdin.readline())