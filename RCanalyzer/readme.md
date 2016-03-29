# Response Code Analyzer

## Usage
baselineGenerator.py -u http://url.com -p pathToPathsFile  
This script generates the baseline dictionary needed for the analyzer script

analyzer.py -p pathsFile.txt
This script automates the process of performing basic  
CRUD analysis and checks response codes against a baseline
