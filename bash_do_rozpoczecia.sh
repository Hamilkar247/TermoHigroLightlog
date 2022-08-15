#!/bin/bash

deactivate
cp klplatforma_utrzymanie_wersji/.env_projektu .env_projektu
rm -r klplatforma_utrzymanie_wersji
git clone https://github.com/Hamilkar247/klplatforma_utrzymanie_wersji.git
cd klplatforma_utrzymanie_wersji
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
mv ../.env_projektu .env_projektu
#python3 utrzymanie_wersji.py


