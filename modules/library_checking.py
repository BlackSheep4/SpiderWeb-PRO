from config.libraries import Fore, Style, init, subprocess, time, os

with open("requirements.txt", "r") as requirements_file:
    library_list = requirements_file.read()
    library_lines = library_list.splitlines()
    libraries_required_list = [line.strip() for line in library_lines]

class LibraryChecker:
    
    def check_required_libraries_installed(self):
        # This function will check for the necessary libraries required to work
        # In case that a library is not installed, a warning will be displayed in the output and added to the log file.

        with open("logs/library_module.log", "w") as library_log_file_deletion:
            for library in libraries_required_list:
                if library == "sys" or "io":
                    pass
                else:
                    command_show = f"pip show {library}"
                    command_check = subprocess.run(command_show, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                    if command_check.returncode == 1:
                        print(Fore.YELLOW + f"[!] The library module {library} is not installed. Try 'pip3 install {library}' or use 'fix' to solve it" + Style.RESET_ALL)
                        library_log_file_deletion.write(f"{library}\n")

    def fix_required_libraries(self):
        # This function will fix and install the necessary libraries required to work
        # If the user uses the reserved word 'fix', SpiderWeb will install the required libraries

        with open("logs/library_module.log", "r") as library_log_file:
            
            file_size = os.path.getsize("logs/library_module.log")

            if file_size == 0:
                print(Fore.GREEN + f"\n[+] All the required library modules are installed" + Style.RESET_ALL)
            else:
                for line in library_log_file:
                    library = line.strip()

                    command_install = f"pip3 install {library}"
                    command_check = subprocess.run(command_install, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                    if command_check.returncode == 0:
                        print(Fore.GREEN + f"[+] The library module {library} has been installed successfully" + Style.RESET_ALL)
                    else:
                        print(Fore.RED + f"[*] Error: The library {library} could not be installed. Check logs and try again" + Style.RESET_ALL)
    
    def check_sudo_privileges(self):
        command_show = "whoami"
        command_check = subprocess.run(command_show, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if command_check.stdout.strip() != "root":
            print(Fore.YELLOW + "[!] Some of the modules requires root permissions for work correctly" + Style.RESET_ALL)
        else:
            pass