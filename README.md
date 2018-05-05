This repo brings up an instance of influxDB and Grafana and begins to populate the DB with Bitcoin prices from Coinbase's API. It also provides a Grafana dashboard to see the price.

#### Requirements

To run the scripts in this repo, it is expected that the user have:
* Docker
* python3 (and the requests module)
* bash
* An internet connection

Any other dependencies/requirements will be added as they come up

#### Basic usage instructions
1) Run bringup.sh. It may be run from any directory. It will report "Done" but will not return control. This is OK as no other shell work is required.
2) Go to http://localhost:3000/dashboard/import, and login as admin/admin
3) Click "Upload .json file" and upload the BTC_USD_dashboard.json file from this repo.
4) You may leave the name alone, and choose "btc_source" from the dropdown for InfluxDB data source, and then hit import

You should now be looking at a live updating graph of the price of 1 Bitcoin in USD as reported by Coinbase.

To bring everything down, you may kill the initial script and then run bringdown.sh (also may be run from any directory)