#!/bin/bash

#install.sh

sudo apt update
sudo apt install -y python3-pip
sudo apt-get install -y python3-venv

cd nihalgupta11213-me_buildout_xmeme
cd backend\ -\ xmeme

python3 -m venv venv
source ./venv/bin/activate

pip3 install -r requirements.txt


