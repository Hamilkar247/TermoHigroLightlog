#!/usr/bin/env python3

import os
import sys 
from funkcje_pomocnicze import ExceptionExistInstanceOfProcess, ExceptionVirtualenv, ExceptionRepository, FunkcjePomocnicze, ExceptionWindows, ExceptionNotExistFolder, ExceptionEnvProjektu

def nazwa_programu():
    return "pliki_z_logami_programu_i_ich_utylizacja.py"

def funkcje_pomocnicze_inicjalizacja():
    fp=FunkcjePomocnicze(nazwa_programu())
    return fp

def main():
    fp=funkcje_pomocnicze_inicjalizacja()
    fp.drukuj("proba reboota")
    os.system('/sbin/reboot')

if __name__ == "__main__":
    main()
