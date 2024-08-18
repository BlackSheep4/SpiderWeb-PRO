#!/bin/python3

import argparse
from config import banner
from config.libraries import subprocess, Fore, Style, init
from modules.advanced_os_detection import AdvancedStealthOSDetection
from modules.waf_detection import firewall_detection
from modules.helper_panel import help_panel
from modules.about_me import aboutme_info

def main_function(args):
    # Mostrar el banner
    banner()

    if args.option == "help":
        help_panel()

    elif args.option == "info":
        aboutme_info()

    elif args.option == "scan":
        os_detection = AdvancedStealthOSDetection(args.target)
        os_detection.passive_ttl_method()
        os_detection.active_nmap_method()
        os_detection.banner_grabbing()
        os_detection.pypof_detection()

    else:
        print(f"Specified command '{args.option}' does not exist.")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="AIO Tool For Information Gathering And Automatic Vulnerability Scanner")
    parser.add_argument('option', choices=['help', 'info', 'scan'], help="Command to execute: 'help', 'info', or 'scan'.")
    parser.add_argument('target', nargs='?', help="Target for the scan (required for 'scan' command).")

    args = parser.parse_args()

    if args.option == 'scan' and not args.target:
        parser.error("The 'scan' command requires the target argument.")
    
    main_function(args)