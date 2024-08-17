#!/bin/python3

from .libraries import Fore, Style, init

# Const
MAINTAINER = "BlackSheep4"
GITHUB = "https://github.com/BlackSheep4"

# Vars
version = 2.0


def print_banner():

    print(Fore.RED + fr"""\n\n\t\t\tAIO Tool For """ + Fore.GREEN + fr"""Information Gathering """ + Fore.RED + fr"""And """ + Fore.GREEN + fr"""Reconnaissance Scanner\n\t\t\t\t\t\t\t""" + Fore.RED + fr"""[$] Current Version: """ +  Fore.GREEN + fr"""{version}""")
    print(Fore.RED + fr"""
                                                                                                                 
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

    print(fr"""\n\t\t\t\t""" + Fore.GREEN + fr"""\t\t{C} Coded By - """ + Fore.RED + fr"""{MAINTAINER}""" + Fore.GREEN + fr"""\n\t\t\t{I} Find me in github: """ + Fore.RED + """{GITHUB}\n""" + Style.RESET_ALL)

print_banner()