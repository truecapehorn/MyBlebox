from switchBoxD_API import Blebox
import time
import argparse
import textwrap


def str2bool(v):
    if v.lower() in ('yes', 'true', 'h', 'y', '1'):
        return 1
    elif v.lower() in ('no', 'false', 'l', 'n', '0'):
        return 0
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\

        --------------------------------------------------------

        --------------------------------------------------------
        '''))

parser.add_argument('-hl', action='store', dest='action_hl', type=str2bool,
                    help='Sterowanie halospoty lewe')
parser.add_argument('-hp', action='store', dest='action_hp', type=str2bool,
                    help='Sterowanie halospoty prawe')
parser.add_argument('-ln', action='store', dest='action_ln', type=str2bool,
                    help='Sterowanie lampka nocna')
parser.add_argument('-b', action='store', dest='action_b', type=str2bool,
                    help='Sterowanie biurko')
parser.add_argument('-p', action='store', dest='action_p', type=str2bool,
                    help='Sterowanie piecyk')
parser.add_argument('-w', action='store', dest='action_w', type=str2bool,
                    help='Sterowanie piecyk')
parser.add_argument('-a', action='store', dest='action_a', type=str2bool,
                    help='Sterowanie zbiorcze')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()  # pobranie rezultatow parsera

action_hl = results.action_hl
action_hp = results.action_hp
action_ln = results.action_ln
action_b = results.action_b
action_p = results.action_p
action_w = results.action_w
action_a = results.action_a
action = [action_hl, action_hp, action_ln, action_b, action_p, action_w, action_a]

ip_halospoty = '192.168.1.201'
ip_lampki = '192.168.1.202'
ip_kotlownia = '192.168.1.203'
ips = [ip_halospoty, ip_lampki, ip_kotlownia]

halospoty = Blebox(ip_halospoty)
lampki = Blebox(ip_lampki)
kotlownia = Blebox(ip_kotlownia)
devs = [halospoty, lampki, kotlownia]


for i in action:
    print(i)

if action_hl != None:
    print('halospoty lewe akcja', action_hl)
    halospoty.relay_set_get(0, action_hl)
if action_hp != None:
    print('halospoty prawe akcja', action_hp)
    halospoty.relay_set_get(1, action_hp)
if action_ln != None:
    print('lampka nocna akcja', action_ln)
    lampki.relay_set_get(0, action_ln)
if action_b != None:
    print('biurko akcja', action_b)
    lampki.relay_set_get(1, action_b)
if action_p != None:
    print('piecyk akcja', action_p)
    kotlownia.relay_set_get(0, action_p)
if action_w != None:
    print('wiatrak akcja', action_w)
    kotlownia.relay_set_get(1, action_w)
if action_a != None:
    print('akcja grupowa', action_a)
    for dev in devs:
        for relay in [0, 1]:
            print(dev.device_adress, relay, action_a)
            dev.relay_set_get(relay, action_a)
            time.sleep(1)

if __name__ == '__main__':
    for i in devs:
        blebox = i
        print(blebox.relay_state())
        time.sleep(1)
    lampki.relay_set_get(1, 1)
    time.sleep(5)
    lampki.relay_set_get(1, 0)
