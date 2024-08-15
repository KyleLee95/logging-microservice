#! /bin/bash

docker rm -f logging-service logging-mongodb
docker compose up --build
