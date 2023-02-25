import requests
import time
import os
os.system("mode con cols=136 lines=35")
from bs4 import BeautifulSoup


def sleeep(n):
    time.sleep(0.25)

def m(q):
    for p in q:
        print(p, end='')
        time.sleep(0.005)


print(135*"─")
sleeep(1)
print("""─██████──────────██████─██████████─██████████████─██████████████─
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
sleeep(1)
print(135*"─")
sleeep(1)
m("Created by https://github.com/miceroman")
print("")
sleeep(1)
print(135*"─")

s='██'
for i in range(21):
    time.sleep(0.05)
    print('\r','Loading',i*s,str(5*i),'%',end='')


print("")
sleeep(1)
print(135*"─")

m("Paste the URL to the Steam profile: ")
url_steam = input()

h = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}

d = {
    'name': url_steam
}

r = requests.post('https://faceitfinder.com/profile/', headers=h, data=d)

f_id = ''.join([x for x in r.content.decode() if x.isdigit()])

r_id = requests.get('https://faceitfinder.com/profile/' + f_id, headers=h)
r_s = BeautifulSoup(r_id.content, 'html.parser')
url_steam = r_s.find_all("a", href=True)

try:
    f_url = [x["href"] for x in url_steam if "https://www.faceit.com/" in str(x["href"]) and "csgo" not in str(x["href"])][0]
    f_stats = r_s.find_all("meta")[::-1][0]["content"]

    sleeep(1)
    print(135 * "─")

    sleeep(1)
    m("SteamID: ")
    m(f_id)

    print("")
    print("")

    sleeep(1)
    m("FaceIT URL: ")
    m(f_url)

    print(" ")
    print(" ")

    m(f_stats)

except IndexError:
    print(135 * "─")
    m("The player does not have a FaceIT account")
    print(" ")



sleeep(1)
print("")

sleeep(1)
print(135*"─")

sleeep(1)
print("")
print("")
sleeep(1)

m("Press ENTER to close the window...")

stop = input()