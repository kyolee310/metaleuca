#!/usr/bin/python

import re
import sys
import commands
import MySQLdb as mdb

class ResourceManager:

#	TEMP_GROUP_FILE = "./var/temp_machine_map_for_cobbler.lst"
	TEMP_GROUP_FILE = "./var/machine_map_for_new_datacenter.lst"


	def display_group_by_name(self, group):
		cmd = "cat " + self.TEMP_GROUP_FILE				###	QUICK HACK, Prefers DB
		if group is "_ALL":
			return commands.getoutput(cmd)
		else:
			cmd = cmd + " | grep " + group
			return commands.getoutput(cmd)


	def display_only_freed_group_by_name(self, group):
		grouplist = self.display_group_by_name(group)
		freed = self.display_user_by_name("FREED")
		freed_systems = freed.split('\n')
		freedhash = {}
		for freed_system in freed_systems:
			words = freed_system.split()
			ip = words[0]
			freedhash[ip] = 1
		glist = grouplist.split('\n')
		message = ""
		for g in glist:
			gwords = g.split()
			if len(gwords) > 0:
				this_ip = gwords[0]
				this_group = gwords[1]
				if this_ip in freedhash.keys():
					message += this_ip + "\t" + this_group + "\tFREED\n"
		return message.rstrip()


	def display_user_by_name(self, user):
		con = mdb.connect('localhost', 'root', 'foobar', 'eucaqa');
		with con: 
    			cur = con.cursor(mdb.cursors.DictCursor)
			if user is "_ALL":
    				cur.execute("SELECT ip, owner FROM reserve_machine_pool_records")
			else:
				cur.execute("SELECT ip, owner FROM reserve_machine_pool_records WHERE owner='" + user + "'")
			rows = cur.fetchall()
			message = ""
			if len(rows) == 0:
				message = "No system under user: " + user
			else:
				for row in rows:
					message += "%s\t%s\n" % (row["ip"], row["owner"])
			return message.rstrip()
		
