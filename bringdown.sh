#!/bin/bash -x

docker stop grafana
docker rm grafana
docker stop influx
docker rm influx