#!/bin/ash

# Change to the app directory
cd /volumeBackend

sleep 3

# Run Django commands with absolute paths
./manage.py collectstatic --noinput
./manage.py makemigrations
./manage.py migrate

# Start Django development server
python manage.py runserver
