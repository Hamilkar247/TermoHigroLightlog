#!/bin/bash

deactivate
cp update_projektu_skryptu_klraspi/.env_projektu .env_projektu
rm -r update_projektu_skryptu_klraspi
git clone https://github.com/Hamilkar247/update_projektu_skryptu_klraspi
cd update_projektu_skryptu_klraspi
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
mv ../.env_projektu .env_projektu
#python3 utrzymanie_wersji.py


