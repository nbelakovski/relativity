#!/bin/bash -x

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

./bringdown.sh

docker run --rm -d --name=influx -p 8086:8086 influxdb
docker run --rm -d --name=grafana -p 3000:3000 grafana/grafana

python3 grafana_configuration.py
if [[ $? -ne 0 ]]; then
    exit -1
fi
python3 populate_database.py