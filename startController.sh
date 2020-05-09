#/bin/bash

uwsgi --http :9090 --wsgi-file controller.py --callable app
#export PIGPIOD_ADDR="localhost"
#export PIGPIO_PORT=8888
#sudo pigpiod
