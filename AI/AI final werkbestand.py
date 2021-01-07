from tkinter import *
import requests

github_example = "https://raw.githubusercontent.com/AlphaConsultants/ALPHA/main/AI/textdocumenttest.json"

json_data = requests.get(github_example).json()

games_list = []

def sorteren(keuze):
    '''Sorteren op:
    -   keuze 0 = Naam A-Z
    -   keuze 1 = Naam Z-A
    -   keuze 2 = Genre A-Z
    -   keuze 3 = Genre Z-A
    -   keuze 4 = Releasedatum Oud - Nieuw
    -   keuze 5 = Releasedatum Nieuw - Oud
    -   keuze 6 = Prijs Laag - Hoog
    -   keuze 7 = Prijs Hoog - Laag
    -   keuze 8 = Owners Laag - Hoog
    -   keuze 9 = Owners Hoog - Laag
    -   keuze 10 = Rating Laag - Hoog
    -   keuze 11 = Rating Hoog - Laag'''

    n = len(games_list)
    if keuze == 0:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][0] > games_list[g+1][0]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list
    elif keuze == 1:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][0] < games_list[g+1][0]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list
    elif keuze == 2:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][1] > games_list[g+1][1]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list
    elif keuze == 3:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][1] < games_list[g+1][1]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list
    elif keuze == 4:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][2] > games_list[g+1][2]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list
    elif keuze == 5:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][2] < games_list[g+1][2]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list
    elif keuze == 6:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][3] > games_list[g+1][3]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list
    elif keuze == 7:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][3] < games_list[g+1][3]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list
    elif keuze == 8:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][4] > games_list[g+1][4]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list
    elif keuze == 9:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][4] < games_list[g+1][4]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list
    elif keuze == 10:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][5] > games_list[g+1][5]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list
    elif keuze == 11:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][5] < games_list[g+1][5]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list


def datascherm1_tonen():
    Hoofdscherm.pack_forget()
    Datascherm2.pack_forget()
    TerugknopFrame.pack_forget()
    TerugknopFrame.pack(pady=20)
    Datascherm.pack()
    Datascherm1.pack()
    Terug.pack()


def datascherm2_tonen():
    Hoofdscherm.pack_forget()
    TerugknopFrame.pack_forget()
    Datascherm1.pack_forget()
    TerugknopFrame.pack(pady=20)
    Datascherm.pack()
    Datascherm2.pack()
    Terug.pack()


def hoofdscherm_tonen():
    Datascherm.pack_forget()
    TerugknopFrame.pack_forget()
    Hoofdscherm.pack()


def data_opvragen():
    games_list.clear()
    for data in json_data:
        rating_in_percentage = ((data["positive_ratings"] - data["negative_ratings"]) / data["positive_ratings"]) * 100
        rating_in_percentage_afgerond = str(round(rating_in_percentage, 1))
        data_per_game = data["name"], data["genres"], data["release_date"], data["price"], data[
            "owners"], rating_in_percentage_afgerond
        games_list.append(tuple(data_per_game))


def informatie_tonen():
    datascherm1_tonen()
    total_rows = len(games_list)
    total_columns = len(games_list[0])
    for games in range(total_rows):
        for game in range(total_columns):
            e = Entry(Datascherm1, fg='blue', font=('Arial', 12, 'bold'))
            e.grid(row=games, column=game)
            e.insert(END, games_list[games][game])


def toon_spellen():
    data_opvragen()
    informatie_tonen()


def toon_eerste_spel():
    data_opvragen()
    datascherm2_tonen()
    a = games_list[0][0]
    e = Entry(Datascherm2, fg='blue', font=('Arial', 12, 'bold'))
    e.grid(row=0, column=0)
    e.insert(END, a)


def toon_naam_az():
    data_opvragen()
    sorteren(0)
    informatie_tonen()


def toon_naam_za():
    data_opvragen()
    sorteren(1)
    informatie_tonen()


def toon_genre_az():
    data_opvragen()
    sorteren(2)
    informatie_tonen()


def toon_genre_za():
    data_opvragen()
    sorteren(3)
    informatie_tonen()


def toon_release_date_on():
    data_opvragen()
    sorteren(4)
    informatie_tonen()


def toon_release_date_no():
    data_opvragen()
    sorteren(5)
    informatie_tonen()


def toon_prijs_lh():
    data_opvragen()
    sorteren(6)
    informatie_tonen()


def toon_prijs_hl():
    data_opvragen()
    sorteren(7)
    informatie_tonen()


def toon_owners_hl():
    data_opvragen()
    sorteren(8)
    informatie_tonen()


def toon_owners_lh():
    data_opvragen()
    sorteren(9)
    informatie_tonen()


def toon_rating_lh():
    data_opvragen()
    sorteren(10)
    informatie_tonen()


