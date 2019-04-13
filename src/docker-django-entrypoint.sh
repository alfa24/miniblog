#!/bin/bash
python manage.py makemigrations
python manage.py migrate        # Apply database migrations
python manage.py collectstatic --noinput  # collect static files
# Prepare log files and start outputting logs to stdout
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &

echo Starting nginx 
# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn src.wsgi:application \
    --name django_hisect \
    --bind 127.0.0.1:8000 \
    --workers 3 \
    --log-level=info \
    --log-file=/srv/logs/gunicorn.log \
    --access-logfile=/srv/logs/access.log & 
exec service nginx start