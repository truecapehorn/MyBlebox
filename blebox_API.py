#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import time
import requests
import sys


# wifi_name = "ASUS_18_2G"
# wifi_pwd = "501195121"

class Blebox():
    """
    Obsluga Bleboxow

    """

    def __init__(self, device_adress, wifi_name="ASUS_18_2G", wifi_pwd="501195121"):
        self.device_adress = device_adress
        self.wifi_name = wifi_name
        self.wifi_pwd = wifi_pwd

    def makeUrl(self, api_adress):
        '''Generacja adresu url'''
        return 'http://' + self.device_adress + api_adress

    def request_get(self, url):
        '''Generacja requestu typu GET'''
        try:
            r = requests.get(url, timeout=3)
            # time.sleep(0.5)
            return r.json()
        except Exception as e:
            print(e)
            # sys.exit(0)

    def request_post(self, url, payload):
        '''Generacja requestu typu POST'''
        try:
            r = requests.post(url, data=json.dumps(payload), timeout=3)
            time.sleep(0.5)
            return r.json()
        except Exception as e:
            print(e)
            # sys.exit(0)

    def response_status(self, action, r):
        '''Wydrukowanie wynikow'''
        # Response, status etc
        print('\n' + 125 * '-' + '\n')
        print('* {0} dla URL: {1}\n  Kodowanie znaków: {2}\n'.format(action,
                                                                     r.url, r.apparent_encoding))
        print('* ODPOWIEDZ SERWERA:\n{0}\n'.format(r))  # TEXT/HTML
        # HTTP
        print(
            '* KOD STATUSU I STATUS:\n[{0} --> {1}]\n'.format(r.status_code, r.reason))
        print('* NAGLOWEK ODPOWIEDZI:\n{0}\n'.format(r.headers))
        print('<!---------koniec-----------!>')


