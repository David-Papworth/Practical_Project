#!/bin/bash

sudo apt update 
sudo apt install python3 python3-pip

pip3 install -r requirements.txt
export DATABASE_URI
export SECRET_KEY

python3 -m pytest front_end --junitxml=junit/test-results.xml --cov=app --cov-report=xml --cov-report=html
python3 -m pytest operator_random --junitxml=junit/test-results.xml --cov=app --cov-report=xml --cov-report=html
python3 -m pytest strat_random --junitxml=junit/test-results.xml --cov=app --cov-report=xml --cov-report=html
python3 -m pytest points --junitxml=junit/test-results.xml --cov=app --cov-report=xml --cov-report=html