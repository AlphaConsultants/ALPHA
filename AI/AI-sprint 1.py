from tkinter import *
import requests

github_example = "https://raw.githubusercontent.com/AlphaConsultants/ALPHA/main/AI/textdocumenttest.json"
json_data = requests.get(github_example).json()


games_list = []

for data in json_data:
    rating_in_percentage = ((data["positive_ratings"] - data["negative_ratings"]) / data["positive_ratings"]) * 100
    rating_in_percentage_afgerond = str(round(rating_in_percentage, 1))
    data_per_game = data["appid"], data["name"], data["genres"], data["release_date"], data["price"], data["owners"], rating_in_percentage_afgerond, data["required_age"], "\n"
    games_list.append(tuple(data_per_game))

print(games_list)


def toon_spellen():
    data_box.delete(0, "end")
    data_box.pack()
    positie = 0
    for games in games_list:
        for game in games:
            positie += 1
            data_box.insert(positie, game)


def toon_eerste_spel():
    data_box.delete(0, "end")
    data_box.pack()
    eersteSpel = games_list[0][1]
    data_box.insert(1, eersteSpel)

root = Tk()
root.title("Dashboard Steam")
root.geometry("1800x1000")
root.configure(bg="#17202e")


'''Frames voor widgets'''
DataFrame = Frame(root, bg="#17202e")
SorteerButtonFrame = Frame(root, bg="#17202e")
LinkerFrame = Frame(SorteerButtonFrame, bg="#17202e")
RechterFrame = Frame(SorteerButtonFrame, bg="#17202e")
eerste_spel_frame = Frame(root, bg="#17202e")


'''Titel van dashboard'''
titel = Label(root, text="Alpha Consultants", bg="#17202e", fg="white", font=("Calibri", 40, "bold", "underline"))
titel.pack(pady=90)

DataFrame.place(x=100, y=400)
SorteerButtonFrame.pack(side=RIGHT)
LinkerFrame.pack(side=LEFT, pady=55, padx=30)
RechterFrame.pack(side=RIGHT, pady=55, padx=30)


'''Sorteerknoppen met titel'''
SorteerTitel = Label(SorteerButtonFrame, text="Sorteren op:", bg="#17202e", fg="white", font=("Calibri", 24, "bold"))
ToonAlleGames = Button(RechterFrame, text="Toon Games", width=24, font=("Calibri", 14, "bold"), command=toon_spellen)
Eerste_Spel = Button(LinkerFrame, text="Eerste Spel", width=24, font=("Calibri", 14, "bold"), command=toon_eerste_spel)
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
Eerste_Spel.pack(pady=10)
ToonAlleGames.pack(pady=10)
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


'''Scrollbar'''
sb = Scrollbar(DataFrame)
sb.pack(side=RIGHT, fill=Y)


'''Data'''
data_box = Listbox(DataFrame, width=100, height=18, yscrollcommand=sb.set, font=("Calibri", 14, "bold"))
sb.config(command=data_box.yview)


# Naam = Label(DataFrame, text="Naam", bg="yellow", fg="black", width=12, font=("Calibri", 16, "bold"))
# Genre = Label(DataFrame, text="Genre", bg="yellow", fg="black", width=12, font=("Calibri", 16, "bold"))
# ReleaseDate = Label(DataFrame, text="Release date", bg="yellow", fg="black", width=12, font=("Calibri", 16, "bold"))
# Price = Label(DataFrame, text="Price in $", bg="yellow", fg="black", width=12, font=("Calibri", 16, "bold"))
# Owners = Label(DataFrame, text="Owners", bg="yellow", fg="black", width=12, font=("Calibri", 16, "bold"))
# Rating = Label(DataFrame, text="Rating in %", bg="yellow", fg="black", width=12, font=("Calibri", 16, "bold"))
# RequiredAge = Label(DataFrame, text="Legal age", bg="yellow", fg="black", width=12, font=("Calibri", 16, "bold"))
#
# Naam.grid(row=0, column=0, pady=5)
# Genre.grid(row=1, column=0, pady=5)
# ReleaseDate.grid(row=2, column=0, pady=5)
# Price.grid(row=3, column=0, pady=5)
# Owners.grid(row=4, column=0, pady=5)
# Rating.grid(row=5, column=0, pady=5)
# RequiredAge.grid(row=6, column=0, pady=5)


toon_spellen()
root.mainloop()
