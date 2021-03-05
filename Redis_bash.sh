#!/bin/bash

sudo apt update
sudo apt install redis-server
sudo systemctl status redis
redis-cli ping
pip3 install redis
