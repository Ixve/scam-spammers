#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
# This website is no longer up, do not attempt spamming it #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#



import requests
import random
import time
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

def r(length):
    return ''.join(random.choice('1234567890') for i in range (length))

for i in range(250):
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()
    
    print("\nGrabbing fake info")
    x = requests.get("https://random-data-api.com/api/users/random_user").json()
    c = x["first_name"]
    v = x["last_name"]
    b = x["phone_number"]
    n = x["address"]["street_address"]
    m = r(2)

    formjson = {"formProperties":{"formName":"Sales lead","formId":"comp-jy49adkl"},"emailConfig":{"sendToEmails":{"emailIds":["cccddc92-b8ff-42f2-ab4d-f0427cc1e765"]}},"viewMode":"Site","fields":[{"fieldId":"comp-jy49afys","label":"First Name","firstName":{"value":f"{c}"}},{"fieldId":"comp-jy49afyx","label":"Last Name","lastName":{"value":f"{v}"}},{"fieldId":"comp-jy49afz1","label":"Email","email":{"value":"{c}{v}{m}@gmail.com","tag":"main"}},{"fieldId":"comp-jy49afz6","label":"Phone","phone":{"value":"{b}","tag":"main"}},{"fieldId":"comp-jy49afza","label":"Address","address":{"value":"{n","tag":"other"}},{"fieldId":"comp-jy49afzf","label":"Company","company":{"value":"31"}}],"labelIds":["contacts-contacted_me","cbbd5247-4703-4501-8e65-2f43e15dd691"]}

    formheaders = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Authorization': '-RUTrMPg-1y7-QQ3KZbLH0w76hMUERj30YFCURlzIbU.eyJpbnN0YW5jZUlkIjoiM2RlNjVjYTMtY2YxMS00MGIwLThmODMtYzM0ZDQzN2RhYTM5IiwiYXBwRGVmSWQiOiIxNGNlMTIxNC1iMjc4LWE3ZTQtMTM3My0wMGNlYmQxYmVmN2MiLCJtZXRhU2l0ZUlkIjoiYzViYjZhM2MtNjlhMS00ZmMxLThkYzMtYjQ2MWM0OGZkYmQwIiwic2lnbkRhdGUiOiIyMDIyLTA3LTE3VDAwOjUwOjA0LjUyMFoiLCJkZW1vTW9kZSI6ZmFsc2UsIm9yaWdpbkluc3RhbmNlSWQiOiI0NjM4YWRhZi0yMzdmLTQwYWMtOWUwNC0zNDdkYzliMDhlZjIiLCJhaWQiOiJlODIxNjRjMy1iMDc2LTRkZmMtOGNjNi05ZTRiNTE4YTA1MjkiLCJiaVRva2VuIjoiZjg1ZDM2OWYtYTZiMC0wZjcxLTAyNDAtNzcyYzg3ZjI3MWU5Iiwic2l0ZU93bmVySWQiOiIzMTQ2YTRhNy03NDlhLTQ4ZWQtODA4My05NTdmZDhhOTY5NzAifQ',
        'Connection': 'keep-alive',
        'Content-Length': '738',
        'Content-Type': 'application/json',
        'Cookie': 'XSRF-TOKEN=1658015846|uFbIiPtCnBAZ; hs=1644363035; bSession=6a5e87ee-b3b2-45b1-b334-60409426a25c|1',
        'DNT': '1',
        'Host': 'hf86nhj54gk86gj.wixsite.com',
        'Origin': 'https://hf86nhj54gk86gj.wixsite.com',
        'Referer': 'https://hf86nhj54gk86gj.wixsite.com/_partials/wix-thunderbolt/dist/clientWorker.0ae124c6.bundle.min.js',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': f'{user_agent}',
        'X-Wix-Client-Artifact-Id': 'wix-form-builder'
        }

    print("Preparing to POST data (Timeout=10)\n")
    try:
        z = requests.post("https://hf86nhj54gk86gj.wixsite.com/_api/wix-forms/v1/submit-form", json=formjson, headers=formheaders, timeout=10)
    except requests.exceptions.ReadTimeout as e:
        print("Request time out, continuing..")
        continue
    print("\nResponse: ")
    print(z.json())
    print(f"{z}\n")

    print("Fake Info Provided: ")
    print(f"{c}\n{v}\n{b}\n{n}\n{m}\n")
    print("Waiting 3 seconds..")
    time.sleep(3)

