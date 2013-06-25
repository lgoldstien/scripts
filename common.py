# common.py
# The common functions needed by my python scripts
# @package scripts
# @version 0.1
# @author lgoldstien

import os

def ssh_connect ( host, username, key ):
	os.system("ssh -i " + key + " " + username + "@" + host)

def term_colours ( string, colour ):
    colours = { 'red': "\033[91m", 'green': "\033[32m", 'blue': "\033[34m" }
    stop = "\033[00m"
    return colours[colour] + string + stop

def dirs(dir):
    return os.walk('./' + dir).next()[1]

def files(dir):
	return os.listdir('./' + dir)
