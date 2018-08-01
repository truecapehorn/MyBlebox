#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import time

device_adress = 'http://192.168.1.201'
wifi_name = "ASUS_18_2G"
wifi_pwd = "501195121"


def response_status(action, r):
    '''Wydrukowanie wynikow'''
    # Response, status etc
    print('\n' + 125 * '-' + '\n')
    print('* {0} dla URL: {1}\n  Kodowanie znaków: {2}\n'.format(action,
                                                                 r.url, r.apparent_encoding))
    print('* ODPOWIEDZ SERWERA:\n{0}\n'.format(r.text))  # TEXT/HTML
    # HTTP
    print(
        '* KOD STATUSU I STATUS:\n[{0} --> {1}]\n'.format(r.status_code, r.reason))
    print('* NAGLOWEK ODPOWIEDZI:\n{0}\n'.format(r.headers))
    print('<!---------koniec-----------!>')


def device_set(device_adress):
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
    action = 'Device - Change device configuration'
    # ADRESS
    api_adress = '/api/device/set'
    url = device_adress + api_adress
    # POSTDATA
    payload = {
        "device": {"deviceName": "MYswitchBoxD"},
        "network": {"apSSID": wifi_name, "apPasswd": wifi_pwd}
    }
    # POST with form-encoded data
    #r = requests.post(url, data=payload)
    r = requests.post(url, data=json.dumps(payload))
    # Response, status etc
    response_status(action, r)


def devive_uptime(device_adress):
    '''
        Device - Get device uptime
        RX:
            "uptime": Number of miliseconds from turning device on.
    '''
    action = 'Device - Get device uptime'
    # ADRESS
    api_adress = '/api/device/uptime'
    url = device_adress + api_adress
    # GET
    r = requests.get(url)
    # Response, status etc
    response_status(action, r)


def device_state(device_adress):
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
    url = device_adress + api_adress
    # GET
    r = requests.get(url)
    # Response, status etc
    response_status(action, r)


def device_network(device_adress):
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
    url = device_adress + api_adress
    # GET
    r = requests.get(url)
    # Response, status etc
    response_status(action, r)


def relay_set_post(device_adress,state1, state2):
    '''
        Relays - Change relays configuration. POST method
        TX:,RX:
            "relay": Relay number.,
            "state": Current relay state. Where: 0 - OFF, 1 - ON.,
            "stateAfterRestart": Default state after resetting device.
             Where: 0 - OFF, 1 - ON.,
            "name": Relay name.
    '''
    action = 'Relays - Change relays configuration. POST method'
    # ADRESS
    api_adress = '/api/relay/set'
    url = device_adress + api_adress
    # POSTDATA
    payload = {
        "relays":
            [{
                "relay": 0,
                "state": state1,
                "stateAfterRestart": 2,
                "name": "Q0"
            }, {
                "relay": 1,
                "state": state2,
                "stateAfterRestart": 2,
                "name": "Q1"
            }]
    }

    # POST with form-encoded data
    # r = requests.post(url, data=payload)
    r = requests.post(url, data=json.dumps(payload))
    # Response, status etc
    response_status(action, r)


def relay_set_get(device_adress,relay, state):
    '''
        Relays - Change relays configuration. GET method
        RX:
            "relay": Relay number., # GET
            "state": Current relay state. Where: 0 - OFF, 1 - ON.,
            "stateAfterRestart": Default state after resetting device.
                                Where: 0 - OFF, 1 - ON.,
            "name": Relay name.
    '''
    action = 'Relays - Change relays configuration. GET method'
    # ADRESS
    api_adress = '/s/{0}/{1}'.format(relay, state)
    url = device_adress + api_adress
    # GET
    r = requests.get(url)
    # Response, status etc
    #response_status(action, r)



def relay_state(device_adress):
    '''
        Relays - Get information about relays
        RX:
            "relay": Relay number.,
            "state": Current relay state. Where: 0 - OFF, 1 - ON.,
            "stateAfterRestart": Default state after resetting device.
                                Where: 0 - OFF, 1 - ON.,
            "name": Relay name.
    '''
    action = 'Relays - Get information about relays'
    # ADRESS
    api_adress = '/api/relay/state'
    url = device_adress + api_adress
    # GET
    r = requests.get(url)
    # Response, status etc
    response_status(action, r)
    return r


def switch_state(device_adress):
    '''
        Switch - Get information about switch configuration
        "outputMode": Current value of relation between output relays.
                    Where: 0 - independent outputs,
                    1 - push-pull outputs (only one at a time can be enabled).
    '''
    action = 'Switch - Get information about switch configuration'
    # ADRESS
    api_adress = '/api/switch/state'
    url = device_adress + api_adress
    # GET
    r = requests.get(url)
    # Response, status etc
    response_status(action, r)


def wifi_connect(device_adress):
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
    action = 'WiFi - Connect to WiFi network'
    # ADRESS
    api_adress = '/api/wifi/connect'
    url = device_adress + api_adress
    # POSTDATA
    payload = {"ssid": wifi_name, "pwd": wifi_pwd}
    # POST with form-encoded data
    #r = requests.post(url, data=payload)
    r = requests.post(url, data=json.dumps(payload))
    # Response, status etc
    response_status(action, r)


def wifi_disconnect(device_adress):
    '''
        WiFi - Disconnect from WiFi network
    '''
    action = 'WiFi - Disconnect from WiFi network'
    # ADRESS
    api_adress = '/api/wifi/disconnect'
    url = device_adress + api_adress
    # POSTDATA
    payload = {}
    # POST with form-encoded data
    #r = requests.post(url, data=payload)
    r = requests.post(url, data=json.dumps(payload))
    # Response, status etc
    response_status(action, r)


def wifi_status(device_adress):
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
    action = 'WiFi - Get information about connection to WiFi network'
    # ADRESS
    api_adress = '/api/wifi/status'
    url = device_adress + api_adress
    # GET
    r = requests.get(url)
    # Response, status etc
    response_status(action, r)


def wifi_scan(device_adress):
    '''
        WiFi - Get nearby WiFi networks list
        RX:
        "ssid": Name of WiFi network.,
        "rssi": Signal strength of WiFi network (0-255)
        "enc": Encrytption of Wifi Network. Where: 0 - Not encrypted.
    '''
    action = 'WiFi - Get nearby WiFi networks list'
    # ADRESS
    api_adress = '/api/wifi/scan'
    url = device_adress + api_adress
    # GET
    r = requests.get(url)
    # Response, status etc
    response_status(action, r)

if __name__ == '__main__':
    relay_state(device_adress)
