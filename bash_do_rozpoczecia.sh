#!/bin/bash

FILE="env_programu"
if [ -f "$FILE" ]; then
    deactivate
    rm -r klplatforma_utrzymanie_wersji
    git clone https://github.com/Hamilkar247/klplatforma_utrzymanie_wersji.git
    cd klplatforma_utrzymanie_wersji
    virtualenv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
else 
    echo "$FILE nie istnieje - skopiuj env_programu.example, dostosuj scieszki i odpal skrypt raz jeszcze"
fi
