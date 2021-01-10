from tkinter import *
from tkinter.messagebox import showinfo
import requests

"""Data opvragen van onderstaande link d.m.v. requests.get"""
github_example = "https://raw.githubusercontent.com/AlphaConsultants/ALPHA/main/AI/textdocumenttest.json"
json_data = requests.get(github_example).json()

games_list = []


def data_in_datastructuur():
    """Functie haalt nuttige info uit json en zet het in games_list als tuples. games_list = [(),(),()]"""
    games_list.clear()
    for data in json_data:
        rating_in_percentage = ((data["positive_ratings"] - data["negative_ratings"]) / data["positive_ratings"]) * 100
        rating_in_percentage_afgerond = str(round(rating_in_percentage, 1))
        data_per_game = data["name"], data["genres"], data["release_date"], data["price"], data[
            "owners"], rating_in_percentage_afgerond
        games_list.append(tuple(data_per_game))


def bubblesort(choice, reverse):
    """Functie sorteert opgehaalde data
        Sorteren op:
    -   reverse 0 = A-Z, Oud-Nieuw, Laag-Hoog
    -   reverse 1 = Z-A, Nieuw-Oud, Hoog-Laag
    -   choice 0 = Naam
    -   choice 1 = Genre
    -   choice 2 = Releasedatum
    -   choice 3 = Prijs
    -   choice 4 = Owners
    -   choice 5 = Rating"""
    n = len(games_list)
    if reverse == 0:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][choice] > games_list[g+1][choice]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list
    elif reverse == 1:
        for index in range(n):
            for g in range(0, n - index - 1):
                if games_list[g][choice] < games_list[g+1][choice]:
                    games_list[g], games_list[g+1] = games_list[g+1], games_list[g]
        return games_list


def beginscherm_tonen():
    """Functie toont eerste scherm van GUI"""
    OngesorteerdeDataScherm.pack_forget()
    SorteerButtonsScherm.pack_forget()
    SorteerButtonsScherm1.pack_forget()
    GesorteerdeDataScherm.pack_forget()
    GesorteerdeDataScherm1.pack_forget()
    ZoekenInDataScherm.pack_forget()
    ZoekenInDataScherm1.pack_forget()
    BeginScherm.pack()


def ongesorteerde_datascherm_tonen():
    """Functie toont ongesorteerde datascherm van GUI"""
    BeginScherm.pack_forget()
    OngesorteerdeDataScherm.pack()
    data_in_datastructuur()
    GesorteerdeDataScherm1.pack()
    total_rows = len(games_list)
    total_columns = len(games_list[0])
    for games in range(total_rows):
        for game in range(total_columns):
            e = Entry(GesorteerdeDataScherm1, fg='blue', font=('Arial', 12, 'bold'), width=18)
            e.grid(row=games, column=game)
            e.insert(END, games_list[games][game])


def sorteeroptiesscherm_tonen():
    """Functie toont sorteeropties scherm van GUI"""
    BeginScherm.pack_forget()
    GesorteerdeDataScherm.pack_forget()
    GesorteerdeDataScherm1.pack_forget()
    GesorteerdeDataScherm2.pack_forget()
    SorteerButtonsScherm.pack()
    SorteerButtonsScherm1.pack()


def gesorteerde_datacherm_tonen():
    """Functie toont gesorteerde datascherm van GUI"""
    SorteerButtonsScherm.pack_forget()
    SorteerButtonsScherm1.pack_forget()
    GesorteerdeDataScherm2.pack_forget()
    GesorteerdeDataScherm.pack()
    GesorteerdeDataScherm1.pack()
    total_rows = len(games_list)
    total_columns = len(games_list[0])
    for games in range(total_rows):
        for game in range(total_columns):
            e = Entry(GesorteerdeDataScherm1, fg='blue', font=('Arial', 12, 'bold'), width=18)
            e.grid(row=games, column=game)
            e.insert(END, games_list[games][game])


def zoeken_in_datascherm_tonen():
    """Functie toont zoeken in datascherm van GUI"""
    BeginScherm.pack_forget()
    Zoekvak.delete(0, "end")
    ZoekenInDataScherm.pack()


