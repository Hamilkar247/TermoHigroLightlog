# - *- coding: utf-8 - *-

import os
import shutil
from funkcje_pomocnicze import ExceptionExistInstanceOfProcess, ExceptionVirtualenv, ExceptionRepository, FunkcjePomocnicze, ExceptionWindows, ExceptionNotExistFolder, ExceptionEnvProjektu

def nazwa_programu():
    return "pliki_z_logami_programu_i_ich_utylizacja.py"

def funkcje_pomocnicze_inicjalizacja():
    fp=FunkcjePomocnicze(nazwa_programu())
    return fp

def czy_plik_przekracza_dopuszczalny_rozmiar(element):
    fp=funkcje_pomocnicze_inicjalizacja()
    fp.drukuj("def: czy_plik_przekracza_dopuszczalny_rozmiar")
    scieszka_do_pliku=f"{os.getcwd()}/{element[0]}"
    fp.drukuj(f"scieszka_do_pliku: {scieszka_do_pliku}")
    #przerwij_i_wyswietl_czas()
    #sys.exit()
    if os.path.exists(scieszka_do_pliku):
        max_rozmiar_dla_tego_pliku=element[1]
        badany_plik = os.stat(scieszka_do_pliku)
        if int(badany_plik.st_size) > int(max_rozmiar_dla_tego_pliku):
            fp.drukuj(f"plik o scieszce {scieszka_do_pliku}")
            fp.drukuj(f"max rozmiar dla tego pliku {max_rozmiar_dla_tego_pliku}")
            fp.drukuj(f"rozmiar pliku {badany_plik.st_size}")
            #kopiuje obecny plik jako stary - a ten stary zastapi
            shutil.copy(scieszka_do_pliku, scieszka_do_pliku+".old")
            #zeruje stary plik na nowe logi
            file=open(scieszka_do_pliku, "w")
            file.write("\n")
            file.close()
    else:
        fp.drukuj("nie ma pliku")


def main():
    fp=funkcje_pomocnicze_inicjalizacja()
    tablica_plikow_i_max_zakresy=[
        ["klplatforma_odbior_wysylka/wyslane_krotki.json", 20000],
        ["klplatforma_odbior_wysylka/odebrane_jsony_z_alarmami.json", 10000],
        ["klplatforma_odbior_wysylka/odebrane_jsony_z_konfiguracjami.json", 10000],
        ["klplatforma_odbior_wysylka/plik_z_krotkami_logi.json", 20000],
        ["logs.txt", 20000],
        ["logs_2.txt", 20000],
        ["logs_3.txt", 20000],
        ["reboot.log", 20000]
        ]
    fp.drukuj("sprawdzam rozmiar plikow z logami")
    for plik_do_sprawdzenia in tablica_plikow_i_max_zakresy:
         czy_plik_przekracza_dopuszczalny_rozmiar(plik_do_sprawdzenia)

if __name__ == "__main__":
    main()
