#!/bin/python3

import requests
import sys
import threading
import time

use1 = "python3 DirBlast.py <TARGET URL> <FULL PATH OF WORDLIST>"
use2 = "python3 DirBlast.py <TARGET URL>"

def Main(wordlist):
    start_time = time.time()
    
    # Request Headers
    header = {
        'User-Agent':'Macintosh Mac OS X' 
    }

    # Loding Wordlist
    file = open(wordlist,'r',encoding="ISO-8859-1")
    lines = file.readlines()

    # Checking The URL
    if 'http' in sys.argv[1] or 'http' in sys.argv[1]:
        pass
    else:
        print("\x1b[31m[*] URL Not Defined\x1b[0m")
        print("\x1b[34m[*] URL Format : https:// OR http:// \x1b[0m")
        sys.exit()
    def Start_Scan(line):
        # Parsing words from wordlist
        Web_directory = sys.argv[1]+'/'+line
        r = requests.get(Web_directory, headers=header)
        if r.status_code != 404:
            print("\x1b[32m[*] STATUS CODE :{:3} | {}\x1b[0m".format(r.status_code,Web_directory))
    print("=" * 100)    
    print("\x1b[32m[*] SCANNING STARTED\x1b[0m")
    print("=" * 100)
    try:
         for line in lines:
            line = line.strip("\n")
            thread = threading.Thread(target=Start_Scan, args=(line,))
            thread.start()
            time.sleep(0.05)
    except:
            print("\x1b[31m[*] Error Occured\x1b[0m")
    end_time = time.time()
    print("=" * 100)
    print("\x1b[34m[*] SCANNING COMPLETE\x1b[0m")
    print("\x1b[34m[*] TIME TAKEN :\x1b[0m", end_time - start_time, "s")
    print("=" * 100)
    sys.exit()

print("=" * 100)
print()
print("\x1b[1m\x1b[37m ___             ___    _                 _         _.-^^---....,,--       ")
print("(  _`\  _       (  _`\ (_ )              ( )_   _--                  --_  ")
print("| | ) |(_) _ __ | (_) ) | |    _ _   ___ | ,_) <                        >)")
print("| | | )| |( '__)|  _ <' | |  /'_` )/',__)| |   |                         | ")
print("| |_) || || |   | (_) ) | | ( (_| |\__, \| |_   \._                   _./  ")
print("(____/'(_)(_)   (____/'(___)`\__,_)(____/`\__)     ```--. . , ; .--'''       ")
print("                                                         | |   |     ")        
print("                                                      .-=||  | |=-.  ") 
print("                                                      `-=#$%&%$#=-'  ") 
print("                                                         | ;  :|     ")
print("                                                _____.,-#%&$@%#&#~,._____ \x1b[0m")

while True:
    if len(sys.argv) == 3:
        print("\x1b[34m[*] Mode         : Custom Wordlist\x1b[0m")
        print("\x1b[34m[*] Target URL   : \x1b[0m{}".format(sys.argv[1]))
        print("\x1b[34m[*] Wordlist     : \x1b[0m{}".format(sys.argv[2]))
        Main(sys.argv[2])
    elif len(sys.argv) == 2:
        print("\x1b[34m[*] Mode         : Default Wordlist\x1b[0m")
        print("\x1b[34m[*] Target URL   : \x1b[0m{}".format(sys.argv[1]))
        print("\x1b[34m[*] Wordlist     : \x1b[0m{}".format("Default_Wordlists/Common.txt"))
        Main("Default_Wordlists/Common.txt")
    else:
        print()
        print("\x1b[34m[*] Custom Wordlist :\x1b[0m")
        print("\x1b[34m[*] FORMAT:\x1b[0m " + use1)
        print()
        print("\x1b[34m[*] Default Wordlist :\x1b[0m")
        print("\x1b[34m[*] FORMAT:\x1b[0m " + use2)
        print("=" * 100)
        break