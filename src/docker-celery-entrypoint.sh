#!/bin/bash
celery worker --app=src.celery:app --loglevel=INFO --logfile=/srv/code/django_app/logs/celery.log