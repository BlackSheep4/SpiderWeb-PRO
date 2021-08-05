import subprocess
import time
import whois
from ip2geotools.databases.noncommercial import DbIpCity
import dns.resolver
import urllib.request
import requests
import re
import time
import platform
import socket
from bs4 import BeautifulSoup as bs
from Wappalyzer import Wappalyzer, WebPage
import warnings
import sys
import os
import phonenumbers
from phonenumbers import geocoder, carrier
from colorama import Fore, Style, init
init()


def banner():
    print(Fore.RED + """
  ____        _     _         __        __   _             _ 
 / ___| _ __ (_) __| | ___ _ _\ \      / /__| |__   __   _/ |
 \___ \| '_ \| |/ _` |/ _ \ '__\ \ /\ / / _ \ '_ \  \ \ / / |
  ___) | |_) | | (_| |  __/ |   \ V  V /  __/ |_) |  \ V /| |
 |____/| .__/|_|\__,_|\___|_|    \_/\_/ \___|_.__/    \_/ |_|
       |_|                                                   
    \t\t[Coded By: BlackSheep4]
    """)
    print(Style.RESET_ALL)

    
def pressAny():
    input('\n' + "Press any key to continue...")
    os.system('clear')
    
def main():
    print('\n' + "Welcome to SpiderWeb v1 - Information Gathering Tool" + '\n')

    print(Fore.RED + "\t[" + Fore.GREEN + "01" + Fore.RED + "] " + Fore.WHITE + "Operative System Detection")
    print(Fore.RED + "\t[" + Fore.GREEN + "02" + Fore.RED + "] " + Fore.WHITE + "WHOIS Information")
    print(Fore.RED + "\t[" + Fore.GREEN + "03" + Fore.RED + "] " + Fore.WHITE + "Target Geolocation")
    print(Fore.RED + "\t[" + Fore.GREEN + "04" + Fore.RED + "] " + Fore.WHITE + "DNS Dumping")
    print(Fore.RED + "\t[" + Fore.GREEN + "05" + Fore.RED + "] " + Fore.WHITE + "Robots.txt Extraction")
    print(Fore.RED + "\t[" + Fore.GREEN + "06" + Fore.RED + "] " + Fore.WHITE + "Get all the links from the target")
    print(Fore.RED + "\t[" + Fore.GREEN + "07" + Fore.RED + "] " + Fore.WHITE + "Server Detection")
    print(Fore.RED + "\t[" + Fore.GREEN + "08" + Fore.RED + "] " + Fore.WHITE + "Server Technologies Detection")
    print(Fore.RED + "\t[" + Fore.GREEN + "09" + Fore.RED + "] " + Fore.WHITE + "Phone Information Extractor")
    print(Fore.RED + "\n\t[" + Fore.GREEN + "10" + Fore.RED + "] " + Fore.WHITE + "Exit")
    print('\n')
    option = int(input("[+] Choose an option >> "))
    print(Style.RESET_ALL)

    
    int(option)
   
    if option == 1:
        target = str(input("[+] Target Domain >> "))
        url = f'http://www.{target}/'
        system = platform.system()
        target2 = socket.gethostbyname(target)

        if system == 'Linux':
            try:
                print('[!] GETTING OPERATIVE SYSTEM')
                time.sleep(1)
                ping = subprocess.Popen(f"ping -c 1 {target2}",shell=True,  stdout=subprocess.PIPE)
                out = ping.communicate()[0] #access stdoutdata
                out = out.split() #split by spaces
                out = str(out)

                ttl = re.search(r'ttl=(\d+)', out).group(1)
                ttl= int(ttl)

                if ttl >= 0 and ttl <= 64:
                    o_system = "LINUX"
                elif ttl >= 65 and ttl <= 128:
                    o_system = "WINDOWS"
                else:
                    o_system = "UNKNOWN"
                print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Server Operative System:" + Fore.GREEN + o_system)
                print(Style.RESET_ALL)
                pressAny()
            
            except (AttributeError):
                print('\n')
                print(Fore.RED + "[" + Fore.GREEN + "!" + Fore.RED + "] " + Fore.WHITE + 'An error occurred. It is possible that the server is down or that you have misspelled the IP or domain.')

        else:
            print('Please use this script in Linux OS')
            pressAny()

    elif option == 2:

        target = str(input("[+] Target Domain >> "))
        
        w = whois.whois(target)
        print(Fore.RED + "[" + Fore.GREEN + "!" + Fore.RED + "] " + Fore.WHITE + f"Getting WHOIS Information from {target}")
        time.sleep(0.5)
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Domain Names: " + str(w.get("domain_name")))
        time.sleep(0.3)
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Domain Name Servers: " + str(w.get("name_servers"))[2:-2])
        time.sleep(0.3)
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Organization: " + str(w.get("org")))
        time.sleep(0.3)
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Registration: " + str(w.get("registrar")))
        time.sleep(0.3)
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Emails: " + str(w.get("emails")))
        time.sleep(0.3)
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "DNSSec: " + str(w.get("dnssec")))
        time.sleep(0.3)
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Country: " + str(w.get("country")))
        time.sleep(0.3)
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "State: " + str(w.get("state")))
        time.sleep(0.3)
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "City: " + str(w.get("city")))
        time.sleep(0.3)
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Zipcode: " + str(w.get("zipcode")))
        time.sleep(0.3)
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Address: " + str(w.get("address")))

        pressAny()

    elif option == 3:

        target = str(input("[+] Target Domain >> "))
        target2 = socket.gethostbyname(target)

        response = DbIpCity.get(target2, api_key="free")
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Tracking IP Location")
        time.sleep(0.5)
        latitude = response.latitude
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Latitude: " + str(response.latitude))
        time.sleep(0.3)
        longitude = response.longitude
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Longitude: " + str(response.longitude))
        time.sleep(0.3)
        print("[+] Google Maps Track: " + f"https://google.es/maps/@{latitude},{longitude},15z?hl=en")

        pressAny()

    elif option == 4:

        target = str(input("[+] Target Domain >> "))

        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Starting DNS Dumping")
        mx = dns.resolver.resolve(target, 'MX')
        soa = dns.resolver.resolve(target, 'SOA')
        ns = dns.resolver.resolve(target, 'NS')
        time.sleep(0.5)

        print(Fore.RED + "[" + Fore.GREEN + "!" + Fore.RED + "] " + Fore.WHITE + "DUMPING MX SERVERS")
        for data in mx:
            print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "MX Servers: " + str(data.exchange) + "\t" + " PREFERENCE: " + str(data.preference))
            time.sleep(0.3)
        print(Fore.RED + "[" + Fore.GREEN + "!" + Fore.RED + "] " + Fore.WHITE + "DUMPING DOMAIN NAME SERVERS")
        for data in ns:
            print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Domain Name Servers: " + str(data.target))
            time.sleep(0.3)
        
        print(Fore.RED + "[" + Fore.GREEN + "!" + Fore.RED + "] " + Fore.WHITE + "DUMPING PRIMARY ZONE DOMAIN")
        for data in soa:
            print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "DNS Primary Zone: " + str(data.mname))
            time.sleep(0.3)

        pressAny()


    elif option == 5:

        target = str(input("[+] Target Domain >> "))

        print(Fore.RED + "[" + Fore.GREEN + "!" + Fore.RED + "] " + Fore.WHITE + "Trying to get robots.txt")

        robots = f'http://www.{target}/robots.txt'
        file = "robots.txt"

        request = requests.get(robots)
        if request.status_code == 200:
            r = urllib.request.urlopen(robots)
            f = open(file, 'wb')
            f.write(r.read())
            f.close
            print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "File Successfully Downloaded!")
        else:
            print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + f"Seems that {target} doesn´t have any robots.txt")

        pressAny()

    elif option == 6:

        target = str(input("[+] Target Domain >> "))
        url = f'http://www.{target}/'

        print(Fore.RED + "[" + Fore.GREEN + "!" + Fore.RED + "] " + Fore.WHITE + f"Getting all links from {target} ")

        req = requests.get(url)
        soup = bs(req.text, 'html.parser') #transform request to unicode and parse to HTML

        for link in soup.find_all('a'):
            time.sleep(0.2)
            print(link.get('href'))

        pressAny()

    elif option == 7:

        target = str(input("[+] Target Domain >> "))
        url = f'http://www.{target}/'

        r = requests.get(url)
        server = r.headers['Server']
        print(Fore.RED + "[" + Fore.GREEN + "!" + Fore.RED + "] " + Fore.WHITE + "Getting the Type of Server... ")
        time.sleep(0.5)
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Server: " + str(server))

        pressAny()

    elif option == 8:

        target = str(input("[+] Target Domain >> "))
        url = f'http://www.{target}/'

        print(Fore.RED + "[" + Fore.GREEN + "!" + Fore.RED + "] " + Fore.WHITE + "Detecting Technologies...")
        #STUPID WARNING XD
        warnings.filterwarnings("ignore", message="""Caught 'unbalanced parenthesis at position 119' compiling regex""", category=UserWarning )

        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)
        technologies = wappalyzer.analyze(webpage)
        for t in technologies:
            time.sleep(0.5)
            print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Technology Detected: {}".format(t))
        
        pressAny()
    
    elif option == 9:
        target = str(input("[+] Phone Target (+12345678901) >> "))
        phone = phonenumbers.parse(target)
        carrier2 = carrier.name_for_number(phone, 'en')
        region = geocoder.description_for_number(phone, 'en')
        possible = phonenumbers.is_possible_number(phone)
        
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Phone Number Validation: " + str(possible))
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "General Information: "+ str(phone))
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Carrier: " + str(carrier2))
        print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Country: " + str(region))

        pressAny()

    elif option == 10:
        print(Fore.RED + "[" + Fore.GREEN + "!" + Fore.RED + "] " + Fore.WHITE + "Exiting")
        sys.exit()

    else:
        print("WTF are you trying dude? Select a number of the menu!")
        
if __name__ == '__main__':
    try:
        while True:
            banner()
            main()
    except:
        print('[!] Stopping the scanner...')
        sys.exit(1)
