#!/bin/bash

export SETTINGS='config.DevelopmentConfig'

createuser -s publictitles
createdb -U publictitles -O publictitles publictitles -T template0

python manage.py db upgrade
python run_dev.py
