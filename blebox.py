from lib.switchBoxD_API import Blebox
import time

ip_halospoty='192.168.1.201'
ip_lampki='192.168.1.202'
ip_kotlownia='192.168.1.203'
ips=[ip_halospoty,ip_lampki,ip_kotlownia]

halospoty=Blebox(ip_halospoty)
lampki=Blebox(ip_lampki)
kotlownia=Blebox(ip_kotlownia)
devs=[halospoty,lampki,kotlownia]


for i in devs:
    blebox=i
    print(blebox.relay_state())
    time.sleep(1)

lampki.relay_set_get(1,1)
time.sleep(5)
lampki.relay_set_get(1,0)

