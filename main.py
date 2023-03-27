import requests
import time
import os
os.system("mode con cols=136 lines=35")
from bs4 import BeautifulSoup


def strip(q):           #strip
    print(135 * "─")

def loading(q):         #beautiful loading
    for i in range(21):
        time.sleep(0.05)
        print('\r','Loading',i * s,str(5 * i),'%',end='')
    print("")

def sleep(q):           #time sleep
    time.sleep(0.25)

def logo(q):            #my logo
    print("""    ─██████──────────██████─██████████─██████████████─██████████████─
    ─██░░██████████████░░██─██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
    ─██░░░░░░░░░░░░░░░░░░██─████░░████─██░░██████████─██░░██████████─
    ─██░░██████░░██████░░██───██░░██───██░░██─────────██░░██─────────
    ─██░░██──██░░██──██░░██───██░░██───██░░██─────────██░░██████████─
    ─██░░██──██░░██──██░░██───██░░██───██░░██─────────██░░░░░░░░░░██─
    ─██░░██──██████──██░░██───██░░██───██░░██─────────██░░██████████─
    ─██░░██──────────██░░██───██░░██───██░░██─────────██░░██─────────
    ─██░░██──────────██░░██─████░░████─██░░██████████─██░░██████████─
    ─██░░██──────────██░░██─██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
    ─██████──────────██████─██████████─██████████████─██████████████─""")


strip('')

logo('')

strip('')

sleep('')
print("Created by https://github.com/miceroman")

strip('')

s='██'

loading('')

flag = str()

while flag != 'N':
    strip('')
    print("Paste the URL to the Steam profile: ")
    url_steam = input()

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    }

    data = {
        'name':url_steam
    }

    r = requests.post('https://faceitfinder.com/profile/',headers=headers,data=data)

    f_id = ''.join([x for x in r.content.decode() if x.isdigit()])

    r_id = requests.get('https://faceitfinder.com/profile/'+f_id,headers=headers)
    r_s = BeautifulSoup(r_id.content, 'html.parser')
    url_steam = r_s.find_all("a", href=True)

    try:
        f_url = [x["href"] for x in url_steam if "https://www.faceit.com/" in str(x["href"]) and "csgo" not in str(x["href"])][0]
        f_stats = r_s.find_all("meta")[::-1][0]["content"]

        strip('')

        print("SteamID: " + str(f_id) + '\n')
        sleep('')

        print("FaceIT URL: " + str(f_url) + '\n')
        sleep('')

        print(str(f_stats))
        sleep('')

    except IndexError:                 #if the account was not found
        strip('')
        sleep('')
        print("The player does not have a FaceIT account")
        sleep('')

    strip('')

    print("To explore another account, press ENTER")
    sleep('')

    print("To close the application, print N")
    sleep('')

    flag = input()
