#!/bin/bash
source /home/www/code/REACTLAB/venv/bin/activate
exec gunicorn -c "/home/www/code/REACTLAB/RUSALMA/gunicorn_config.py" RUSALMA.wsgi
