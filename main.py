#!/bin/python3

import sys
from config import banner
from config.libraries import subprocess, Fore, Style, init
from modules.advanced_os_detection import AdvancedStealthOSDetection
from modules.waf_detection import firewall_detection
from modules.helper_panel import help_panel
from modules.about_me import aboutme_info

# Global Variables
option = sys.argv[1]
target = sys.argv[2]

def main_function():

    banner

    if option == "help":
        help_panel()
    
    elif option == "info":
        aboutme_info()

    elif option == "scan":
        AdvancedStealthOSDetection(target)
        AdvancedStealthOSDetection(target).passive_ttl_method()
        AdvancedStealthOSDetection(target).active_nmap_method()
        AdvancedStealthOSDetection(target).banner_grabbing()
        AdvancedStealthOSDetection(target).pypof_detection()

    else:
        print(f"Specified command does not exist")

if __name__ == "__main__":
    main_function()