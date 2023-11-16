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
    file = open(wordlist,'r')
    lines = file.readlines()

    # Checking The URL
    if 'http' in sys.argv[1] or 'http' in sys.argv[1]:
        pass
    else:
        print("URL Not Defined")
        print("URL Format : https:// OR http://")
        sys.exit()
    def Start_Scan(line):
        # Parsing words from wordlist
        Web_directory = sys.argv[1]+'/'+line
        r = requests.get(Web_directory, headers=header)
        if r.status_code != 404:
            print("[*] STATUS CODE :{:3} | {}".format(r.status_code,Web_directory))
    print("=" * 100)    
    print("[*] SCANNING STARTED")
    print("=" * 100)
    try:
         for line in lines:
            line = line.strip("\n")
            thread = threading.Thread(target=Start_Scan, args=(line,))
            thread.start()
    except:
            print("Error Occured")
    end_time = time.time()
    print("=" * 100)
    print("[*] SCANNING COMPLETE")
    print("[*] TIME TAKEN :", end_time - start_time, "s")
    print("=" * 100)
    sys.exit()


while True:
    if len(sys.argv) == 3:
        print("[*] Mode         : Custom Wordlist")
        print("[*] Target URL   : {}".format(sys.argv[1]))
        print("[*] Wordlist     : {}".format(sys.argv[2]))
        Main(sys.argv[2])
    elif len(sys.argv) == 2:
        print("[*] Mode         : Default Wordlist")
        print("[*] Target URL   : {}".format(sys.argv[1]))
        print("[*] Wordlist     : {}".format("Default_Wordlists/Common.txt"))
        Main("Default_Wordlists/Common.txt")
    else:
        print("Custom Wordlist :")
        print("FORMAT:" + use1)
        print("Default Wordlist :")
        print("FORMAT:" + use2)
        break