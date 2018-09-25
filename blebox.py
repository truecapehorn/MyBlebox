from blebox_API import SwichBoxD
import time
import argparse
import textwrap


class Devices:

    def __init__(self, name, noRelay, action, blebox):
        '''
        :param name: Nazwa wyjscia w bleboxie
        :param noRelay: Numer wyjyjscia
        :param action: akcja 1 LUB 0
        :param blebox: obiekt klasy odwoujacej sie do klasy SwichBoxD
        '''

        self.name = name
        self.noRelay = noRelay
        self.action = action
        self.blebox = blebox

    def relaySet(self):
        if self.action is not None:
            self.blebox.relay_set_get(self.noRelay, self.action)


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
        example:
            python3 belbox.py -hl 1
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
parser.add_argument('--status', action='store_true', default=False,
                    dest='action_status',
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
if action_lamp is not None:  # przypisanie akcji gupowych dla lamp
    action_hl = action_lamp
    action_hp = action_lamp
    action_l = action_lamp
    action_b = action_lamp
    action_k = action_lamp
    action_mp = action_lamp
action_all = results.action_all
if action_all is not None:  # przypisanie akcji gupowych wszystkie
    action_hl = action_all
    action_hp = action_all
    action_l = action_all
    action_b = action_all
    action_p = action_all
    action_w = action_all
    action_k = action_all
    action_mp = action_all
action_status = results.action_status

#   deklaracja numerow IP
ip_halospoty = '192.168.1.201'
ip_lampki = '192.168.1.202'
ip_kotlownia = '192.168.1.203'
ip_kuchnia = "192.168.1.204"
ip_wejscie = "192.168.1.205"
ips = [ip_halospoty, ip_lampki, ip_kotlownia]  # tablica z ipkami

#   dodanie nowych urzadzen blebox
halospoty = SwichBoxD(ip_halospoty)
lampki = SwichBoxD(ip_lampki)
kotlownia = SwichBoxD(ip_kotlownia)
kuchnia = SwichBoxD(ip_kuchnia)
wejscie = SwichBoxD(ip_wejscie)
swBox = [halospoty, lampki, kotlownia, kuchnia]  # tablica z bleboxami

#   deklaracja urzadzen dla bleboxow
hl = Devices("Halospoty lewe", 0, action_hl, halospoty)
hp = Devices("Halospoty prawe", 1, action_hp, halospoty)

l = Devices("Lampka nocna", 0, action_l, lampki)
b = Devices("Biurko", 1, action_b, lampki)

p = Devices("Piecyk", 0, action_p, kotlownia)
w = Devices("Wiatrak", 1, action_w, kotlownia)

k = Devices("Kuchnia", 1, action_k, kuchnia)
mp = Devices("Mały pokój", 0, action_mp, kuchnia)

we = Devices("Wejscie", 0, action_we, wejscie)
laz = Devices("Łazienka", 1, action_laz, wejscie)

devs = [hl, hp, l, b, p, w, k, mp]  # tablica obejektów z wszystkimi  urzadzeniami

#   akcja dla przekaznikow
for dev in devs:
    if dev.action is not None:
        print('{} - {}'.format(dev.name, dev.action))
        dev.relaySet()

#   odczyt ststusow bleboxow
if action_status == True:
    print('sprawdzenie stanow', action_status)
    for box in swBox:
        print(30 * "=")
        print("Blebox: ", box.device_adress)
        print("{}: {} ".format("WiFi Connect", box.wifi_connect()))
        print("{}: {} ".format("Wifi Status", box.wifi_status()))
        print("{}: {} ".format("Wifi Scan", box.wifi_scan()))
        print("{}: {} ".format("Device state", box.device_state()))
        print("{}: {} ".format("Device network", box.device_network()))
        print("{}: {} ".format("Up Time", box.device_uptime()))
        print("{}: {} ".format("Relay state", box.relay_state()))
        print("!!!Koniec testu dla: ", box.device_adress, " ", 60 * "/\\", "\n")