def zoeken(choice, target):
    """"Functie zoekt in opgehaalde data naar de zoekopdracht
        Zoeken op:
    -   choice 0 = Naam
    -   choice 1 = Genre"""
    games_list2 = []
    if not target:
        ZoekenInDataScherm1.pack_forget()
        waarschuwing = "Voer eerst een zoekopdracht in."
        showinfo(title='popup', message=waarschuwing)
        ZoekenInDataScherm1.destroy()
    else:
        games_list2.clear()
        for char in games_list:
            if target in char[choice]:
                games_list2.append(tuple(char))
        if not games_list2:
            bericht2 = 'Uw zoekopdracht komt niet voor in de lijst.'
            showinfo(title='popup', message=bericht2)
            ZoekenInDataScherm1.pack_forget()
            Zoekvak.delete(0, "end")
        else:
            bericht = 'Uw zoekopdracht komt voor in de lijst.'
            showinfo(title='popup', message=bericht)
            Zoekvak.delete(0, "end")
            total_rows = len(games_list2)
            total_columns = len(games_list2[0])
            for games in range(total_rows):
                for game in range(total_columns):
                    e = Entry(ZoekenInDataScherm1, fg='blue', font=('Arial', 12, 'bold'), width=18)
                    e.grid(row=games, column=game)
                    e.insert(END, games_list2[games][game])
                ZoekenInDataScherm1.pack()


def naam_clicked():
    """Functie voert zoeken(choice, target) uit na geklik"""
    zoekopdracht = Zoekvak.get()
    zoeken(0, zoekopdracht)


def genre_clicked():
    """Functie voert zoeken(choice, target) uit na geklik"""
    zoekopdracht = Zoekvak.get()
    zoeken(1, zoekopdracht)


def eerste_spel_in_gesorteerdescherm_tonen():
    """Functie toont eerste spel van ongesorteerde lijst"""
    SorteerButtonsScherm.pack_forget()
    SorteerButtonsScherm1.pack_forget()
    GesorteerdeDataScherm1.pack_forget()
    GesorteerdeDataScherm.pack()
    GesorteerdeDataScherm2.pack()
    data_in_datastructuur()
    GesorteerdTitel["text"] = "Eerste spel in ongesorteerde lijst"
    a = games_list[0][0]
    e = Entry(GesorteerdeDataScherm2, fg='blue', font=('Arial', 12, 'bold'))
    e.grid(row=0, column=0)
    e.insert(END, a)


def toon_naam_az():
    """Functie toont tabel gesorteerd op Naam"""
    bubblesort(0, 0)
    GesorteerdTitel["text"] = "Gesorteerd op Naam A-Z"
    gesorteerde_datacherm_tonen()


def toon_naam_za():
    """Functie toont tabel gesorteerd op Naam"""
    bubblesort(0, 1)
    GesorteerdTitel["text"] = "Gesorteerd op Naam Z-A"
    gesorteerde_datacherm_tonen()


def toon_genre_az():
    """Functie toont tabel gesorteerd op Genre"""
    bubblesort(1, 0)
    GesorteerdTitel["text"] = "Gesorteerd op Genre A-Z"
    gesorteerde_datacherm_tonen()


def toon_genre_za():
    """Functie toont tabel gesorteerd op Genre"""
    bubblesort(1, 1)
    GesorteerdTitel["text"] = "Gesorteerd op Genre Z-A"
    gesorteerde_datacherm_tonen()


def toon_release_date_on():
    """Functie toont tabel gesorteerd op Releasedate"""
    bubblesort(2, 0)
    GesorteerdTitel["text"] = "Gesorteerd op Releasedatum Oud-Nieuw"
    gesorteerde_datacherm_tonen()


def toon_release_date_no():
    """Functie toont tabel gesorteerd op Releasedate"""
    bubblesort(2, 1)
    GesorteerdTitel["text"] = "Gesorteerd op Releasedatum Nieuw-Oud"
    gesorteerde_datacherm_tonen()


def toon_prijs_lh():
    """Functie toont tabel gesorteerd op Prijs"""
    bubblesort(3, 0)
    GesorteerdTitel["text"] = "Gesorteerd op Prijs Laag-Hoog"
    gesorteerde_datacherm_tonen()


def toon_prijs_hl():
    """Functie toont tabel gesorteerd op Prijs"""
    bubblesort(3, 1)
    GesorteerdTitel["text"] = "Gesorteerd op Prijs Hoog-Laag"
    gesorteerde_datacherm_tonen()


def toon_owners_hl():
    """Functie toont tabel gesorteerd op Owners"""
    bubblesort(4, 0)
    GesorteerdTitel["text"] = "Gesorteerd op Owners Laag-Hoog"
    gesorteerde_datacherm_tonen()


def toon_owners_lh():
    """Functie toont tabel gesorteerd op Owners"""
    bubblesort(4, 1)
    GesorteerdTitel["text"] = "Gesorteerd op Owners Hoog-Laag"
    gesorteerde_datacherm_tonen()


def toon_rating_lh():
    """Functie toont tabel gesorteerd op Rating"""
    bubblesort(5, 0)
    GesorteerdTitel["text"] = "Rating (laag-hoog)"
    gesorteerde_datacherm_tonen()