def toon_rating_hl():
    data_opvragen()
    sorteren(11)
    informatie_tonen()


root = Tk()
root.title("Dashboard Steam")
root.geometry("1500x1000")
root.configure(bg="#17202e")


Hoofdscherm = Frame(root)
Datascherm = Frame(root)
TerugknopFrame = Frame(root)
Datascherm1 = Frame(Datascherm)
Datascherm2 = Frame(Datascherm)


'''Titel van dashboard'''
titel = Label(root, text="Alpha Consultants", bg="#17202e", fg="white", font=("Calibri", 40, "bold", "underline"))
titel.pack(pady=90)


'''Frames voor widgets'''
SorteerButtonFrame = Frame(Hoofdscherm, bg="#17202e")
LinkerFrame = Frame(SorteerButtonFrame, bg="#17202e")
RechterFrame = Frame(SorteerButtonFrame, bg="#17202e")


Hoofdscherm.pack()
SorteerButtonFrame.pack(side=RIGHT)
LinkerFrame.pack(side=LEFT, pady=55, padx=30)
RechterFrame.pack(side=RIGHT, pady=55, padx=30)


'''Sorteerknoppen met titel op hoofdscherm'''
SorteerTitel = Label(SorteerButtonFrame, text="Sorteren op:", bg="#17202e", fg="white", font=("Calibri", 24, "bold"))
ToonAlleGames = Button(RechterFrame, text="Toon Games", width=24, font=("Calibri", 14, "bold"), command=toon_spellen)
Eerste_Spel = Button(LinkerFrame, text="Eerste Spel", width=24, font=("Calibri", 14, "bold"), command=toon_eerste_spel)
Name_AZ = Button(LinkerFrame, text="Naam (A-Z)", width=24, font=("Calibri", 14, "bold"), command=toon_naam_az)
Name_ZA = Button(RechterFrame, text="Naam (Z-A)", width=24, font=("Calibri", 14, "bold"), command=toon_naam_za)
Genre_AZ = Button(LinkerFrame, text="Genre (A-Z)", width=24, font=("Calibri", 14, "bold"), command=toon_genre_az)
Genre_ZA = Button(RechterFrame, text="Genre (Z-A)", width=24, font=("Calibri", 14, "bold"), command=toon_genre_za)
ReleaseDate_ON = Button(LinkerFrame, text="Releasedatum (oud-nieuw)", width=24, font=("Calibri", 14, "bold"),
                        command=toon_release_date_on)
ReleaseDate_NO = Button(RechterFrame, text="Releasedatum (nieuw-oud)", width=24, font=("Calibri", 14, "bold"),
                        command=toon_release_date_no)
Price_LH = Button(LinkerFrame, text="Prijs (laag-hoog)", width=24, font=("Calibri", 14, "bold"), command=toon_prijs_lh)
Price_HL = Button(RechterFrame, text="Prijs (hoog-laag)", width=24, font=("Calibri", 14, "bold"), command=toon_prijs_hl)
Owners_LH = Button(LinkerFrame, text="Owners (laag-hoog)", width=24, font=("Calibri", 14, "bold"),
                   command=toon_owners_lh)
Owners_HL = Button(RechterFrame, text="Owners (hoog-laag)", width=24, font=("Calibri", 14, "bold"),
                   command=toon_owners_hl)
Rating_LH = Button(LinkerFrame, text="Rating (laag-hoog)", width=24, font=("Calibri", 14, "bold"),
                   command=toon_rating_lh)
Rating_HL = Button(RechterFrame, text="Rating (hoog-laag)", width=24, font=("Calibri", 14, "bold"),
                   command=toon_rating_hl)


''''Terugknop van Datascherm naar Hoofdscherm'''
Terug = Button(TerugknopFrame, text="Terug naar Hoofdscherm", font=("Calibri", 14, "bold"),
               command=hoofdscherm_tonen)


NameLabel = Entry(Datascherm1, text="AppID", fg='blue', font=('Arial', 12, 'bold'))
GenreLabel = Entry(Datascherm1, text="AppID", fg='blue', font=('Arial', 12, 'bold'))
DateLabel = Entry(Datascherm1, text="AppID", fg='blue', font=('Arial', 12, 'bold'))
PriceLabel = Entry(Datascherm1, text="AppID", fg='blue', font=('Arial', 12, 'bold'))
OwnersLabel = Entry(Datascherm1, text="AppID", fg='blue', font=('Arial', 12, 'bold'))
RatingLabel = Entry(Datascherm1, text="AppID", fg='blue', font=('Arial', 12, 'bold'))
RequiredAgeLabel = Entry(Datascherm1, text="AppID", fg='blue', font=('Arial', 12, 'bold'))


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


hoofdscherm_tonen()
root.mainloop()
