from textblob import TextBlob
import requests
import json



#data = requests.get("https://poetrydb.org/author/John%20Milton")

#f = data.json()

#storage = []

file = open("thou2.txt", "r")

f = file.readlines()

#for x in f:
    #subset = x["lines"]
    #for y in subset:
        #storage.append(y)


words = []
for line in f:
    #for word in line.split():
    words.append(line) 


pol = []

newscen = open("sentimentgenerated.txt", "w")
for x in words:
    y = TextBlob(x)
    polarizer = (y.sentiment.polarity)*10
    pol.append(polarizer)
    if polarizer != 0:
        newscen.write(x)
        print("added")

print(pol)
