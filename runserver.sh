#!/bin/sh

# updating conda environment
echo "Updating conda environment"
conda env update --file env.yaml

# starting the redis server
echo "Starting redis server"
docker run -p 6380:6380 -d redis:5

# running django
echo "Running migrations"
python manage.py migrate
echo "Starting django server"
python manage.py runserver