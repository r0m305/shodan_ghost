'''
Author: Romeos CyberGypsy
Name: shodan_ghost.py
(c) romeos
Website: https://romeoscybergypsy.pb.online
GitHub: https://github.com/lewiswaigwa
'''

################################
#shodan_ghost
#copying my code won't make you a coder
#seek to understand
################################

import os
import shodan
from colorama import *
from termcolor import *
import sys
import time

class Engine:
    def __init__(self):
        try:
            self.search()

        except KeyboardInterrupt:
            print(colored("Exiting safely...","red"))
            sys.exit()

        except Exception as e:
            print(e)

    def writer(self, file_object, data):
        file_object.write(data)

    def search(self):
        choice = input(f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN}Would you like to save you results to a text file?(Y/n){Fore.BLUE}")
        if choice == "Y" or choice == 'y':
            filename = input(f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN}Enter the name for the text file:{Fore.YELLOW}")
            file = open(filename+".txt","a")

        elif choice == "N" or choice == 'n':
            print(f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN}Continuing without saving...!")

        else:
            print(colored("Invalid choice. Exiting...","red"))
            sys.exit()

        if os.path.exists("api.txt"):
            f = open("api.txt","r")
            api_key = f.read()
            f.close()

        else:
            api_key = input(f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN}Enter your shodan API key:{Fore.YELLOW}")

        query = input(f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN}Enter your search query:{Fore.YELLOW}")
        try:
            api = shodan.Shodan(api_key)
            search_data = api.search(query)
            print(f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN}Matches found: {Fore.RED}{search_data['total']}")
            time.sleep(2)
            f = open("api.txt","w")
            f.write(api_key)
            f.close()

        except Exception as e:
            print(e)

        for finding in search_data['matches']:
            print("\n")
            print(colored("<--"+"*"*30+"-->","yellow"))
            print(f"{Fore.GREEN}IP Address : {Fore.YELLOW}{finding['ip_str']}")
            host = api.host(finding['ip_str'])
            print(f"{Fore.GREEN}Transport : {Fore.YELLOW}{finding['transport']}")
            print(f"{Fore.GREEN}Port : {Fore.YELLOW}{finding['port']}")
            print(f"{Fore.GREEN}Other ports on host: {Fore.YELLOW}{str(host['ports']).strip('[]')}")
            try:
                print(f"{Fore.GREEN}cpe : {Fore.YELLOW}{str(finding['cpe']).strip('[]')}")
            except:
                pass
            print(f"{Fore.GREEN}OS : {Fore.YELLOW}{finding['os']}")
            print(f"{Fore.GREEN}Location : {Fore.YELLOW}{finding['location']}")
            print(f"{Fore.GREEN}Timestamp : {Fore.YELLOW}{finding['timestamp']}")
            print(f"{Fore.GREEN}Organization : {Fore.YELLOW}{finding['org']}")
            try:
                print(f"{Fore.GREEN}Vulnerabilities: {Fore.RED}{str(host['vulns']).strip('[]]')}")

            except:
                pass

            #print(f"{Fore.GREEN}ISP : {Fore.YELLOW}{finding['isp']}")
            print(f"{Fore.GREEN}Data:\n{Fore.YELLOW}{finding['data']}")
            try:
                self.writer(file, "ip address:"+finding['ip_str']+"\nTransport"+finding['transport']+"\nPort:"+str(finding['port'])+"Vulnerabilities:"+str(host['vulns']).strip('[]')+"\nLocation:"+str(finding['location'])+"\ntimestamp:"+finding['timestamp']+"\nOrg:"+finding['org']+"\n"+finding['data'])

            except Exception as e:
                pass



if __name__ == '__main__':
    banner = '''
     ▗▖           ▗▖                    ▗▖
     ▐▌           ▐▌                    ▐▌              ▐▌
▗▟██▖▐▙██▖ ▟█▙  ▟█▟▌ ▟██▖▐▙██▖      ▟█▟▌▐▙██▖ ▟█▙ ▗▟██▖▐███
▐▙▄▖▘▐▛ ▐▌▐▛ ▜▌▐▛ ▜▌ ▘▄▟▌▐▛ ▐▌     ▐▛ ▜▌▐▛ ▐▌▐▛ ▜▌▐▙▄▖▘ ▐▌
 ▀▀█▖▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▗█▀▜▌▐▌ ▐▌     ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌ ▀▀█▖ ▐▌
▐▄▄▟▌▐▌ ▐▌▝█▄█▘▝█▄█▌▐▙▄█▌▐▌ ▐▌     ▝█▄█▌▐▌ ▐▌▝█▄█▘▐▄▄▟▌ ▐▙▄
 ▀▀▀ ▝▘ ▝▘ ▝▀▘  ▝▀▝▘ ▀▀▝▘▝▘ ▝▘      ▞▀▐▌▝▘ ▝▘ ▝▀▘  ▀▀▀   ▀▀
                                    ▜█▛▘                    '''
    print(colored(banner,"green"))
    banner2 = '''
    +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+
    |W|r|i|t|t|e|n| |B|y| |R|o|m|e|o|s| |C|y|b|e|r|G|y|p|s|y|
    +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+'''
    print(colored(banner2,"blue"))
    print(f"{Fore.GREEN}Website: {Fore.BLUE}https://romeoscybergypsy.pb.online")
    obj = Engine()
