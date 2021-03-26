#!/bin/bash

sudo apt install docker.io docker-compose -y
sudo docker-compose build
sudo docker-compose up -d