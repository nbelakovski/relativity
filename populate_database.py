#!/usr/bin/env python3

import requests
import time

# First set up the database if it does not already exist
influx_url = "http://localhost:8086/"
dbname = open('db_name', 'r').read()

def create_database(dbname):
    r = requests.get(influx_url + 'query', params="q=SHOW DATABASES")
    # Get the values returned, but default to 0 in case there are no dbs yet
    existing_dbs = r.json()['results'][0]['series'][0].get('values', [])

    for db in existing_dbs:
        if db[0] == dbname:
            print("Database {} already exists, skipping creation".format(dbname))
            break
    else:
        # create db
        print("Database {} not found, creating...".format(dbname))
        r = requests.post(influx_url + 'query', data={'q':"CREATE DATABASE {}".format(dbname)})
        print("Done")


create_database(dbname)

# Now get some data and throw it in there
def get_btc_price():
    coinbase_url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    r = requests.get(coinbase_url)
    value = float(r.json()['data']['amount'])
    return value

def insert_value_into_db(value, dbname):
    r = requests.post(influx_url + 'write?db={}'.format(dbname), data="btcusd,source=coinbase value={}".format(get_btc_price()).encode())
    pass

while True:
    insert_value_into_db(get_btc_price(), dbname)
    time.sleep(5)
