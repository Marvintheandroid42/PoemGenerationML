import requests
import json


data = requests.get("https://poetrydb.org/author/Emily%20Dickinson")

files = data.json()

st = open("otherPoemStorage1.txt", "w")

st.truncate(0)

storage = []
for x in files:
    subset = x["lines"]
    for y in subset:
        storage.append(y)

for line in storage:
    seperator = ""
    seperator.join(line)
    newline = line+"\n"
    st.write(newline)


""" lineFile = open("lineFile.txt", "w")

for poem in storage:
    lineFile.write(poem)

lineFile.close()

lineFile = open("lineFile.txt", "r")

fileopen = lineFile.readlines()
  
print(fileopen) """
