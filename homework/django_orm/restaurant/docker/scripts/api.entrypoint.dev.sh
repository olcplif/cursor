#!/usr/bin/env bash

./restaurant/docker/scripts/wait-for-it.sh restaurant-postgres:5432 -s -t 30 --

python restaurant/src/manage.py runserver 0.0.0.0:8000 || { echo 'runserver failed' ; exit 1; }
