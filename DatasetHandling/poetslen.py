import requests
import json

response = requests.get("https://poetrydb.org/author")

jsonFile = response.json()

list = jsonFile["authors"]

authorDict = {}
for author in list:
    response2 = requests.get("https://poetrydb.org/author/"+author)
    jsonFile2 = response2.json()
    numberOfLines = 0
    for v in jsonFile2:
        numberOfLines += int(v["linecount"])
    authorDict[author] = numberOfLines

print(authorDict)

for xy in authorDict:
    if authorDict.get(xy) >= 10000:
        print(xy)
