#!/bin/python3

from .libraries import Fore, Style, init
import _curses
import os

os.environ['TERM'] = 'xterm'

def print_banner():
    version = 2.0

    print(Fore.RED + "\n\n\t\t\tAIO Tool For " + Fore.GREEN + "Information Gathering " + Fore.RED + "And " + Fore.GREEN + f"Automatic Vulnerability Scanner\n\t\t\t\t\t\t\t" + Fore.RED + "[$] Current Version: " +  Fore.GREEN + f"{version}")
    print(Fore.RED + r"""
                                                                                                                 
  ______             __        __                      __       __            __                                        
 /      \           |  \      |  \                    |  \  _  |  \          |  \      
|  $$$$$$\  ______   \$$  ____| $$  ______    ______  | $$ / \ | $$  ______  | $$____  
| $$___\$$ /      \ |  \ /      $$ /      \  /      \ | $$/  $\| $$ /      \ | $$    \ 
 \$$    \ |  $$$$$$\| $$|  $$$$$$$|  $$$$$$\|  $$$$$$\| $$  $$$\ $$|  $$$$$$\| $$$$$$$
 _\$$$$$$\| $$  | $$| $$| $$  | $$| $$    $$| $$   \$$| $$ $$\$$\$$| $$    $$| $$  | $$
|  \__| $$| $$__/ $$| $$| $$__| $$| $$$$$$$$| $$      | $$$$  \$$$$| $$$$$$$$| $$__/ $$
 \$$    $$| $$    $$| $$ \$$    $$ \$$     \| $$      | $$$    \$$$ \$$     \| $$    $$
  \$$$$$$ | $$$$$$$  \$$  \$$$$$$$  \$$$$$$$ \$$       \$$      \$$  \$$$$$$$ \$$$$$$$ 
          | $$                                                                         
          | $$                                                                           
           \$$                                                                                                                                                                                                                            
    """)

    print("\n\t\t\t\t" + Fore.GREEN + "\t\t{C} Coded By - " + Fore.RED + "BlackSheep4" + Fore.GREEN + "\n\t\t\t{I} Find me on github: " + Fore.RED + "https://github.com/BlackSheep4\n" + Style.RESET_ALL)

try:
    init()
except _curses.error:
    print("Terminal features are unavailable. Continuing without them.")

print_banner()