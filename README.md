# MyBlebox
  Program do obslugi automatyki BleBox
  
  ## O Programie

Uruchomienie bleboxow
Dozwolone wartosci dla argumentow to:
*   ('yes', 'true', 'on', 'y', '1')
*   ('no', 'false', 'off', 'n', '0')
    
##### argumenty opcjonalne:
*  -h, --help      show this help message and exit
*  -hl ACTION_HL   Sterowanie halospoty lewe
*  -hp ACTION_HP   Sterowanie halospoty prawe
*  -l ACTION_L     Sterowanie lampka nocna
*  -b ACTION_B     Sterowanie biurko
*  -p ACTION_P     Sterowanie piecyk
*  -w ACTION_W     Sterowanie wiatrak
*  -a ACTION_LAMP  Sterowanie zbiorcze dla oswietenia
*  -A ACTION_ALL   Sterowanie zbiorcze wszystko
*  --state         Sprawdzenie stanow
*  --version       show program's version number and exit
  
  ## Przykłady
  
```
blebox -h       # uruchomienie pomocy
blebox -l on    # uruchomienie lamki nocnej
blebox -w 0     # wyłączenie wiatraka 
blebox -A 1     # włączynie wszystkich przekaźników w bleboxach
blebox --state  # sprawdznie stanu przekaźników
```