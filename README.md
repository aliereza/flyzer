# Flyzer
NetFlow Based Botnet Analyzer

Flyzer is a set of custom configuration tweaks to ELK stack, that will help you find botnet activities in your network with netflow output.

[![elasticsearch Version](https://img.shields.io/badge/elasticsearch-5.5.2-green.svg)](https://github.com/elastic/elasticsearch)
[![logstash Version](https://img.shields.io/badge/logstash-5.5.2-green.svg)](https://github.com/elastic/logstash)
[![kibana Version](https://img.shields.io/badge/kibana-5.5.2-green.svg)](https://github.com/elastic/kibana)

## Introduction
There have been lots of botnet detection method in computer networks, some of them work perfectly, some of them has some false positives and false negatives. As botnet evolve, detection methods have to revolve to catch botnets. This method detects botnet based on similiar flows and has nothing to do with packet payload and DPI.


## Prerequisite
This method is maily developed over ELK stack and has been tested on multiple elasticsearch instances. Make sure you are using the latest stable realease of ELK stack.

## ELK installation
ELK Installation procedure is straight forward, if you are new to ELK stack, you might find [this](https://www.elastic.co/start) helpful.

## Configuration

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