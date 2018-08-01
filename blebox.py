from lib import switchBoxD_API
import time

dev1='http://192.168.1.201'
dev2='http://192.168.1.202'
dev3='http://192.168.1.203'

dev=[dev1,dev2,dev3]

for i in dev:
    switchBoxD_API.relay_state(i)
    time.sleep(1)
