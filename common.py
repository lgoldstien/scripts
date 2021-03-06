# common.py
# The common functions needed by my python scripts
# @package scripts
# @version 0.1
# @author lgoldstien

import os

def ssh_connect ( host, username, key ):
	os.system("ssh -i " + key + " " + username + "@" + host)

def term_colours ( string, colour ):
    colours = { 'red': "\033[91m", 'green': "\033[32m", 'blue': "\033[34m", 'yellow': "\033[33m", 'magenta': "\033[35m", 'cyan': "\033[36m" }
    stop = "\033[00m"
    return colours[colour] + string + stop

def dirs(dir):
    return os.walk('./' + dir).next()[1]

def files(dir):
	return os.listdir('./' + dir)

def confirm():
	goahead = raw_input( term_colours( "Are you happy with your selection? Y or N", "green" ) )
	if goahead == "Y":
		return True
	elif goahead == "N":
		return False
	else:
		print "Sorry you need to enter a Y or an N"
		confirm()

def make_dir(path):
	if ( os.path.exists(path) == True):
		return False
	else:
		if( os.makedirs(path) == True):
			return True
		else:
			return False


