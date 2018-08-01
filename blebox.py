from lib.switchBoxD_API import Blebox
import time

dev1='http://192.168.1.201'
dev2='http://192.168.1.202'
dev3='http://192.168.1.203'

dev=[dev1,dev2,dev3]

for i in dev:
    blebox= Blebox(i)
    print(blebox.relay_state())
    time.sleep(1)