class SwichBoxD(Blebox):
    '''Clasa opisujaca moduły SwichBoxD dziedziczy z klasy Blebox'''

    def device_set(self):
        '''Device - Change device configuration
            TX:
                "deviceName":New name of device.
                "network":Network section.
                "apSSID":New name of access point in device.
                "apPasswd":New password to access point in device.
            RX:
                "deviceName": New name of device.,
                "type": Type of device. In this example always: switchBox.,
                "fv": Firmware version.,
                "hv": Hardware version.,
                "id": Id of device..
        '''
        # ADRESS
        api_adress = '/api/device/set'
        url = self.makeUrl(api_adress)
        # POSTDATA
        payload = {
            "device": {"deviceName": "MYswitchBoxD"},
            "network": {"apSSID": self.wifi_name, "apPasswd": self.wifi_pwd}
        }

        return self.request_post(url, payload)

    def device_uptime(self):
        '''
            Device - Get device uptime
            RX:
                "uptime": Number of miliseconds from turning device on.
        '''
        # ADRESS
        api_adress = '/api/device/uptime'
        url = self.makeUrl(api_adress)
        # GET
        return self.request_get(url)  # GET

    def device_state(self):
        '''
            Device - Get information about device
            RX:
                "deviceName": Namhttps://www.raspberrypi.org/forums/viewtopic.php?f=63&t=138610e of device.,
                "type": Type of device. In this example always: switchBox.,
                "fv": Firmware version.,
                "hv": Hardware version.,
                "id": Id of device.,
                "ip": Device's IP in WiFi network.
        '''
        action = 'Device - Get information about device'
        # ADRESS
        api_adress = '/api/device/state'
        url = self.makeUrl(api_adress)
        return self.request_get(url)  # GET

    def device_network(self):
        '''
            Device - Get information about network
            RX:
                "ip": Device's IP in WiFi network.,
                "ssid": Name of connected WiFi network.,
                "station_status":Status of current conection with WiFi network.
                                Where: 0 - Not configured, 1 - Connecting, 2 -
                                Wrong password, 3 - WiFi network not found, 4 -
                                Error, 5 - Connected.,
                "apSSID": Name of access point in device.,
                "apPasswd": Password to access point in device
        '''
        action = 'Device - Get information about network'
        # ADRESS
        api_adress = '/api/device/network'
        url = self.makeUrl(api_adress)
        return self.request_get(url)  # GET

    def relay_set_post(self, state1, state2, name1, name2):
        '''
            Relays - Change relays configuration. POST method
            TX:,RX:
                "relay": Relay number.,
                "state": Current relay state. Where: 0 - OFF, 1 - ON.,
                "stateAfterRestart": Default state after resetting device.
                 Where: 0 - OFF, 1 - ON.,
                "name": Relay name.
        '''
        # ADRESS
        api_adress = '/api/relay/set'
        url = self.makeUrl(api_adress)
        # POSTDATA
        payload = {
            "relays":
                [{
                    "relay": 0,
                    "state": state1,
                    "stateAfterRestart": 2,
                    "name": name1
                }, {
                    "relay": 1,
                    "state": state2,
                    "stateAfterRestart": 2,
                    "name": name2
                }]
        }

        return self.request_post(url, payload)  # POST

    def relay_set_get(self, relay, state):
        '''
            Relays - Change relays configuration. GET method
            RX:
                "relay": Relay number., # GET
                "state": Current relay state. Where: 0 - OFF, 1 - ON.,
                "stateAfterRestart": Default state after resetting device.
                                    Where: 0 - OFF, 1 - ON.,
                "name": Relay name.
        '''
        # ADRESS
        api_adress = '/s/{0}/{1}'.format(relay, state)
        url = self.makeUrl(api_adress)
        return self.request_get(url)  # GET

    def relay_state(self):
        '''
            Relays - Get information about relays
            RX:
                "relay": Relay number.,
                "state": Current relay state. Where: 0 - OFF, 1 - ON.,
                "stateAfterRestart": Default state after resetting device.
                                    Where: 0 - OFF, 1 - ON.,
                "name": Relay name.
        '''
        # ADRESS
        api_adress = '/api/relay/state'
        url = self.makeUrl(api_adress)
        return self.request_get(url)  # GET

    def switch_state(self):
        '''
            Switch - Get information about switch configuration
            "outputMode": Current value of relation between output relays.
                        Where: 0 - independent outputs,
                        1 - push-pull outputs (only one at a time can be enabled).
        '''
        # ADRESS
        api_adress = '/api/switch/state'
        url = self.makeUrl(api_adress)
        return self.request_get(url)  # GET

    def wifi_connect(self):
        '''
            WiFi - Connect to WiFi network
            TX:
                "ssid":Name of WiFi network we want to connect.
                "pwd":Password of WiFi network we want to connect.
                        For open network this parameter should be an empty string.
            RX:
                "ssid": Name of connected WiFi network.
                "station_status": Status of current conection with WiFi network. Where:
                        0 - Not configured, 1 - Connecting, 2 - Wrong password,
                        3 - WiFi network not found, 4 - Error, 5 - Connected.,
                "ip":  	Device's IP in WiFi network.
        '''
        # ADRESS
        api_adress = '/api/wifi/connect'
        url = self.makeUrl(api_adress)
        # POSTDATA
        payload = {"ssid": self.wifi_name, "pwd": self.wifi_pwd}
        return self.request_post(url, payload)  # POST

    def wifi_disconnect(self):
        '''
            WiFi - Disconnect from WiFi network
        '''
        # ADRESS
        api_adress = '/api/wifi/disconnect'
        url = self.makeUrl(api_adress)
        # POSTDATA
        payload = {}
        return self.request_post(url, payload)  # POST

    def wifi_status(self):
        '''
            WiFi - Get information about connection to WiFi network
            RX:
            "scanning": Is scanning for WiFi networks in progress.,
            "ssid": Name of connected WiFi network.,
            "station_status": Status   of current conection with WiFi network. Where:
                            0 - Not configured, 1 - Connecting,
                            2 - Wrong password, 3 - WiFi network not found,
                            4 - Error, 5 - Connected.,
            "ip": Device's IP in WiFi network.
        '''
        # ADRESS
        api_adress = '/api/wifi/status'
        url = self.makeUrl(api_adress)
        return self.request_get(url)  # GET

    def wifi_scan(self):
        '''
            WiFi - Get nearby WiFi networks list
            RX:
            "ssid": Name of WiFi network.,
            "rssi": Signal strength of WiFi network (0-255)
            "enc": Encrytption of Wifi Network. Where: 0 - Not encrypted.
        '''
        # ADRESS
        api_adress = '/api/wifi/scan'
        url = self.makeUrl(api_adress)
        return self.request_get(url)  # GET


if __name__ == '__main__':
    dev1 = '192.168.1.201'
    dev2 = '192.168.1.202'
    dev3 = '192.168.1.203'

    swBox1 = SwichBoxD(dev1)
    swBox2 = SwichBoxD(dev2)
    swBox3 = SwichBoxD(dev3)
    swBox = [swBox1, swBox2, swBox3]

    for box in swBox:
        print(30 * "=")
        print("Blebox: ", box.device_adress)
        print("{}: {} ".format("WiFi Connect", box.wifi_connect()))
        print("{}: {} ".format("Wifi Status", box.wifi_status()))
        print("{}: {} ".format("Wifi Scan", box.wifi_scan()))
        print("{}: {} ".format("Relay Get", box.relay_state()))
        print("{}: {} ".format("Switch State", box.switch_state()))
        print("{}: {} ".format("Dev State", box.device_state()))
        print("{}: {} ".format("Up Time", box.device_uptime()))
        print("{}: {} ".format("Relay State", box.relay_state()))
        print("Koniec testu dla, ",box.device_adress)
    print("Uruchominie lampki")
    print(swBox2.relay_set_get(1, 1))
    time.sleep(5)
    swBox2.relay_set_get(1, 0)
