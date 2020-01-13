
from lib.blebox_API import *
import concurrent.futures
import time
import random
from termcolor import colored
t1 = time.perf_counter()

from network_scan import check
address=[i for i in range(0,250)]
lista=check(address)
print('Znaleziono urzadznia:')
for i in lista:
    print(i)

bleboxes=[]
for dev in lista:
    if dev['type']=='switchBoxD':
        box=SwichBoxD(dev['adress'])
    elif dev['type']=='tempSensor':
        box=TempSensor(dev['adress'])
    bleboxes.append(box)


"""Test modułów blebox"""

# swBox1 = SwichBoxD('192.168.1.201')
# swBox2 = SwichBoxD('192.168.1.202')
# swBox3 = SwichBoxD('192.168.1.203')
# swBox4 = SwichBoxD('192.168.1.204')
# swBox5 = SwichBoxD('192.168.1.205')
# tempSensor1 = TempSensor('192.168.1.206')

print(Blebox.__doc__, '\n')


def box_test(box):
    global state
    t3 = time.perf_counter()
    try:
        if 'switchBoxD' in (type := box.device_state()['device']['type']):
            state = f"Relay Get: {box._relay_state()}\nSwitch State: {box._switch_state()}"
        elif "tempSensor" in type:
            state = f"Temp Sensor data: {box._getData()}"
        wyj = f"{40 * '='}\n{type} - adress: {box.device_adress}\n" \
              f"Dev State: {box.device_state()}\n" \
              f"WiFi Connect: {box.wifi_connect()}\n" \
              f"Wifi Status: {box.wifi_status()}\n" \
              f"Wifi Scan: {box.wifi_scan()}\n" \
              f"Up Time: {box.device_uptime()}\n" \
              f"{state}\n" \
              f"Koniec testu dla {box.device_adress}. {colored(f'Czas: {time.perf_counter() - t3:.2f} sek.', 'green')}\n"
        return wyj
    except Exception as e:
        return f"{40 * '='}\n{colored(f'Problem z odpaleniem modułu: {box.device_adress} !!!', 'red')} : {colored(f'{e}', 'magenta')}"


# bleboxes = [swBox1, swBox2, swBox3, swBox4, swBox5, tempSensor1]
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(box_test, bleboxes)

for result in results:
    print(result)


# print(30 * "=", '\n', "Uruchominie lampki")
# print(swBox2._relay_set_get(1, 1))
# time.sleep(5)
# print(swBox2._relay_set_get(1, 0))

print(f"{colored(f'Program wykonał sie w {time.perf_counter() - t1:.2f} sec.', 'yellow')}")

