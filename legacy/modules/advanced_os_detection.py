#!/bin/python3

from config.libraries import socket
from config.libraries import sys
from config.libraries import io
from config.libraries import subprocess
from config.libraries import re
#from config.libraries import nmap
from config.libraries import Fore, Style
from modules.waf_detection import firewall_detection

import nmap

class AdvancedStealthOSDetection:

    def __init__(self, target):
        
        self.target = target

        try:
            target = socket.gethostbyname(self.target)
            print(Fore.GREEN + f"[+] IP Address: " + Style.RESET_ALL + f"{target}")
        except Exception as e:
            print(Fore.RED + f"[*] Impossible to get the IP Address for the given domain" + Style.RESET_ALL)
    
    def passive_ttl_method(self):

        # Passive Method 1 - TTL
        print (Fore.YELLOW + "[!] Identifying Operative System based on the TTL..." + Style.RESET_ALL)
        os_list = ['Linux / FreeBSD', 'Windows', 'Solaris/AIX']

        try:
            ping = subprocess.Popen(f"ping -c 1 {self.target}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = ping.communicate()

            if error:
                print(Fore.RED + f"[*] Error: Cannot resolve host ({self.target})." + Style.RESET_ALL)
                return
            else:
                print(output)
                output = ping.communicate()[0]
                output_splitted = output.split()
                response = str(output_splitted)
                ttl_match = re.search(r'ttl=(\d+)', response)

                if ttl_match:
                    ttl = int(ttl_match.group(1))
                    print(Fore.GREEN + f"[+] TTL Detected: " + Style.RESET_ALL + f"{ttl}")

                    if ttl > 0 and ttl <= 64:
                        print(Fore.GREEN + "[+] OS Identified: " + Style.RESET_ALL + os_list[0])
                    elif ttl >= 65 and ttl <= 128:
                        print(Fore.GREEN + f"[+] OS Identified: " + Style.RESET_ALL + os_list[1])
                    elif ttl >= 129 and ttl <= 256:
                        print(Fore.GREEN + f"[+] OS Identified: " + Style.RESET_ALL + os_list[2])

                    else:
                        print(Fore.RED + f"[*] TTL value not found in ping response. Was impossible to determine the OS based on the TTL" + Style.RESET_ALL)

        except Exception as e:
            print(Fore.RED + f"[*] General error. Cannot resolve unknown host" + Style.RESET_ALL)

    def pypof_detection(self):
        pass

    def shodan_detection(self):
        pass

    def censys_detection(self):
        pass

    def active_nmap_method(self):

        # Active Method 2 - NMAP
        print (Fore.YELLOW + "[!] Identifying Operative System using Agressive Scan..." + Style.RESET_ALL)

        # Captura la salida estándar
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()
            
        nm = nmap.PortScanner()
        print(nm.scan(hosts=self.target, arguments="-O"))

        # Restaura la salida estándar
        sys.stdout = original_stdout
        
        for host in nm.all_hosts():
            os_info = nm[host]['osmatch']
            if os_info:
                for os in os_info:
                    print(Fore.GREEN + "[+] Name: " + Style.RESET_ALL + f"{os['name']}")
                    print(Fore.GREEN + "[+] Accuracy: " + Style.RESET_ALL + f"{os['accuracy']}%")
                    if 'osclass' in os:
                        osclass_list = os['osclass']
                        for osclass in osclass_list:
                            print(Fore.GREEN + "[+] Class: " + Style.RESET_ALL + f"{osclass.get('type', 'Not found')}")
                            print(Fore.GREEN + "[+] Vendor: " + Style.RESET_ALL + f"{osclass.get('Vendor', 'Not found')}")
                            print(Fore.GREEN + "[+] OS Family: " + Style.RESET_ALL + f"{osclass.get('osfamily', 'Not found')}")
                            print(Fore.GREEN + "[+] OS Version: " + Style.RESET_ALL + f"{osclass.get('osversion', 'Not found')}")
                            cpe = ', '.join(osclass.get('cpe', []))
                            print(Fore.GREEN + f"[+] CPE: " + Style.RESET_ALL +  f"{cpe if cpe else 'Not found'}")        
                    else:
                        print(Fore.RED + "[*] OS could not be detected using agressive scan" + Style.RESET_ALL)
            
                
            else:
                print(Fore.RED + f"[*] OS could not be detected using agressive scan. Maybe {self.target} is under a WAF" + Style.RESET_ALL)
                firewall_detected = firewall_detection(self.target)

                if firewall_detected == True:
                    print("[+] Fragmenting packets for get the OS")
                else:
                    print("Firewall not detected")
                
                # Nota: Integración de WAF mediante llamada a su módulo
                # Nota 2: Integración de persistencia si no se detecta el SO pero si el WAF

