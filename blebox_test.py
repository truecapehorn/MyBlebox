from lib.blebox_API import *
import concurrent.futures
import time
import random
from termcolor import colored

swBox1 = SwichBoxD('192.168.1.201')
swBox2 = SwichBoxD('192.168.1.202')
swBox3 = SwichBoxD('192.168.1.203')
swBox4 = SwichBoxD('192.168.1.204')
swBox5 = SwichBoxD('192.168.1.205')
tempSensor1 = TempSensor('192.168.1.206')

print(Blebox.__doc__, '\n')

t1 = time.perf_counter()


def box_test(box):
    t3 = time.perf_counter()
    try:
        dev_state = box.device_state()
        if 'switchBoxD' in dev_state['device']['type']:
            state1 = f"Relay Get: {box._relay_state()}\nSwitch State: {box._switch_state()}"
        elif "tempSensor" in dev_state['device']['type']:
            state1 = f"Temp Sensor data: {box._getData()}"
        state = state1
        wyj = f"{30 * '='}\n{dev_state['device']['type']} - Blebox adress: {box.device_adress}\n" \
              f"Dev State: {box.device_state()}\n" \
              f"WiFi Connect: {box.wifi_connect()}\n" \
              f"Wifi Status: {box.wifi_status()}\n" \
              f"Wifi Scan: {box.wifi_scan()}\n" \
              f"Up Time: {box.device_uptime()}\n" \
              f"{state}\n" \
              f"Koniec testu dla {box.device_adress}. {colored(f'Czas: {time.perf_counter() - t3:.2f} sec.', 'green')}\n"
        return wyj
    except Exception:
        return f"{30 * '='}\n{colored(f'Problem z odpaleniem modułu: {box.device_adress} !!!', 'red')}\n"


bleboxes = [swBox1, swBox2, swBox3, swBox4, swBox5, tempSensor1]
with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(box_test, bleboxes)

for result in results:
    print(result)

# print(30 * "=", '\n', "Uruchominie lampki")
# print(swBox2._relay_set_get(1, 1))
# time.sleep(5)
# print(swBox2._relay_set_get(1, 0))

t2 = time.perf_counter()
print(f"{colored(f'Program wykonał sie w {t2 - t1:.2f} sec.', 'yellow')}")
