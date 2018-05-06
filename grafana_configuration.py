#!/usr/bin/env python3

import requests
import time
import sys

# Setup grafana data source
grafana_url = "http://admin:admin@localhost:3000/"

# Wait for Grafana to come online (testing in linux VM showed this to take a few seconds
start = time.clock()
TIMEOUT_PERIOD=5 # seconds
grafana_up = False
while not grafana_up and (time.clock() - start < TIMEOUT_PERIOD):
    try:
        r = requests.get(grafana_url)
        grafana_up = r.ok
    except:
        pass

if not grafana_up:
    print("Could not connect to Grafana. Exiting")
    sys.exit(-1)


dbname = open('db_name', 'r').read()

data_source_dict = {
    "name": "btc_source",
    "type":"influxdb",
    "url":"http://localhost:8086",
    "access":"direct",
    "basicAuth":False,
    "database":dbname
}
r = requests.post(grafana_url + "api/datasources", data=data_source_dict)
assert r.ok, "Failed to create datasource within Grafana"
