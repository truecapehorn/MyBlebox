from lib.switchBoxD_API import Blebox
import time
import argparse
import textwrap



parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
        
        --------------------------------------------------------

        --------------------------------------------------------
        '''))


parser.add_argument('-hl', action='store', dest='action_hl', type=int,
                    help='Sterowanie halospoty lewe')
parser.add_argument('-hp', action='store', dest='action_hp', type=int,
                    help='Sterowanie halospoty prawe')
parser.add_argument('-hp', action='store', dest='action_hp', type=int,
                    help='Sterowanie halospoty prawe')
parser.add_argument('-ln', action='store', dest='action_ln', type=int,
                    help='Sterowanie lampka nocna')
parser.add_argument('-b', action='store', dest='action_b', type=int,
                    help='Sterowanie biurko')
parser.add_argument('-p', action='store', dest='action_p', type=int,
                    help='Sterowanie piecyk')
parser.add_argument('-w', action='store', dest='action_w', type=int,
                    help='Sterowanie piecyk')
parser.add_argument('-a', action='store', dest='action_a', type=int,
                    help='Sterowanie zbiorcze')




parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args()  # pobranie rezultatow parsera

action_hl=results.action_hl
action_hp=results.action_hp
action_ln=results.action_ln
action_b=results.action_b
action_p=results.action_p
action_w=results.action_w
action_a=results.action_a




ip_halospoty='192.168.1.201'
ip_lampki='192.168.1.202'
ip_kotlownia='192.168.1.203'
ips=[ip_halospoty,ip_lampki,ip_kotlownia]

halospoty=Blebox(ip_halospoty)
lampki=Blebox(ip_lampki)
kotlownia=Blebox(ip_kotlownia)
devs=[halospoty,lampki,kotlownia]



if __name__ == '__main__':

    for i in devs:
        blebox=i
        print(blebox.relay_state())
        time.sleep(1)

    lampki.relay_set_get(1,1)
    time.sleep(5)
    lampki.relay_set_get(1,0)

