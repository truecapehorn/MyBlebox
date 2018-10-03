from lib.blebox_API import SwichBoxD
import time
from threading import Timer
import threading
from datetime import datetime

class RepeatableTimer(object):
    blok=False

    def __init__(self, interval, function, args=[], kwargs={}):
        self._interval = interval
        self._function = function
        self._args = args
        self._kwargs = kwargs


    def start(self):
        if self.blok==False:
            self.t = Timer(self._interval, self._function, *self._args, **self._kwargs)
            self.t.start()
            print("t start")
        self.blok=self.t.is_alive()



def set_proc_name(newname):
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(len(newname) + 1)
    buff.value = newname
    libc.prctl(15, byref(buff), 0, 0, 0)


def get_proc_name():
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(128)
    # 16 == PR_GET_NAME from <linux/prctl.h>
    libc.prctl(16, byref(buff), 0, 0, 0)
    return buff.value


set_proc_name(b'blebox_norbert')

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


def check():
    hl = halospoty.relay_state()['relays'][0]['state']
    hp = halospoty.relay_state()['relays'][1]['state']
    #print(hl, hp)
    time.sleep(0)
    if hp == 1 or hl == 1:
        return True
    else:return False



seconds = 5


# Function to be called when the timer expires
def halospotyOff():
    halospoty.relay_set_get(1, 0)
    halospoty.relay_set_get(0, 0)



t=RepeatableTimer(5,halospotyOff)

start_time=0
while True:
    #print('status?', check())
    if check()==True:
        t.start()
    #print("Program glowny")
    time.sleep(0.0)
    print(t.blok)