def toon_rating_hl():
    """Functie toont tabel gesorteerd op Rating"""
    bubblesort(5, 1)
    GesorteerdTitel["text"] = "Rating (hoog-laag)"
    gesorteerde_datacherm_tonen()


root = Tk()
root.title("Dashboard Steam")
root.geometry("1500x1000")
root.configure(bg="#17202e")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FRAMES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Frame van eerste scherm GUI"""
BeginScherm = Frame(root, bg="#17202e")

"""Frame van ongesorteerde datascherm."""
OngesorteerdeDataScherm = Frame(root, bg="#17202e")

"""Frames van de sorteeropties scherm"""
SorteerButtonsScherm = Frame(root, bg="#17202e")
SorteerButtonsScherm1 = Frame(root, bg="#17202e")

"""Frame van gesorteerde datascherm"""
GesorteerdeDataScherm = Frame(root, bg="#17202e")
GesorteerdeDataScherm1 = Frame(root, bg="#17202e")
GesorteerdeDataScherm2 = Frame(root, bg="#17202e")

"""Frame van zoeken in datascherm"""
ZoekenInDataScherm = Frame(root, bg="#17202e")
ZoekenInDataScherm1 = Frame(root, bg="#17202e")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FRAME-BEGINSCHERM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Titel van eerste scherm GUI en Label voor het maken van een keuze"""
BeginschermTitel = Label(BeginScherm, text="Alpha Consultants", bg="#17202e", fg="white", font=("Calibri", 40, "bold", "underline"))
keuze = Label(BeginScherm, text="Maak een keuze:", bg="#17202e", fg="white", font=("Calibri", 22, "bold"))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~FRAME-GESORTEERDE DATASCHERM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Titel van ongesorteerde scherm GUI"""
OngesorteerdTitel = Label(OngesorteerdeDataScherm, text="Data ongesorteerd:", bg="#17202e", fg="white", font=("Calibri", 22, "bold"))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FRAME-SORTEEROPTIES SCHERM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Titel van Sorteeropties scherm en buttons voor het sorteren"""
EersteSpelTonen = Label(SorteerButtonsScherm, text="Toon eerste spel in ongesorteerde lijst:", bg="#17202e", fg="white", font=("Calibri", 22, "bold"))
Eerste_Spel = Button(SorteerButtonsScherm, text="Eerste Spel", width=24, font=("Calibri", 14, "bold"), command=eerste_spel_in_gesorteerdescherm_tonen)
SorterenOp = Label(SorteerButtonsScherm, text="Sorteren op:", bg="#17202e", fg="white", font=("Calibri", 22, "bold", "underline"))
Name_AZ = Button(SorteerButtonsScherm1, text="Naam (A-Z)", width=24, font=("Calibri", 14, "bold"), command=toon_naam_az)
Name_ZA = Button(SorteerButtonsScherm1, text="Naam (Z-A)", width=24, font=("Calibri", 14, "bold"), command=toon_naam_za)
Genre_AZ = Button(SorteerButtonsScherm1, text="Genre (A-Z)", width=24, font=("Calibri", 14, "bold"), command=toon_genre_az)
Genre_ZA = Button(SorteerButtonsScherm1, text="Genre (Z-A)", width=24, font=("Calibri", 14, "bold"), command=toon_genre_za)
ReleaseDate_ON = Button(SorteerButtonsScherm1, text="Releasedatum (oud-nieuw)", width=24, font=("Calibri", 14, "bold"),
                        command=toon_release_date_on)
ReleaseDate_NO = Button(SorteerButtonsScherm1, text="Releasedatum (nieuw-oud)", width=24, font=("Calibri", 14, "bold"),
                        command=toon_release_date_no)
Price_LH = Button(SorteerButtonsScherm1, text="Prijs (laag-hoog)", width=24, font=("Calibri", 14, "bold"), command=toon_prijs_lh)
Price_HL = Button(SorteerButtonsScherm1, text="Prijs (hoog-laag)", width=24, font=("Calibri", 14, "bold"), command=toon_prijs_hl)
Owners_LH = Button(SorteerButtonsScherm1, text="Owners (laag-hoog)", width=24, font=("Calibri", 14, "bold"),
                   command=toon_owners_lh)
Owners_HL = Button(SorteerButtonsScherm1, text="Owners (hoog-laag)", width=24, font=("Calibri", 14, "bold"),
                   command=toon_owners_hl)
Rating_LH = Button(SorteerButtonsScherm1, text="Rating (laag-hoog)", width=24, font=("Calibri", 14, "bold"),
                   command=toon_rating_lh)
