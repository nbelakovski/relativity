#!/usr/bin/env bash -x

docker stop grafana
docker rm grafana
docker stop influx
docker rm influx