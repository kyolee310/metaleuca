#!/usr/bin/python
import xmlrpclib

def connect_to_cobbler(server, username, password):
    """
    Make the connection to the cobbler server that will be used for the
    all operations on the system. This will keep from having to make a 
    connection everytime we perform an operation on the server and should
    keep a (possible) huge connection load on the cobbler server

    server -- The IP or FQDN of the cobbler server
    username -- Username with admin rights on the cobbler server
    password -- Password of the corresponding username above
    """

    remote = xmlrpclib.Server("http://" + server + "/cobbler_api")
    token = remote.login(username, password)

    return remote, token


def display_distros(server):
	for x in server.get_distros():
		print "NAME: " + x['name'] + "\tOS_VERSION: " + x['os_version']

def display_profiles(server):
	for x in server.get_profiles():
		print "NAME: " + x['name'] + "\tKICKSTART: " + x['kickstart']

def display_systems(server):
	for x in server.get_systems():
		print "HOSTNAME: " + x['hostname'] + "\tPROFILE: " + x['profile']

def display_images(server):
	for x in server.get_images():
		print x

def display_repos(server):
	for x in server.get_repos():
		print x['mirror']


def main():

	COBBLER_SERVER = "192.168.62.1"
	USER = "cobbler"
	PASSWORD = "cobbler"

	server, token = connect_to_cobbler(COBBLER_SERVER, USER, PASSWORD)

	print "DISPLAY DISTROS"
	display_distros(server)
	print

	print "DISPLAY PROFILES"
	display_profiles(server)
	print

	print "DISPLAY SYSTEMS"
	display_systems(server)
	print

	print "DISPLAY IMAGES"
#	display_images(server)
	print

	print "DISPLAY REPOS"
#	display_repos(server)
	print

#	print server.get_distros()
#	print server.get_profiles()
#	print server.get_systems()
#	print server.get_images()
#	print server.get_repos()

if __name__ == "__main__":
    main()
    exit

