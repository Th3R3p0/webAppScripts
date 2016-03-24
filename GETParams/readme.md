Tool to extract params or values from GET requests

First setup burp as the interception proxy. Then capture traffice from web app. Select all of the URLs from the proxy history and copy the URLs (make sure only URLs in scope are selected). Paste into a file of yoru choice (ex: urls.txt).

Usage:
extractParams.py url.txt
