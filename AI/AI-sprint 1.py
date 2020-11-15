from tkinter import *
import requests

file = open("github_voorbeeld", "r+")

github_example = "https://raw.githubusercontent.com/tijmenjoppe/AnalyticalSkills-student/master/project/data/steam.json"
json_data = requests.get(github_example).json()
file.write(str(json_data))

def toon_eerste_spel():
    eerste_spel_frame.pack()
    data = json_data[0]
    eerste_spel = data["name"]
    spel_label = Label(eerste_spel_frame, text=eerste_spel, bg="red", fg="white", font=("Calibri", 27, "bold"))
    spel_label.pack(pady=80)

root = Tk()
root.title("Dashboard Steam")
root.geometry("1800x1000")
root.configure(bg="#17202e")
eerste_spel_frame = Frame(root, bg="#17202e")

titel = Label(root, text="Dashboard Steam", bg="#17202e", fg="white", font=("Calibri", 34, "bold"))
titel.pack(pady=130)

toon_eerste_spel()
root.mainloop()
