from tkinter import *
import requests

file = open("github_voorbeeld", "r+")

github_example = "https://raw.githubusercontent.com/AlphaConsultants/ALPHA/main/AI/textdocumenttest.json"
json_data = requests.get(github_example).json()
file.write(str(json_data))


def toon_eerste_spel():
    eerste_spel_frame.pack(side=LEFT)
    for games in json_data:
        if games["appid"] < 20:
            eerste_spel = games["name"], "\n", games["release_date"], "\n", games["price"]
            spel_label = Label(eerste_spel_frame, text=eerste_spel, bg="red", fg="white", font=("Calibri", 18, "bold"))
            spel_label.pack(padx=200, pady=20)


root = Tk()
root.title("Dashboard Steam")
root.geometry("1800x1000")
root.configure(bg="#17202e")
SorteerFrame = Frame(root, bg="#17202e")
LinkerFrame = Frame(SorteerFrame, bg="#17202e")
RechterFrame = Frame(SorteerFrame, bg="#17202e")
eerste_spel_frame = Frame(root, bg="#17202e")

titel = Label(root, text="Dashboard Steam", bg="#17202e", fg="white", font=("Calibri", 40, "bold", "underline"))
titel.pack(pady=90)

SorteerFrame.pack(side=RIGHT)
LinkerFrame.pack(side=RIGHT, pady=55, padx=30)
RechterFrame.pack(side=RIGHT, pady=55, padx=30)


SorteerTitel = Label(SorteerFrame, text="Sorteren op:", bg="#17202e", fg="white", font=("Calibri", 24, "bold"))
Name_AZ = Button(LinkerFrame, text="Naam (A-Z)", width=24, font=("Calibri", 14, "bold"))
Name_ZA = Button(RechterFrame, text="Naam (Z-A)", width=24, font=("Calibri", 14, "bold"))
Genre_AZ = Button(LinkerFrame, text="Genre (A-Z)", width=24, font=("Calibri", 14, "bold"))
Genre_ZA = Button(RechterFrame, text="Genre (Z-A)", width=24, font=("Calibri", 14, "bold"))
ReleaseDate_ON = Button(LinkerFrame, text="Releasedatum (oud-nieuw)", width=24, font=("Calibri", 14, "bold"))
ReleaseDate_NO = Button(RechterFrame, text="Releasedatum (nieuw-oud)", width=24, font=("Calibri", 14, "bold"))
Price_LH = Button(LinkerFrame, text="Prijs (laag-hoog)", width=24, font=("Calibri", 14, "bold"))
Price_HL = Button(RechterFrame, text="Prijs (hoog-laag)", width=24, font=("Calibri", 14, "bold"))
Owners_LH = Button(LinkerFrame, text="Owners (laag-hoog)", width=24, font=("Calibri", 14, "bold"))
Owners_HL = Button(RechterFrame, text="Owners (hoog-laag)", width=24, font=("Calibri", 14, "bold"))
Rating_LH = Button(LinkerFrame, text="Rating (laag-hoog)", width=24, font=("Calibri", 14, "bold"))
Rating_HL = Button(RechterFrame, text="Rating (hoog-laag)", width=24, font=("Calibri", 14, "bold"))
RequiredAge_LH = Button(LinkerFrame, text="Required Age (laag-hoog)", width=24, font=("Calibri", 14, "bold"))
RequiredAge_HL = Button(RechterFrame, text="Required Age (hoog-laag)", width=24, font=("Calibri", 14, "bold"))

SorteerTitel.place(x=30, y=10)
Name_AZ.pack(pady=10)
Name_ZA.pack(pady=10)
Genre_AZ.pack(pady=10)
Genre_ZA.pack(pady=10)
ReleaseDate_ON.pack(pady=10)
ReleaseDate_NO.pack(pady=10)
Price_LH.pack(pady=10)
Price_HL.pack(pady=10)
Owners_LH.pack(pady=10)
Owners_HL.pack(pady=10)
Rating_LH.pack(pady=10)
Rating_HL.pack(pady=10)
RequiredAge_LH.pack(pady=10)
RequiredAge_HL.pack(pady=10)

toon_eerste_spel()
root.mainloop()
