#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
# This website is no longer up, do not attempt spamming it #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#


##############################################################
# Site: 'dlscord-egifs.com'                                  #
# Poses as a "free Nitro" website to steal Steam credentials #
##############################################################


import requests
import random
import time
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

def r(length):
    return ''.join(random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm') for i in range (length))

for i in range(2048):
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()
    
    headers = {
        'User-Agent': f'{user_agent}',
    }

    data = {
        'userName': f'{r(815)}@gmail.com',
        'password': f'{r(815)}',
        'url': 'https://dlscord-egifs.com/fromsteamnitro-auth',
        }
    
    try:
        x = requests.post('https://dlscord-egifs.com/check.php', data=data, headers=headers, timeout=5)
        if x.status_code == 403:
            print("[!] 403 FORBIDDEN - Try using a VPN or Proxy [!]")
            exit()
        print(f"\nData:\n{data}\nUser Agent => {user_agent} \n\n=> dlscord-egifs.com")
        print(f"=> {x.status_code}\n=> Response JSON:\n{x.json()}")
        print("[#] Waiting 3 seconds [#]")
    except requests.exceptions.Timeout as e:
        print("=> Request timed out, continuing.")
    except KeyboardInterrupt:
        print("=> ^C Detected - Stopping..")
        exit()
        
