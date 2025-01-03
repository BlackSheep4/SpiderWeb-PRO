def banner_grabbing(self):
    
        try:
            target = f"https://{self.target}"
            print(target)
            r = requests.get(target)
            print(r.headers)
            server = r.headers['Server']
            print(Fore.RED + "[" + Fore.GREEN + "!" + Fore.RED + "] " + Fore.WHITE + "Getting the Type of Server... ")
            
            print(Fore.RED + "[" + Fore.GREEN + "+" + Fore.RED + "] " + Fore.WHITE + "Server: " + str(server))

            input('\n' + "Press any key to continue...")
            
        
        except Exception as e:
            print("Error:", e)