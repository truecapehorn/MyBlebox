from blebox_API import SwichBoxD
import time
import argparse
import textwrap

ip_halospoty = '192.168.1.201'
ip_lampki = '192.168.1.202'
ip_kotlownia = '192.168.1.203'
ips = [ip_halospoty, ip_lampki, ip_kotlownia]

halospoty = SwichBoxD(ip_halospoty)
lampki = SwichBoxD(ip_lampki)
kotlownia = SwichBoxD(ip_kotlownia)
devs = [halospoty, lampki, kotlownia]
devs_lamp = [halospoty, lampki]


def str2bool(v):
    if v.lower() in ('yes', 'true', 'on', 'y', '1'):
        return 1
    elif v.lower() in ('no', 'false', 'off', 'n', '0'):
        return 0
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def relay_out(r, nr_relay):
    return r["relays"][nr_relay]["name"], r["relays"][nr_relay]["state"]


parser = argparse.ArgumentParser(
    prog='PROG',
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
parser.add_argument('-a', action='store', dest='action_lamp', type=str2bool,
                    help='Sterowanie zbiorcze dla oswietenia')
parser.add_argument('-A', action='store', dest='action_all', type=str2bool,
                    help='Sterowanie zbiorcze wszystko')
parser.add_argument('--state', action='store_true', default=False,
                    dest='action_state',
                    help='Sprawdzenie stanow')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()  # pobranie rezultatow parsera

action_hl = results.action_hl
action_hp = results.action_hp
action_l = results.action_l
action_b = results.action_b
action_p = results.action_p
action_w = results.action_w
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
if action_lamp != None:
    print('akcja grupowa', action_lamp)
    for dev in devs_lamp:
        for relay in [0, 1]:
            dev.relay_set_get(relay, action_lamp)
            #time.sleep(0.1)
            r = dev.relay_state()
            print(relay_out(r, relay))
if action_all != None:
    print('akcja grupowa', action_all)
    for dev in devs:
        for relay in [0, 1]:
            dev.relay_set_get(relay, action_all)
            #time.sleep(0.1)
            r = dev.relay_state()
            print(relay_out(r, relay))
if action_state == True:
    print('sprawdzenie stanow', action_state)
    for dev in devs:
        print(dev.relay_state())
        #time.sleep(0.5)

