
# DirBlast

***A fast Directory Buster tool made for Linux.***
######
*The program supports fast brute force directories and files names on web/application servers due to multithreading.* 

### *Supported OS:*
    LINUX
This program is made and designed for **Linux Opearing System** ***only***.

## Installation

Clone the repository :

```console
kali@kali:~$ git clone https://github.com/Sanjipan/DirBlast
```

Install Python Libraries :
```console
kali@kali:~$ pip install requests
```
## How To Use?

**To *Use the Code*** :
```console
kali@kali:~$ cd DirBlast
kali@kali:~$ python3 ./DirBlast.py <TARGET URL> <FULL PATH OF WORDLIST>
kali@kali:~$ python3 ./DirBlast.py <TARGET URL>
```

## Demo :
```console
┌──(kali㉿kali)-[~]
└─$ cd DirBlast
                                                                                                                         
┌──(kali㉿kali)-[~/DirBlast]
└─$ python3 ./DirBlast.py https://google.com   
====================================================================================================

 ___             ___    _                 _         _.-^^---....,,--       
(  _`\  _       (  _`\ (_ )              ( )_   _--                  --_                                                 
| | ) |(_) _ __ | (_) ) | |    _ _   ___ | ,_) <                        >)                                               
| | | )| |( '__)|  _ <' | |  /'_` )/',__)| |   |                         |                                               
| |_) || || |   | (_) ) | | ( (_| |\__, \| |_   \._                   _./                                                
(____/'(_)(_)   (____/'(___)`\__,_)(____/`\__)     ```--. . , ; .--'''                                                   
                                                         | |   |                                                         
                                                      .-=||  | |=-.                                                      
                                                      `-=#$%&%$#=-'                                                      
                                                         | ;  :|                                                         
                                                _____.,-#%&$@%#&#~,._____                                                
[*] Mode         : Default Wordlist
[*] Target URL   : https://google.com
[*] Wordlist     : Default_Wordlists/Common.txt
====================================================================================================
[*] SCANNING STARTED
====================================================================================================
[*] STATUS CODE :200 | https://google.com/
[*] STATUS CODE :200 | https://google.com/2002
[*] STATUS CODE :200 | https://google.com/2001
[*] STATUS CODE :200 | https://google.com/2007
[*] STATUS CODE :200 | https://google.com/2003
[*] STATUS CODE :200 | https://google.com/2005
[*] STATUS CODE :200 | https://google.com/2004
[*] STATUS CODE :200 | https://google.com/2008
[*] STATUS CODE :200 | https://google.com/2006
[*] STATUS CODE :200 | https://google.com/2009
====================================================================================================
[*] SCANNING COMPLETE
[*] TIME TAKEN : 14.638089895248413 s
====================================================================================================
```

## Authors :

- [@Sanjipan Deb](https://github.com/Sanjipan)

## **Disclaimer**
**"EDUCATIONAL PURPOSES ONLY"**
######
## Legal Disclaimer
The use of code contained in this repository, either in part or in its totality,
for engaging targets without prior mutual consent is illegal. **It is
the end user's responsibility to obey all applicable local, state and
federal laws.**

Developers assume **no liability** and are not
responsible for misuses or damages caused by any code contained
in this repository in any event that, accidentally or otherwise, it comes to
be utilized by a threat agent or unauthorized entity as a means to compromise
the security, privacy, confidentiality, integrity, and/or availability of
systems and their associated resources. In this context the term "compromise" is
henceforth understood as the leverage of exploitation of known or unknown vulnerabilities
present in said systems, including, but not limited to, the implementation of
security controls, human- or electronically-enabled.

The use of this code is **only** endorsed by the developers in those
circumstances directly related to **educational environments** or
**authorized penetration testing engagements** whose declared purpose is that
of finding and mitigating vulnerabilities in systems, limiting their exposure
to compromises and exploits employed by malicious agents as defined in their
respective threat models.
######
The application must be used for **"EDUCATIONAL PURPOSES ONLY"**

### *Contect Us On:*
###### **SANJIPAN DEB** :
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sanjipan-deb-834601220/)