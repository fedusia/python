#!/usr/bin/env python

from elasticsearch import Elasticsearch, helpers
import datetime
import json
import argparse
import sys
import configparser

CONFIG_FILE = 'elasticdump.conf.example'


def parseConfig(configName):
    config = configparser.ConfigParser()
    config.read(configName)
    hosts = config['cluster']['hosts']
    return str(hosts).split()


def dumpIndex(hosts, indexName):
    es = Elasticsearch(hosts)
    currentDate = datetime.date.today()
    filename = indexName + '.' + currentDate.strftime("%Y-%m-%d") + '.dump'
    fd = open(filename, 'w')
    for i in helpers.scan(es, query={"query": {"match_all": {}}}, index=indexName, scroll='20m'):
        fd.write(json.dumps(i) + '\n')
    return


def restoreIndex(hosts, fileName):
    es = Elasticsearch(hosts)
    fileName = fileName
    fd = open(fileName, 'r')
    data = (json.loads(line) for line in fd.readlines())
    helpers.bulk(es, data)
    return


def main():
    esHosts = parseConfig(CONFIG_FILE)
    parser = argparse.ArgumentParser(description='Minimal tool for dump/restore elastic indexes',
                                     usage='\n%(prog)s dump indexname\n' \
                                           '%(prog)s restore filename.dump')
    parser.add_argument('action', type=str, help='dump/restore')
    parser.add_argument('source', type=str, help='Index for dump or file for restore')
    if len(sys.argv) == 1:
        args = parser.parse_args('-h')
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    if args.action == 'dump':
        dumpIndex(esHosts, args.source)
    if args.action == 'restore':
        restoreIndex(esHosts, args.source)


if __name__ == '__main__':
    main()
