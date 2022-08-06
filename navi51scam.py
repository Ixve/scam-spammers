###########################################
# Site: https://navi51.com/               #
# Fake "Natus Vincere Sponsored Giveaway" #
# Steals Steam login credentials          #
###########################################

import requests
import random

def x(length):
    return ''.join(random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm') for i in range (length))

for i in range(128):
    try:
        data = {
            "code": "",
            "password": f"{x(12)}",
            "username": f"synthwashere_{x(4)}@gmail.com", }
        
        r = requests.post("https://navi51.com/auth/login", json=data, timeout=5)
        print(f"Timeout: 5s\n\nSent Data: {data}\n\nStatus Code:\n{r.status_code}\n\nReturned JSON:\n{r.json()}")
    except requests.exceptions.ReadTimeout as e:
        print(f"Read time out, error:\n\n{e}")
        print("\nAttempting to continue..")
        continue
    except r.status_code == 403:
        print("IP banned, switch IPs or use a VPN/Proxy")
        exit()
