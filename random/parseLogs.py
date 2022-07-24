from time import time
import requests
import re

url = "http://bholt.org/ssh/short.txt"
INVALID_USER = "Invalid user"
INCORRECT_PASSWORD = "Failed password"
regex = r"((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])[ (\[]?(\.|dot)[ )\]]?){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))"


def parse_logs_login_errors(url):

    # handle the case where url is invalid/not string

    # compile regex for IP Address
    compiled = re.compile(regex)
    # 8.8.8.8
    ip_map = {}
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("Invalid URL", url)
    
    text = r.text #  Double check

    # KMP 
    for line in text.split('\n'):
        if INVALID_USER in line or INCORRECT_PASSWORD in line:
            output = re.findall(compiled, line)
            if len(output) >= 1:
                ip_map[output[0][0]] = ip_map.get(output[0][0],0) + 1 # in loop

    print("IP, Failed_attempts")
    for k, v in sorted(ip_map.items(), key=lambda item: item[1],reverse=True):
        print(k, v)


parse_logs_login_errors(url)


# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    

