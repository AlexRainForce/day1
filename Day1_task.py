import os
import json
import datetime

os.makedirs("notes", exist_ok=True)

name = input("write your name: ")
note = input("write you notes")
date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

data = {"Name": name, "Note": note, "Date": date} #словарь для Json

#зпись 

with open("notes/data.json", "w") as f:
    json.dump(data, f)

print("note has been saved")
#чтение
with open("notes/data.json", "r") as f:
    loaded = json.load(f)
print(loaded)



