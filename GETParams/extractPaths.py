import urlparse
import argparse

parser = argparse.ArgumentParser(description='Script to extract paths from a list of URLs')
parser.add_argument('-u', required=True, dest="urlFile", help="specifies the file where the URLS are specified",
                    action="store")

args = parser.parse_args()
urlFile = args.urlFile


urls = []

#function to extract path
def extractpath(url):
    parsed = urlparse.urlparse(url)
    return parsed.path.rstrip()    


with open(urlFile) as f:
    for line in iter(f):
        if extractpath(line) not in urls:
            urls.append(extractpath(line))
f.close()

for i in urls:
    print i
