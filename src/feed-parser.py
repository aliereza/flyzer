#This is a file for fethching threatfeed from isc.sans.edu and parse JSON format into readable CSV file for logstash translate filter

import json
import csv
import urllib

url = "https://isc.sans.edu/api/threatcategory/bots?json"
response = urllib.urlopen(url)
threatfeed = json.loads(response.read())
print threatfeed



