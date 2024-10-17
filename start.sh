#!/bin/bash
# Migrar base de datos
python3 manage.py migrate
# Iniciar Gunicorn para servir la aplicación
gunicorn --worker-tmp-dir /dev/shm sitioweb.wsgi:application --bind 0.0.0.0:$PORT
