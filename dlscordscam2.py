#########################################################################
# Site: 'dlscordjbost.com' (Only accessible from 'dlscordjbost.com/csi' #
# Poses as a "free Nitro" website to steal Steam credentials            #
#########################################################################

import requests
import random
import time
from colorama import init, Fore
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

init()
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
user_agent = user_agent_rotator.get_random_user_agent()

def x(length):
    return ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM') for i in range (length))

for i in range(251):
    headers = { "Host": "dlscordjbost.com", "User-Agent": f"{user_agent}", "Content-Length": "19", "Origin": "https://dlscordjbost.com", "DNT": "1", "Connection": "keep-alive", "Cookie": "timezoneOffset=3600,0", }
    data = {
        "userName": f"{x(625)}",
        "password": f"{x(625)}",
        "url": "https://dlscordjbost.com/csi-auth",
        }

    print(f"\n{Fore.WHITE}Generated Data:\n{data}\n")
    time.sleep(0.1)
    try:
        r = requests.post("https://dlscordjbost.com/check.php", data=data, headers=headers, timeout=10)
        if r.status_code == 200:
            print(f"{Fore.GREEN}[+] POST Request Successful ({i}/250)\nResponse: {Fore.YELLOW}{r.json()} {Fore.WHITE}")
        else:
            print(f"{Fore.RED}[-] POST Request Unsuccessful{Fore.WHITE}, Response:\n{r.json()}\nStatus Code: {r.status_code}\n\nExitting program, goodbye")
            exit()
    except requests.exceptions.JSONDecodeError:
        print(f"{Fore.RED}[-] POST Request Unsuccessful: JSONDecodeError\n[!] Exitting program, goodbye")
        exit()
    except requests.exceptions.ReadTimeout:
        print(f"{Fore.BLUE}[i] {Fore.WHITE}POST Request Timed Out... Continuing.")
        continue
