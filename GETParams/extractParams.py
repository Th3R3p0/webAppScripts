import sys
import urlparse
import json

# usage - extractParams.py {file.txt}

file = sys.argv[1]
#file = "testURLs.txt"

params = []

#function to extract path
def extractpath(url):
    parsed = urlparse.urlparse(url)
    return parsed.path.rstrip()    

# function to parse url and return all params and values in a json object
def parseurl(url):
    parsed = urlparse.urlparse(url)
    paramsandkeys = urlparse.parse_qs(parsed.query)
    return paramsandkeys

# function to extract params from json with params and values - return as list
def extractparams(url):
    paramsandkeys = parseurl(url)
    urlparams = paramsandkeys.keys()
    return urlparams

# function to parse the params and add unique ones to the params list
# This function should be reworked. Not very optimal
def checkuniqueparams(urlparams):
    t = "false"
    for i in params:
        if urlparams[0] in i:
            t = "true"
            for b in urlparams[1]:
                if b not in i[1]:
                    i[1].append(b)
    if t == "false":
        params.append(urlparams)        

# function to create a list of one single [path,param]
def listpathparam(path,param):
    a = []
    a.append(path)
    a.append(param)
    return a

# function to pull all params from url and append unique ones to the params list 
def parseparams(url):
    params = extractparams(url)
    path = extractpath(url)
    ulist = listpathparam(path,params)
    checkuniqueparams(ulist)


with open(file) as f:
    for line in iter(f):
        parseparams(line)
f.close()


for i in params:
    print i
