#!/bin/bash

pwd
cd backend\ -\ xmeme

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 8081

