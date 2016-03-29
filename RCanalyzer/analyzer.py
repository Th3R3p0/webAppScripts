import requests
import argparse

responses = {"GET":{},"POST":{},"PUT":{},"PATCH":{},"DELETE":{}}

parser = argparse.ArgumentParser(description='Script to compare response codes')
parser.add_argument('-b', required=True, dest="baselineFile",
                    help="specifies the locations of the file which contains the baseline dictionary", action="store")

args = parser.parse_args()
baselineFile = args.baselineFile

with open(baselineFile) as f:
    baseline = eval(f.read())

url = baseline['URL']
paths = baseline['paths']

for i in paths:
    url = baseline['URL']+i
    r = requests.get(url)
    responses["GET"][i] = r.status_code
    r = requests.put(url)
    responses["PUT"][i] = r.status_code
    r = requests.post(url)
    responses["POST"][i] = r.status_code
    r = requests.patch(url)
    responses["PATCH"][i] = r.status_code
    r = requests.delete(url)
    responses["DELETE"][i] = r.status_code

diffs = 0
for method in baseline["Methods"]:
    for path, response in baseline["Methods"][method].iteritems():
        if responses[method][path] != response:
            diffs += 1
            print "Found diff: %s %s" % (path, responses[method][path])
            print "Expected:   %s %s \n" % (path, response)

print "%d diffs found" % diffs
