''' 
This is a file for fethching threatfeed from isc.sans.edu and parse JSON format
into readable CSV file for logstash translate filter
'''
import urllib2
import json

url = "https://isc.sans.edu/api/threatcategory/bots?json"
url_read = urllib2.urlopen(url).read()
json_encoded = json.loads(url_read)

def encoder(data):
    for records in data:
        yield records["ipv4"] +","+ records["type"]
        
csv_content = '\n'.join(encoder(json_encoded))

with open('../db/botnet.csv', 'w') as f:
    f.write(csv_content)