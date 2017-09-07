# Flyzer
NetFlow Based Botnet Analyzer

[![Kibana Version](https://img.shields.io/badge/Kibana-5.5.0-green.svg)](https://www.elastic.co/start)

Flyzer is a set of custom configuration tweaks to ELK stack, that will help you find botnet activities in your network with netflow output.

## Introduction
There have been lots of botnet detection method in computer networks, some of them work perfectly, some of them has some false positives and false negatives. As botnet evolve, detection methods have to revolve to catch botnets. This method detects botnet based on similiar flows and has nothing to do with packet payload and DPI.


## Prerequisite
This method is maily developed over ELK stack and has been tested on multiple elasticsearch instances.

## ELK installation
ELK Installation procedure is straight forward, if you are new to ELK stack, you might find [this] (https://www.elastic.co/start) helpful.

## Configuration
