#!/bin/python3

from .libraries import Fore, Style, init
import _curses

# Const
MAINTAINER = "BlackSheep4"
GITHUB = "https://github.com/BlackSheep4"

# Vars
version = 2.0

def print_banner():
    print(Fore.RED + r"""\n\n\t\t\tAIO Tool For """ + Fore.GREEN + r"""Information Gathering """ + Fore.RED + r"""And """ + Fore.GREEN + r"""Reconnaissance Scanner\n\t\t\t\t\t""" + Fore.RED + r"""[$] Current Version: """ +  Fore.GREEN + f"""{version}""")
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

    print(f"""\n\t\t\t\t""" + Fore.GREEN + f"""\tCoded By - """ + Fore.RED + f"""{MAINTAINER}""" + Fore.GREEN + f"""\n\tFind me on GitHub: """ + Fore.RED + f"""{GITHUB}\n""" + Style.RESET_ALL)

try:
    init()
except _curses.error:
    print("Terminal features are unavailable. Continuing without them.")

print_banner()

def main_function():
    try:
        target = input("\n[#] Enter the website to scan (e.g: example.com) >> ")
    except EOFError:
        print("No input received. Exiting...")
        exit(1)

main_function()
