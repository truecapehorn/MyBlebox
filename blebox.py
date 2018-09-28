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
        :param blebox: obiekt odwoujacy sie do klasy SwichBoxD
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
parser.add_argument('-f', action='store', dest='action_f', type=str2bool,
                    help='Sterowanie wiatrak')

parser.add_argument('-k', action='store', dest='action_k', type=str2bool,
                    help='Sterowanie kuchnia')
parser.add_argument('-mp', action='store', dest='action_mp', type=str2bool,
                    help='Sterowanie mały pokój')

parser.add_argument('-we', action='store', dest='action_we', type=str2bool,
                    help='Sterowanie holem')
parser.add_argument('-zw', action='store', dest='action_zw', type=str2bool,
                    help='Sterowanie oswietlenie zewnetrzne')

parser.add_argument('-A', action='store', dest='action_all', type=str2bool,
                    help='Sterowanie zbiorcze wszystko')
parser.add_argument('-a', action='store', dest='action_lamp', type=str2bool,
                    help='Sterowanie zbiorcze dla oswietenia')
parser.add_argument('-w', action='store', dest='action_wejscie', type=str2bool,
                    help='Sterowanie zbiorcze lampy wejscie + kuchnia')
parser.add_argument('-s', action='store', dest='action_salon', type=str2bool,
                    help='Sterowanie zbiorcze lampy salon')

parser.add_argument('--status', action='store_true', default=False,
                    dest='action_status',
                    help='Sprawdzenie stanow')

parser.add_argument('--version', action='version', version='%(prog)s 1.2')

actions = vars(parser.parse_args())  # pobranie wartosci akcji z namespace parasera w postaci slownika

# zadeklarowanie akcji
actionAll = ["action_hl", "action_hp", "action_l", "action_b", "action_p", "action_w", "action_k", "action_mp",
             "action_we", "action_zw", ]
actionLamps = ["action_hl", "action_hp", "action_l", "action_b", "action_k", "action_mp", "action_we", "action_zw", ]
actionWejscie = ["action_hl", "action_hp", "action_k ", "action_mp", "action_we", "action_zw", ]
actionSalon = ["action_l", "action_b", ]

if actions["action_lamp"] is not None:  # przypisanie akcji gupowej dla wszystkich lamp
    for i in actionLamps:
        actions[i] = actions["action_lamp"]

if actions["action_all"] is not None:  # przypisanie akcji gupowej wszystkie urzadzenia
    for i in actionAll:
        actions[i] = actions["action_all"]

if actions["action_wejscie"] is not None:  # przypisanie akcji gupowej dla lamp wejsciowych
    for i in actionWejscie:
        actions[i] = actions["action_wejscie"]

if actions["action_salon"] is not None:  # przypisanie akcji gupowej dla lamp w salonie
    for i in actionSalon:
        actions[i] = actions["action_salon"]

# deklaracja numerow IP
ip_halospoty = '192.168.1.201'
ip_lampki = '192.168.1.202'
ip_kotlownia = '192.168.1.203'
ip_kuchnia = "192.168.1.204"
ip_wejscie = "192.168.1.205"
ips = [ip_halospoty, ip_lampki, ip_kotlownia, ip_kuchnia, ip_wejscie]  # tablica z ipkami

#   dodanie nowych urzadzen blebox
halospoty = SwichBoxD(ip_halospoty)
lampki = SwichBoxD(ip_lampki)
kotlownia = SwichBoxD(ip_kotlownia)
kuchnia = SwichBoxD(ip_kuchnia)
wejscie = SwichBoxD(ip_wejscie)
swBox = [halospoty, lampki, kotlownia, kuchnia, wejscie]  # tablica z bleboxami

#   deklaracja urzadzen dla bleboxow
hl = Devices("Halospoty lewe", 0, actions["action_hl"], halospoty)
hp = Devices("Halospoty prawe", 1, actions["action_hp"], halospoty)

l = Devices("Lampka nocna", 0, actions["action_l"], lampki)
b = Devices("Biurko", 1, actions["action_b"], lampki)

p = Devices("Piecyk", 0, actions["action_p"], kotlownia)
f = Devices("Wiatrak", 1, actions["action_f"], kotlownia)

k = Devices("Kuchnia", 1, actions["action_k"], kuchnia)
mp = Devices("Mały pokój", 0, actions["action_mp"], kuchnia)

we = Devices("Wejście", 0, actions["action_we"], wejscie)
zw = Devices("Zewnetrzne", 1, actions["action_zw"], wejscie)

devs = [hl, hp, l, b, p, f, k, mp, we, zw]  # tablica obejektów z wszystkimi  urzadzeniami

#   akcja dla przekaznikow
for dev in devs:
    if dev.action is not None:
        print('{} - {}'.format(dev.name, dev.action))
        dev.relaySet()

#   odczyt ststusow bleboxow
if actions["action_status"] == True:
    print('sprawdzenie stanow', actions["action_status"])
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
