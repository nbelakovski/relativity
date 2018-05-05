#!/usr/bin/env python3

import requests

# Setup grafana data source
grafana_url = "http://admin:admin@localhost:3000/"
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