Rating_HL = Button(SorteerButtonsScherm1, text="Rating (hoog-laag)", width=24, font=("Calibri", 14, "bold"),
                   command=toon_rating_hl)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~FRAME-GESORTEERDE DATASCHERM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Titel van gesorteerde scherm GUI"""
GesorteerdTitel = Label(GesorteerdeDataScherm, text="", bg="#17202e", fg="white", font=("Calibri", 22, "bold"))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~FRAME-ZOEKEN IN DATASCHERM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Titel van zoeken in data scherm GUI en Buttons met zoekvak"""
ZoekschermTitel = Label(ZoekenInDataScherm, text="Type uw zoekopdracht in het vakje hieronder en klik op één van de buttons waarop u wilt zoeken.",
                        bg="#17202e", fg="white", font=("Arial", 14, "bold"))
Zoekvak = Entry(ZoekenInDataScherm, width=50, fg='blue', font=('Arial', 12, 'bold'))
NameButton = Button(ZoekenInDataScherm, text="Naam", width=15, font=("Calibri", 14, "bold"), command=naam_clicked)
GenreButton = Button(ZoekenInDataScherm, text="Genre", width=15, font=("Calibri", 14, "bold"), command=genre_clicked)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~NAVIGEREN TUSSEN SCHERMEN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Buttons voor het navigeren tussen schermen in de GUI"""
OngesorteerdeDataButton = Button(BeginScherm, text="Data ongesorteerd weergeven", width=30, font=("Calibri", 14, "bold"),
                                 command=ongesorteerde_datascherm_tonen)
VanOngesorteerdeDataSchermNaarBeginscherm = Button(OngesorteerdeDataScherm, text="Terug", font=("Calibri", 14, "bold"),
                                                   command=beginscherm_tonen)
SorteerButton = Button(BeginScherm, text="Data sorteren", width=30, font=("Calibri", 14, "bold"),
                       command=sorteeroptiesscherm_tonen)
VanSorteerButtonsSchermNaarBeginscherm = Button(SorteerButtonsScherm, text="Terug", font=("Calibri", 14, "bold"),
                                                command=beginscherm_tonen)
VanGesorteerdeDataSchermNaarSorteerButtonsScherm = Button(GesorteerdeDataScherm, text="Terug",
                                                          font=("Calibri", 14, "bold"), command=sorteeroptiesscherm_tonen)
ZoekenInDataButton = Button(BeginScherm, text="Zoeken in Data", width=30, font=("Calibri", 14, "bold"),
                            command=zoeken_in_datascherm_tonen)
VanZoekenInDataSchermNaarBeginscherm = Button(ZoekenInDataScherm, text="Terug", font=("Calibri", 14, "bold"),
                                              command=beginscherm_tonen)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~POSITIES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Posities van widgets in Beginscherm"""
BeginschermTitel.pack(pady=100)
keuze.pack(pady=50)
OngesorteerdeDataButton.pack(pady=20)
SorteerButton.pack(pady=20)
ZoekenInDataButton.pack(pady=20)

"""Posities van widgets in OngesorteerdeDataScherm"""
VanOngesorteerdeDataSchermNaarBeginscherm.pack(pady=50)
OngesorteerdTitel.pack(pady=20)

"""Posities van widgets in SorteerButtonsScherm"""
VanSorteerButtonsSchermNaarBeginscherm.pack(pady=50)
EersteSpelTonen.pack(pady=20)
Eerste_Spel.pack()
SorterenOp.pack(pady=20)
Name_AZ.grid(row=0, column=0)
Name_ZA.grid(row=0, column=1)
Genre_AZ.grid(row=1, column=0)
Genre_ZA.grid(row=1, column=1)
ReleaseDate_ON.grid(row=2, column=0)
ReleaseDate_NO.grid(row=2, column=1)
Price_LH.grid(row=3, column=0)
Price_HL.grid(row=3, column=1)
Owners_LH.grid(row=4, column=0)
Owners_HL.grid(row=4, column=1)
Rating_LH.grid(row=5, column=0)
Rating_HL.grid(row=5, column=1)

"""Posities van widgets in GesorteerdeDataScherm"""
VanGesorteerdeDataSchermNaarSorteerButtonsScherm.pack(pady=50)
GesorteerdTitel.pack(pady=20)

"""Posities van widgets in ZoekenInDataScherm"""
VanZoekenInDataSchermNaarBeginscherm.pack(pady=50)
ZoekschermTitel.pack()
Zoekvak.pack(pady=20)
NameButton.pack()
GenreButton.pack()


data_in_datastructuur()
beginscherm_tonen()
root.mainloop()
