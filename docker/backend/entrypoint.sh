#!/bin/ash

# Change to the app directory

cd /volumeBackend

sleep 3

# Run Django commands with absolute path
./manage.py makemigrations
./manage.py migrate

# Start Django development server
python manage.py runserver 0.0.0.0:8000
