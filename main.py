#!/bin/python3

# Importations
from config import banner
from config.libraries import subprocess, Fore, Style, init
from modules import library_checking, vulnerability_updater
from modules.advanced_os_detection import AdvancedStealthOSDetection
from modules.library_checking import LibraryChecker
from modules.waf_detection import firewall_detection


def main_function():
    # Show banner
    banner

    # Create instance class
    library_checker = LibraryChecker()
    # Check for required library modules
    library_checker.check_required_libraries_installed()
    # Check if program is running with sudo privileges
    library_checker.check_sudo_privileges()

    # Target Input
    global target
    target = input("\n[#] Enter the website to scan (e.g: example.com) >> ")

    if target == "fix":
        library_checker.fix_required_libraries()
    elif target == "update":
        vulnerability_updater.vuln_updater()
    elif target == "help":
        helper_panel.help_panel()
    else:
        print(Fore.RED + "\n\t[" + Fore.GREEN + "BASIC RECOGNITION" + Fore.RED + "]")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "01" + Fore.RED + "] " + Fore.WHITE + "Advanced Stealth OS Detection")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "01" + Fore.RED + "] " + Fore.WHITE + "DNS Lookup")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "08" + Fore.RED + "] " + Fore.WHITE + "Cloudflare Detection")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "03" + Fore.RED + "] " + Fore.WHITE + "Robots.txt Dumping")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "05" + Fore.RED + "] " + Fore.WHITE + "Banner Grabbing")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "04" + Fore.RED + "] " + Fore.WHITE + "IP Geolocation")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "04" + Fore.RED + "] " + Fore.WHITE + "ASN Discovery")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "04" + Fore.RED + "] " + Fore.WHITE + "URL Endpoint Discovery Crawler")


        print(Fore.RED + "\n\t[" + Fore.GREEN + "SCANNERS" + Fore.RED + "]")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "05" + Fore.RED + "] " + Fore.WHITE + "Phone Scanner")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "05" + Fore.RED + "] " + Fore.WHITE + "Email Scanner")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "08" + Fore.RED + "] " + Fore.WHITE + "CMS Scanner")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "08" + Fore.RED + "] " + Fore.WHITE + "Port Scanner")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "08" + Fore.RED + "] " + Fore.WHITE + "Subdomain Scanner")


        print(Fore.RED + "\n\t[" + Fore.GREEN + "FUZZERS" + Fore.RED + "]")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "05" + Fore.RED + "] " + Fore.WHITE + "Subdomain Fuzzer")
        print(Fore.RED + "\n\t[" + Fore.GREEN + "05" + Fore.RED + "] " + Fore.WHITE + "Web Path Fuzzer")

        choice = input("\nSelect an option >> ")

        if choice == '1' or '01':
            target = AdvancedStealthOSDetection(target)
            target.passive_ttl_method()
            target.active_nmap_method()
            #target.banner_grabbing()
            target.pypof_detection()
        elif choice == '2' or '02':
            firewall_detection
        else:
            pass
        
    

if __name__ == "__main__":
    main_function()
