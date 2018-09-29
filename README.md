# MyBlebox
Program do obslugi automatyki BleBox <br />

## O Programie
Uruchamianie programu z wiersza polecen <br />

##### dozwolone wartosci dla argumentow to:
* dla włączenia przekaźnika: ('yes', 'true', 'on', 'y', '1')
* dla wyłączenia przekaźnika:  ('no', 'false', 'off', 'n', '0')
    
##### argumenty opcjonalne:
*  -h, --help          show this help message and exit
*  -hl  ACTION_HL      Sterowanie halospoty lewe
*  -hp  ACTION_HP      Sterowanie halospoty prawe
*  -l  ACTION_L        Sterowanie lampka nocna
*  -b  ACTION_B        Sterowanie biurko
*  -p  ACTION_P        Sterowanie piecyk
*  -f  ACTION_F        Sterowanie wiatrak
*  -k  ACTION_K        Sterowanie kuchnia
*  -mp  ACTION_MP      Sterowanie mały pokój
*  -we  ACTION_WE      Sterowanie holem
*  -zw  ACTION_ZW      Sterowanie oswietlenie zewnetrzne
*  -A  ACTION_ALL      Sterowanie zbiorcze wszystko
*  -a  ACTION_LAMP     Sterowanie zbiorcze dla oswietenia
*  -w  ACTION_WEJSCIE  Sterowanie zbiorcze lampy wejscie + kuchnia
*  -s  ACTION_SALON    Sterowanie zbiorcze lampy salon
*  --status            Sprawdzenie stanow
*  --version           show program's version number and exit

## Przykłady użycia
  
```
python3 blebox.py -b 1  # uruchominie w katalogu roboczym
# uruchomienia z aliasu
blebox -h               # uruchomienie pomocy
blebox -l on            # uruchomienie lamki nocnej
blebox -w 0             # wyłączenie wiatraka 
blebox -A 1             # włączynie wszystkich przekaźników w bleboxach
blebox --state          # sprawdznie stanu przekaźników
```
