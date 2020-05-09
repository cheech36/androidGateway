#/bin/bash

set -x

virtualenv venv --python=/usr/bin/python3 --system-site-packages
source venv/bin/activate
pip install uwsgi
pip install flask
pip install flask-wtf
