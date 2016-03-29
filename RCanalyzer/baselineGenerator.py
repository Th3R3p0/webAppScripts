import requests
import argparse

parser = argparse.ArgumentParser(description='Script to generate baseline for response code analyzer script')
parser.add_argument('-u', required=True, dest="url", help="specifies the base URL; prefix to the paths",
                    action="store")
parser.add_argument('-p', required=True, dest="pathsFile",
                    help="specifies the locations of the file which contains the list of paths", action="store")

args = parser.parse_args()
pathsFile = args.pathsFile

with open(pathsFile) as f:
    paths = eval(f.read())

responses = {"URL": args.url, "paths": paths, "Methods": {"GET":{},"POST":{},"PUT":{},"PATCH":{},"DELETE":{}}}

for i in paths:
    url = args.url + i
    r = requests.get(url)
    responses["Methods"]["GET"][i] = r.status_code
    r = requests.put(url)
    responses["Methods"]["PUT"][i] = r.status_code
    r = requests.post(url)
    responses["Methods"]["POST"][i] = r.status_code
    r = requests.patch(url)
    responses["Methods"]["PATCH"][i] = r.status_code
    r = requests.delete(url)
    responses["Methods"]["DELETE"][i] = r.status_code

print responses
