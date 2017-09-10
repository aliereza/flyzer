# Flyzer [![Version](https://img.shields.io/badge/release-none-lightgrey.svg)]()
NetFlow/S-Flow/IPFIX Based Botnet Analyzer

Flyzer is a set of custom configuration tweaks to ELK stack, that will help you find botnet activities in your network with netflow output.

[![elasticsearch Version](https://img.shields.io/badge/elasticsearch-v5.5.2-green.svg)](https://github.com/elastic/elasticsearch)
[![logstash Version](https://img.shields.io/badge/logstash-v5.5.2-green.svg)](https://github.com/elastic/logstash)
[![kibana Version](https://img.shields.io/badge/kibana-v5.5.2-green.svg)](https://github.com/elastic/kibana)
[![NetFlow Version](https://img.shields.io/badge/NetFlow-5%2C%209-blue.svg)]()

## Introduction
There have been lots of botnet detection method in computer networks, some of them work perfectly, some of them has some false positives and false negatives. As botnet evolve, detection methods have to revolve to catch botnets. This method detects botnet based on similiar flows and has nothing to do with packet payload and DPI.


## Prerequisite
This method is maily developed over ELK stack and has been tested on multiple elasticsearch instances. Make sure you are using the latest stable realease of ELK stack.

## ELK installation
ELK Installation procedure is straight forward, if you are new to ELK stack, you might find [this](https://www.elastic.co/start) helpful.

## ELK Configuration


### Installation
Flyzer has been tested on latest major linux distribution (CentOS, RHEL, Debian, Ubuntu), maker sure you have updated your ELK installation to the latest stable version.

run this command to install flyzer:

```sh
# curl -o https://
# chmod a+x flyzer-installer.sh
# ./flyzer-installer.sh
```


### Netflow input
Logstash has fully functional netflow plugin which works seamlessly, start listening for flows by this sample. Complete configuration is under Configuration Folder.


```sh
input {
  udp {
    host => "0.0.0.0"
    port => 2055
    codec => netflow {
      versions => [5, 9]
    }
    type => netflow
  }
```

### Elasticsearch output
Flows that has been captured by logstash has to be pushed into elasticsearch as documents. This is a sample configuration for pushing them into elasticsearch. Make sure that you point to the right elasticsearch instance.

```sh
output {
  elasticsearch {
    hosts => ["localhost:9200"]
    sniffing => true
    manage_template => false
    index => "%{[@metadata][beat]}-%{+YYYY.MM.dd}"
    document_type => "%{[@metadata][type]}"
  }
}
```

## Network Appliance Configuration


#### Cisco Router
```cisco
router-2621(config)#interface FastEthernet 0/1
router-2621(config-if)#ip route-cache flow
router-2621(config-if)#exit 
router-2621(config)#ip flow-export destination 192.168.9.101 2205
router-2621(config)#ip flow-export source FastEthernet 0/1
router-2621(config)#ip flow-export version 5
router-2621(config)#^Z
router-2621#show ip flow export
router-2621#show ip cache flow
```

#### Mikrotik Router
```mikrotik
/ip traffic-flow
set enabled=yes interfaces=Ether3-Firewall
/ip traffic-flow target
add dst-address=192.168.9.101
```
