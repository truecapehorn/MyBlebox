from lib.blebox_API import SwichBoxD
import time
from threading import Timer
import threading
from datetime import datetime

class RepeatableTimer(object):
    blok = False

    def __init__(self, interval, function, args=[], kwargs={}):
        self._interval = interval
        self._function = function
        self._args = args
        self._kwargs = kwargs

    def start(self):
        self.timerON()

    def timerON(self):
        self.t = Timer(self._interval, self._function, *self._args, **self._kwargs)
        self.t.start()
        print("t start")



# deklaracja numerow IP
ip_halospoty = '192.168.1.201'
ip_lampki = '192.168.1.202'
ip_kotlownia = '192.168.1.203'
ip_kuchnia = "192.168.1.204"
ip_wejscie = "192.168.1.205"
ips = [ip_halospoty, ip_lampki, ip_kotlownia, ip_kuchnia, ip_wejscie]  # tablica z ipkami

#   dodanie nowych urzadzen blebox
halospoty = SwichBoxD(ip_halospoty)
salon = SwichBoxD(ip_lampki)
kotlownia = SwichBoxD(ip_kotlownia)
kuchnia = SwichBoxD(ip_kuchnia)
wejscie = SwichBoxD(ip_wejscie)


def checkHalospoty():
    try:
        hl = halospoty.relay_state()['relays'][0]['state']
        hp = halospoty.relay_state()['relays'][1]['state']
        # print(hl, hp)
        time.sleep(0)
        if hp == 1 or hl == 1:
            return True
        else:
            return False
    except Exception as e:
        print(f"Błąd w checkHalospoty: {e}")
        return False


def buyrko():
    try:
        biurko = salon.relay_state()['relays'][1]['state']
        time.sleep(0)
        if biurko == 1:
            return True
        else:
            return False
    except Exception as e:
        print(f"Błąd w buyrko: {e}")
        return False


# Function to be called when the timer expires
def halospotyOff():
    try:
        halospoty.relay_set_get(1, 0)
        halospoty.relay_set_get(0, 0)
    except Exception as e:
        print(f"Błąd w halospotyOff: {e}")


def biurkoOff():
    try:
        salon.relay_set_get(1, 0)
    except Exception as e:
        print(f"Błąd w biurkoOff: {e}")


t1 = RepeatableTimer(5, halospotyOff)
t2 = RepeatableTimer(10, biurkoOff)

while True:
    # print('status?', check())
    if checkHalospoty() == True:
        t1.start()
    if buyrko() == True:
        t2.start()
    # print("Program glowny")
    time.sleep(1.0)
    print(t2.blok)
