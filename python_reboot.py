# - *- coding: utf-8 - *-

import os
import sys 
from funkcje_pomocnicze import ExceptionExistInstanceOfProcess, ExceptionVirtualenv, ExceptionRepository, FunkcjePomocnicze, ExceptionWindows, ExceptionNotExistFolder, ExceptionEnvProjektu

def nazwa_programu():
    return "python_reboot.py"

def funkcje_pomocnicze_inicjalizacja():
    fp=FunkcjePomocnicze(nazwa_programu())
    return fp

def sprawdz_lsusb():
    cmd=f"lsusb | grep 'Realtek Semiconductor Corp. RTL2838 DVB-T'"
    output = os.popen(cmd).readlines()
    print(output)
    print(len(output))
    return len(output)

def main():
    fp=funkcje_pomocnicze_inicjalizacja()
    if sprawdz_lsusb() > 0:
        fp.drukuj("proba reboota")
        #os.system('/sbin/reboot') 
        fp.drukuj("jesli reboot sie odbyl poprawnie nie zobaczysz tej wiadomosci")       
    else:
        fp.drukuj("nie ma potrzeby reboota")

if __name__ == "__main__":
    main()
