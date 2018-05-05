#!/usr/bin/env bash -x

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

./bringdown.sh

docker run --rm -d --name=influx -p 8086:8086 influxdb
docker run --rm -d --name=grafana -p 3000:3000 grafana/grafana

python3 grafana_configuration.py
python3 populate_database.py