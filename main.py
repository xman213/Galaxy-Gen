import requests
import os
import re
import io
import sys
import time
import json
import shutil
import ctypes
import random
import zipfile
import requests
import threading
import subprocess
import pylibcheck
import pystyle 
from pystyle import *
from urllib.request import urlopen, urlretrieve
from distutils.version import LooseVersion
from bs4 import BeautifulSoup
from colorama import Fore
from time import sleep
import random
from random import choice
import string
import pypresence

try:
    rpc = pypresence.Presence(961018439475023964)
    rpc.connect()
    start_time = time.time()
    rpc.update(large_image="logo",large_text="Galaxy Gen", details="Generating Nitro Codes",
               state='v0.1 ', start=start_time)
except Exception as e:
    pass 








def getTempDir():
        system = os.name
        if system == 'nt':
            #if its windows
            return os.getenv('temp')
        elif system == 'posix':
            #if its linux
            return '/tmp/'


def setTitle(_str):
    system = os.name
    if system == 'nt':
        #if its windows
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}")
    elif system == 'posix':
        #if its linux
        sys.stdout.write(f"\x1b]0;{_str}\x07")
    else:
        #if its something else or some err happend for some reason, we do nothing
        pass


class proxies():
    


    






    def proxy():
        temp = getTempDir()+"\\proxys.txt"
        #if the file size is empty
        if os.stat(temp).st_size == 0:
            proxy_scrape()
        proxies = open(temp).read().split('\n')
        proxy = proxies[0]

        with open(temp, 'r+') as fp:
            #read all lines
            lines = fp.readlines()
            #get the first line
            fp.seek(0)
            #remove the proxy
            fp.truncate()
            fp.writelines(lines[1:])
        return ({'http://': f'http://{proxy}', 'https://': f'https://{proxy}'})

    #headers for optimazation
    heads = [
        {
            "Content-Type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
        },

        {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
        },

        {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
        },

        {
            "Content-Type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
        },

        {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
        },

        {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
    ]

    def getheaders(token=None):
        headers = random.choice(heads)
        if token:
            headers.update({"Authorization": token})
        return headers





    def proxy_scrape(): 
        proxieslog = []
        setTitle("Scraping Proxies | Galaxy Gen | Codes Checked: 0")
        #start timer
        startTime = time.time()
        #create temp dir
        temp = getTempDir()+"\\proxys.txt"
        print(f"{Fore.MAGENTA}Ima Scrape Proxys For Yo{Fore.RESET} Bitch {Fore.MAGENTA}Ass")

        def fetchProxies(url, custom_regex):
            global proxylist
            try:
                proxylist = requests.get(url, timeout=5).text
            except Exception:
                pass
            finally:
                proxylist = proxylist.replace('null', '')
            #get the proxies from all the sites with the custom regex
            custom_regex = custom_regex.replace('%ip%', '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')
            custom_regex = custom_regex.replace('%port%', '([0-9]{1,5})')
            for proxy in re.findall(re.compile(custom_regex), proxylist):
                proxieslog.append(f"{proxy[0]}:{proxy[1]}")

        #all urls
        proxysources = [
            ["https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt", "%ip%:%port%"],
            ["https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt", "%ip%:%port%"],
            ["https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt", "%ip%:%port%"],
            ["http://spys.me/proxy.txt","%ip%:%port% "],
            ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"],
            ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","],
            ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
            ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt", '%ip%:%port% (.*?){2}-.-S \\+'],
            ["https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt", '%ip%", "type": "http", "port": %port%'],
            ["https://www.us-proxy.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
            ["https://free-proxy-list.net/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
            ["https://www.sslproxies.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
            ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all", "%ip%:%port%"],
            ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt", "%ip%:%port%"],
            ["https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt", "%ip%:%port%"],
            ["https://proxylist.icu/proxy/", "<td>%ip%:%port%</td><td>http<"],
            ["https://proxylist.icu/proxy/1", "<td>%ip%:%port%</td><td>http<"],
            ["https://proxylist.icu/proxy/2", "<td>%ip%:%port%</td><td>http<"],
            ["https://proxylist.icu/proxy/3", "<td>%ip%:%port%</td><td>http<"],
            ["https://proxylist.icu/proxy/4", "<td>%ip%:%port%</td><td>http<"],
            ["https://proxylist.icu/proxy/5", "<td>%ip%:%port%</td><td>http<"],
            ["https://www.hide-my-ip.com/proxylist.shtml", '"i":"%ip%","p":"%port%",'],
            ["https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json", '"ip": "%ip%",\n.*?"port": "%port%",'],
           
        ]
        threads = [] 
        for url in proxysources:
            #send them out in threads
            t = threading.Thread(target=fetchProxies, args=(url[0], url[1]))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

        proxies = list(set(proxieslog))
        with open(temp, "w") as f:
            for proxy in proxies:
                #create the same proxy 7-10 times to avoid ratelimit when using other options
                for i in range(random.randint(7, 10)):
                    f.write(f"{proxy}\n")
        #get the time it took to scrape
        execution_time = (time.time() - startTime)
        print(f"{Fore.MAGENTA}Scraped{Fore.RESET}{len(proxies):>5} {Fore.MAGENTA}Proxys in{Fore.RESET} {execution_time}ms")
        time.sleep(2)
        os.system('cls')
temp = getTempDir()+"\\proxys.txt"    
proxies.proxy_scrape()
r = requests.get(' https://raw.githubusercontent.com/xman213/proxies/main/prox.txt').text













codes = 0
setTitle("Galaxy Gen | Codes Checked: 0")
def gen():
        global codes
        while True:
            with open(temp, "r") as f:
                                proxy1 = choice(f.readlines()).strip()
                                proxies = {'https': f'http://{proxy1}'}
                                

            code = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))

            try:
                r = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true',proxies=proxies)
                if r.status_code == 200:
                    codes += 1
                    print( f'{Fore.MAGENTA}[Galaxy Gen]{Fore.RESET} Valid Code! |{Fore.MAGENTA} discord.gift/{code}{Fore.RESET} ')
                    setTitle("Galaxy Gen | Codes Checked: "+str(codes))
                    os.system('pause > NUL') 
                if r.status_code == 429:
                        print( f'{Fore.MAGENTA}[Galaxy Gen]{Fore.RESET} Rate Limited! | {Fore.MAGENTA}Ratelimited on{Fore.RESET} {proxy1}')
                
                  
            except  Exception as e:
            
              pass


threads = 1000000
for i in range(threads):
    threading.Thread(target=gen).start()
