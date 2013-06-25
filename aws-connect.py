# aws-connect.py
# Manage your connections to aws instances
# @package scripts
# @subpackage aws-connect
# @version 0.1
# @author lgoldstien

# Import our common set of functions
import os
import common

def main():
	# Get a list of hosts
	hosts = common.files('aws/hosts')

	# Get a list of keys
	keys = common.files('aws/keys')

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
