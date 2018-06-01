#!/bin/bash

su -c "python3.6 manage.py bower install" django
su -c "python3.6 manage.py collectstatic" django
su -c "python3.6 manage.py migrate" django

su -c "gunicorn documenter.wsgi:application -b 0.0.0.0:8000 --workers=10" django
