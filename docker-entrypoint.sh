#!/bin/sh
set -e


if [[ "$2" = 'migrate-first' ]]; then
    exec python manage.py migrate --no-input
fi

if [[ "$1" = 'dev' ]]; then
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
fi


exec "$@"
