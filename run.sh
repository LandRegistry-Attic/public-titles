#!/bin/bash

export SETTINGS='config.DevelopmentConfig'
export DATABASE_URL='postgresql://localhost/publictitles'

createuser -s publictitles
createdb -U publictitles -O publictitles publictitles -T template0

python manage.py db upgrade
python run_dev.py
