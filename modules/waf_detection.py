from config.libraries import subprocess


def firewall_detection(target):
    command = f"wafw00f {target}"

    try:
        output = subprocess.check_output(command, shell=True, text=True)
        lines = output.splitlines()
        for line in lines:
            if "The site" in line and "is behind" in line:
                tokens = line.split()
                behind_index = tokens.index("behind")
                if behind_index < len(tokens) - 1:
                    result = " ".join(tokens[behind_index + 1:])
                    print(f"[+] Seems that {target} is using a WAF: {result}")
                    return True
                else:
                    print("[+] Seems that is not using a WAF")
                    return False

    except subprocess.CalledProcessError as e:
        print(f"[*] Something went wrong while trying to detect the firewall: {e}")