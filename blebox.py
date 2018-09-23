from blebox_API import SwichBoxD
import time
import argparse
import textwrap

ip_halospoty = '192.168.1.201'
ip_lampki = '192.168.1.202'
ip_kotlownia = '192.168.1.203'
ip_kuchnia = "192.168.1.204"
ip_wejscie = "192.168.1.205"

ips = [ip_halospoty, ip_lampki, ip_kotlownia]

#   dodanie nowych urzadzen
halospoty = SwichBoxD(ip_halospoty)
lampki = SwichBoxD(ip_lampki)
kotlownia = SwichBoxD(ip_kotlownia)
kuchnia = SwichBoxD(ip_kuchnia)
wejscie = SwichBoxD(ip_wejscie)

swBox = [halospoty, lampki, kotlownia, kuchnia, wejscie]
devs_lamp = [halospoty, lampki]


def str2bool(v):
    if v.lower() in ('yes', 'true', 'on', 'y', '1'):
        return 1
    elif v.lower() in ('no', 'false', 'off', 'n', '0'):
        return 0
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def relay_out(r, nr_relay):
    try:
        return r["relays"][nr_relay]["name"], r["relays"][nr_relay]["state"]
    except Exception as e:
        print(e)


parser = argparse.ArgumentParser(
    prog='BleBox',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
        --------------------------------------------------------
        Uruchomienie bleboxow
        Dozwolone wartosci dla argumentow to:
            ('yes', 'true', 'on', 'y', '1')
            ('no', 'false', 'off', 'n', '0')
        --------------------------------------------------------
        '''))

parser.add_argument('-hl', action='store', dest='action_hl', type=str2bool,
                    help='Sterowanie halospoty lewe')
parser.add_argument('-hp', action='store', dest='action_hp', type=str2bool,
                    help='Sterowanie halospoty prawe')
parser.add_argument('-l', action='store', dest='action_l', type=str2bool,
                    help='Sterowanie lampka nocna')
parser.add_argument('-b', action='store', dest='action_b', type=str2bool,
                    help='Sterowanie biurko')
parser.add_argument('-p', action='store', dest='action_p', type=str2bool,
                    help='Sterowanie piecyk')
parser.add_argument('-w', action='store', dest='action_w', type=str2bool,
                    help='Sterowanie wiatrak')
parser.add_argument('-k', action='store', dest='action_k', type=str2bool,
                    help='Sterowanie kuchnia')
parser.add_argument('-mp', action='store', dest='action_mp', type=str2bool,
                    help='Sterowanie mały pokój')
parser.add_argument('-we', action='store', dest='action_we', type=str2bool,
                    help='Sterowanie wejście')
parser.add_argument('-laz', action='store', dest='action_laz', type=str2bool,
                    help='Sterowanie łazienka')

parser.add_argument('-a', action='store', dest='action_lamp', type=str2bool,
                    help='Sterowanie zbiorcze dla oswietenia')
parser.add_argument('-A', action='store', dest='action_all', type=str2bool,
                    help='Sterowanie zbiorcze wszystko')
parser.add_argument('--state', action='store_true', default=False,
                    dest='action_state',
                    help='Sprawdzenie stanow')

parser.add_argument('--version', action='version', version='%(prog)s 1.2')

results = parser.parse_args()  # pobranie rezultatow parsera

# odczyt akacji
action_hl = results.action_hl
action_hp = results.action_hp
action_l = results.action_l
action_b = results.action_b
action_p = results.action_p
action_w = results.action_w
action_k = results.action_k
action_mp = results.action_mp
action_we = results.action_we
action_laz = results.action_laz

action_lamp = results.action_lamp
action_all = results.action_all
action_state = results.action_state
actions = [action_hl, action_hp, action_l, action_b, action_p, action_w, action_lamp, action_all]

if action_hl != None:
    r = halospoty.relay_set_get(0, action_hl)
    print(relay_out(r, 0))
if action_hp != None:
    r = halospoty.relay_set_get(1, action_hp)
    print(relay_out(r, 1))

if action_l != None:
    r = lampki.relay_set_get(0, action_l)
    print(relay_out(r, 0))
if action_b != None:
    r = lampki.relay_set_get(1, action_b)
    print(relay_out(r, 1))

if action_p != None:
    r = kotlownia.relay_set_get(0, action_p)
    print(relay_out(r, 0))
if action_w != None:
    r = kotlownia.relay_set_get(1, action_w)
    print(relay_out(r, 1))

if action_k != None:
    r = kuchnia.relay_set_get(0, action_k)
    print(relay_out(r, 0))
if action_mp != None:
    r = kuchnia.relay_set_get(1, action_mp)
    print(relay_out(r, 1))

if action_we != None:
    r = wejscie.relay_set_get(0, action_we)
    print(relay_out(r, 0))
if action_laz != None:
    r = kuchnia.relay_set_get(1, action_laz)
    print(relay_out(r, 1))

if action_lamp != None:
    print('akcja grupowa', action_lamp)
    for dev in devs_lamp:
        for relay in [0, 1]:
            dev.relay_set_get(relay, action_lamp)
            # time.sleep(0.1)
            r = dev.relay_state()
            print(relay_out(r, relay))
if action_all != None:
    print('akcja grupowa', action_all)
    for dev in devs:
        for relay in [0, 1]:
            dev.relay_set_get(relay, action_all)
            # time.sleep(0.1)
            r = dev.relay_state()
            print(relay_out(r, relay))
if action_state == True:
    print('sprawdzenie stanow', action_state)
    for box in swBox:
        print(30 * "=")
        print("Blebox: ", box.device_adress)
        print("{}: {} ".format("WiFi Connect", box.wifi_connect()))
        print("{}: {} ".format("Wifi Status", box.wifi_status()))
        print("{}: {} ".format("Wifi Scan", box.wifi_scan()))
        print("{}: {} ".format("Relay Get", box.relay_state()))
        print("{}: {} ".format("Switch State", box.switch_state()))
        print("{}: {} ".format("Dev State", box.device_state()))
        print("{}: {} ".format("Up Time", box.devive_uptime()))
