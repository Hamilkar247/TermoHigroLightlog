# - *- coding: utf-8 - *-

import sys
import os

#*/1 * * * * cd /home/matball/Projects/TermoHigroLightLog/skrypty_klraspi && /home/matball/Projects/TermoHigroLightLog/skrypty_klraspi/venv/bin/python3 uruchom_skrypt_o_godzinie.py >>/home/matball/Projects/TermoHigroLightLog/logs.txt 2>&1
#*/1 * * * * cd /home/matball/Projects/TermoHigroLightLog/update_projektu_skryptu_klraspi && /home/matball/Projects/TermoHigroLightLog/update_projektu_skryptu_klraspi/venv/bin/python3 utrzymanie_wersji.py >>/home/matball/Projects/TermoHigroLightLog/logs.txt 2>&1

def main():
    path_basic="/home/matball/Projects/TermoHigroLightlog"
    glowny_kod="klplatforma_odbior_wysylka"
    python_venv="venv/bin/python3"
    updatejtowiec="klplatforma_utrzymanie_wersji"
    pierwszy=f"*/1 * * * * cd {path_basic}/{glowny_kod} && {path_basic}/{glowny_kod}/{python_venv} uruchom_skrypt_o_godzinie.py >>{path_basic}/logs.txt 2>&1"
    drugi=f"*/5 * * * * cd {path_basic}/{updatejtowiec} && {path_basic}/{updatejtowiec}/{python_venv} utrzymanie_wersji.py >>{path_basic}/logs_2.txt 2>&1"
    print(pierwszy)
    print(drugi)

if __name__ == "__main__":
    main()
