#!/bin/python3

from .libraries import Fore, Style, init

# Const
MAINTAINER = "BlackSheep4"
GITHUB = "https://github.com/BlackSheep4"

# Vars
version = 2.0

def print_banner():
    print(Fore.RED + f"""\n\n\t\t\tAIO Tool For """ + Fore.GREEN + f"""Information Gathering """ + Fore.RED + f"""And """ + Fore.GREEN + f"""Reconnaissance Scanner\n\t\t\t\t\t\t\t""" + Fore.RED + f"""[$] Current Version: """ +  Fore.GREEN + f"""{version}""")
    print(Fore.RED + f"""
                                                                                                                 
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

    print(f"""\n\t\t\t\t""" + Fore.GREEN + f"""\t\tCoded By - """ + Fore.RED + f"""{MAINTAINER}""" + Fore.GREEN + f"""\n\t\t\tFind me on GitHub: """ + Fore.RED + f"""{GITHUB}\n""" + Style.RESET_ALL)

print_banner()
