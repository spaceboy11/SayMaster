import os
from colorama import Fore
import time
import sys
from subprocess import Popen
def banner():
    if os.name == "nt":
        os.system("cls")
        print("")
        Popen('neofetch -c red -ac green')
        time.sleep(2)
    elif os.name == "posix":
        os.system("clear")
        print("")
        Popen('neofetch')
        time.sleep(2)


def infolist0():
    time.sleep(0.1)
    print(Fore.RED+" ["+Fore.WHITE+"*"+Fore.RED+"]"+Fore.CYAN+" Choose one of the options below \n")
    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX+" [1] Access Webcam \n")
    time.sleep(0.1)
    print(Fore.RED+" [2] Access Microphone\n") 
    time.sleep(0.1)
    print(Fore.GREEN+" [3] Developer :)\n")
    time.sleep(0.1)
    print(Fore.BLUE+" [4] Exit . . .\n")


def infolist1():

    print (Fore.GREEN+" [*]"+Fore.BLUE+"  Develper : Mr Qadir :) \n")
    time.sleep(0.1)
    print (Fore.GREEN+" [*]"+Fore.MAGENTA+"  My Github : github.com/joshkar :)\n")
    time.sleep(0.1)
    print (Fore.GREEN+" [*]"+Fore.CYAN+"  My Telegram ID @ Zerosum0_0 :]\n")
    time.sleep(0.1)
    try:

        input(Fore.LIGHTRED_EX+" [*]  Back To Menu (Press Enter...) ")
    except:
        print("")
        print("\n")
        sys.exit()    
