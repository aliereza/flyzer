#!/bin/bash
#This script fetch the list of dangerous IP address from isc.sans.edu and update the "Botnet.csv" file
#The mentioned file is being used by translate filter that check if the DST IP address is being listed.

$api_url = "https://isc.sans.edu/api/threatcategory/bots"
$curl = which curl

echo `$curl -XGET $api_url "zeuscc"`