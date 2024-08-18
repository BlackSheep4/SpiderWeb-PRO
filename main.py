#!/bin/python3

# Importaciones
import sys
from config import banner
from config.libraries import subprocess, Fore, Style, init
#from modules import library_checking, vulnerability_updater
from modules.advanced_os_detection import AdvancedStealthOSDetection
#from modules.library_checking import LibraryChecker
from modules.waf_detection import firewall_detection
from modules.helper_panel import help_panel

def main_function():
    # Mostrar banner
    banner

    # Crear instancia de la clase
    #library_checker = LibraryChecker()
    # Verificar que las bibliotecas necesarias estén instaladas
    #library_checker.check_required_libraries_installed()
    # Verificar si el programa se está ejecutando con privilegios de sudo
    #library_checker.check_sudo_privileges()

    # Verificar si se proporcionaron suficientes argumentos de línea de comandos
    #if len(sys.argv) < 3:
    #    print("Use: python main.py <target> <choice>")
    #    sys.exit(1)

    if sys.argv[1] == "help":
        #library_checker.fix_required_libraries()
        help_panel()
    else:
        pass
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "BASIC RECOGNITION" + Fore.RED + "]")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "01" + Fore.RED + "] " + Fore.WHITE + "Advanced Stealth OS Detection")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "01" + Fore.RED + "] " + Fore.WHITE + "DNS Lookup")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "08" + Fore.RED + "] " + Fore.WHITE + "Cloudflare Detection")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "03" + Fore.RED + "] " + Fore.WHITE + "Robots.txt Dumping")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "05" + Fore.RED + "] " + Fore.WHITE + "Banner Grabbing")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "04" + Fore.RED + "] " + Fore.WHITE + "IP Geolocation")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "04" + Fore.RED + "] " + Fore.WHITE + "ASN Discovery")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "04" + Fore.RED + "] " + Fore.WHITE + "URL Endpoint Discovery Crawler")

        #print(Fore.RED + "\n\t[" + Fore.GREEN + "SCANNERS" + Fore.RED + "]")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "05" + Fore.RED + "] " + Fore.WHITE + "Phone Scanner")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "05" + Fore.RED + "] " + Fore.WHITE + "Email Scanner")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "08" + Fore.RED + "] " + Fore.WHITE + "CMS Scanner")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "08" + Fore.RED + "] " + Fore.WHITE + "Port Scanner")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "08" + Fore.RED + "] " + Fore.WHITE + "Subdomain Scanner")

        #print(Fore.RED + "\n\t[" + Fore.GREEN + "FUZZERS" + Fore.RED + "]")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "05" + Fore.RED + "] " + Fore.WHITE + "Subdomain Fuzzer")
        #print(Fore.RED + "\n\t[" + Fore.GREEN + "05" + Fore.RED + "] " + Fore.WHITE + "Web Path Fuzzer")

        #if choice == '1' or choice == '01':
        #    detection = AdvancedStealthOSDetection(target)
        #    detection.passive_ttl_method()
        #    detection.active_nmap_method()
        #    # detection.banner_grabbing()
        #    detection.pypof_detection()
        #elif choice == '2' or choice == '02':
        #    firewall_detection.detect(target)
        #else:
        #    print(f"Elección no válida: {choice}")
        #    sys.exit(1)

if __name__ == "__main__":
    main_function()
