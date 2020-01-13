
from lib.blebox_API import *
import concurrent.futures
import time
import random
from termcolor import colored
t1 = time.perf_counter()

blebox_list=[]

def box_find(adres):
    sw=SwichBoxD(adres)
    state=sw.device_state()
    if type(state) is dict:
        return {"adress":adres,'type':state['device']['type'], "deviceName":state['device']['deviceName']}

def check(adr):

    with concurrent.futures.ThreadPoolExecutor(max_workers=5000) as executor:
        try:
            print(f"Sprawdznie adresów")
            results = executor.map(box_find,adr)
        except Exception:
            pass

    for result in results:
        if result !=None:
            blebox_list.append(result)
    return blebox_list

if __name__=='__main__':
    # address = [f'192.168.1.{i}' for i in range(0, 250)]
    address=[f"192.168.{x}.{y}" for x in range(0,11) for y in range(0,250)]
    print(len(address))
    lista = check(address)
    print(lista)
    exit(0)