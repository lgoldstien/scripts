# aws-connect.py
# Manage your connections to aws instances
# @package scripts
# @subpackage aws-connect
# @version 0.1
# @author lgoldstien

# Import our common set of functions
import os
import sys
import common

def main():
	# Get a list of hosts
	hosts = common.files('aws/hosts')

	# Get a list of keys
	keys = common.files('aws/keys')

	if len(keys) == 0:
		print common.term_colours("There are no keys saved in the aws/keys directory. Get some in there and make sure they end .pem", "red")
		quit = True
	if len(hosts) == 0:
		print common.term_colours("There are no hosts saved in the aws/hosts directory.", "red")
		quit = True
	if quit == True:
		print "There was an error, please fix and run the program again"
		sys.exit()


	# List the available hosts
	print common.term_colours("The following hosts are available to connect to:", "green")
	print ""
	i = 1
	for host in hosts:
		print common.term_colours( str(i) + " - " + host, "green")
		i += 1

	# Ask user to select a host
	chosen_host = hosts[int( raw_input("Choose a Host:") ) -1]

	# List the available keys
	print common.term_colours("The following keys are available to connect with:", "green")
	print ""
	i = 1
	for key in keys:
		print common.term_colours( str(i) + " - " + key, "green")
		i += 1

	# Ask user to select a host
	chosen_key = keys[int( raw_input("Choose a Key:") ) -1]

	# Ask the user to confirm they are happy with the action to be taken
	print "You have chosen the following:"
	print "Host: " + chosen_host
	print "Key: " + chosen_key
	username = raw_input("Please enter the username: ")

	confirm = common.confirm()

	if confirm == True:
		common.ssh_connect( chosen_host, username, key )
	elif confirm == False:
		print "Start again"
		main()

main()
