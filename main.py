from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import requests
from bs4 import BeautifulSoup

#function
def faceitfinder(a):

    url_steam=a

    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    }

    data={
        'name':url_steam
    }

    r=requests.post('https://faceitfinder.com/profile/',headers=headers,data=data)

    f_id=''.join([x for x in r.content.decode() if x.isdigit()])

    r_id = requests.get('https://faceitfinder.com/profile/'+f_id,headers=headers)
    r_s = BeautifulSoup(r_id.content,'html.parser')
    url_steam = r_s.find_all("a",href=True)

    try:
        f_url = [x["href"] for x in url_steam if
                "https://www.faceit.com/" in str(x["href"]) and "csgo" not in str(x["href"])][0]
        f_stats=r_s.find_all("meta")[::-1][0]["content"]
        return f_id, f_url, f_stats

    except IndexError:  # if the account was not found
        return "The player does not have a FaceIT account", "The player does not have a FaceIT account","The player does not have a FaceIT account"

#GUI
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x404")
window.configure(bg = "#FFFFFF")
window.title("Find FaceIT account using the Steam profile link v2.0")
window.iconbitmap(r"assets\faceit.ico")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 404,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    407.0,
    206.0,
    image=image_image_1
)

canvas.create_text(
    213.0,
    16.0,
    anchor="nw",
    text="Find FaceIT account using the Steam profile link\n",
    fill="#FFFFFF",
    font=("Griffy Regular", 20 * -1)
)

canvas.create_rectangle(
    173.0,
    44.0,
    626.0,
    45.0,
    fill="#FFFFFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    402.0,
    234.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#000000",
    fg="white",
    highlightthickness=0
)
entry_1.place(
    x=36.0,
    y=222.0,
    width=732.0,
    height=23.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    400.0,
    285.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#000000",
    fg="white",
    highlightthickness=0
)
entry_2.place(
    x=34.0,
    y=273.0,
    width=732.0,
    height=23.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    402.0,
    336.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#000000",
    fg="white",
    highlightthickness=0
)
entry_3.place(
    x=36.0,
    y=324.0,
    width=732.0,
    height=23.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    426.0,
    129.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#CECECE",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=259.0,
    y=120.0,
    width=334.0,
    height=17.0
)

canvas.create_text(
    360.0,
    80.0,
    anchor="nw",
    text="Steam profile link:",
    fill="#FFFFFF",
    font=("Griffy Regular", 17 * -1)
)

canvas.create_text(
    350.0,
    375.0,
    anchor="nw",
    text="Created by mice_roman",
    fill="#FFFFFF",
    font=("Griffy Regular", 12 * -1)
)
canvas.create_text(
    750.0,
    375.0,
    anchor="nw",
    text="v2.0",
    fill="#FFFFFF",
    font=("Griffy Regular", 12 * -1)
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: check(),
    relief="flat"
)
button_1.place(
    x=374.0,
    y=173.0,
    width=99.0,
    height=17.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    188.0,
    30.0,
    image=image_image_2
)

def check():
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")
    entry_3.delete(0, "end")
    f_id, f_url, f_stats = faceitfinder(entry_4.get())
    entry_1.insert(0, "SteamID: "+str(f_id))
    entry_2.insert(0, "FaceIT URL: "+str(f_url))
    entry_3.insert(0, str(f_stats))

window.resizable(False, False)
window.mainloop()
