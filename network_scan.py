
from lib.blebox_API import *
import concurrent.futures
import time
import random
from termcolor import colored
t1 = time.perf_counter()

blebox_list=[]

def box_find(konc):
    adres=f"192.168.1.{konc}"

    sw=SwichBoxD(adres)
    state=sw.device_state()
    if type(state) is dict:
        return {"adress":adres,'type':state['device']['type']}

def check(adr):

    with concurrent.futures.ThreadPoolExecutor(max_workers=250) as executor:
        try:
            print(f"Sprawdznie adresu w przedziale 192.168.1.0-250")
            results = executor.map(box_find, adr)
        except Exception:
            pass

    for result in results:
        if result !=None:
            blebox_list.append(result)
    return blebox_list

if __name__=='__main__':
    address = [i for i in range(0, 250)]
    lista = check(address)
    print(lista)