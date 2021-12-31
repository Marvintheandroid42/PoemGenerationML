import re
import pronouncing
from itertools import permutations
import random
from textblob import TextBlob

#file dependencies

file = open("DickensonIambicOuput.txt", "r")
file1 = open("rhymeStorage.txt", "w")
file2 = open("permutations.txt", "w")

iambicLines = file.readlines()

#Formatting the lines and taking away nulls (WORKS)
formattedLines = []

for line in iambicLines:
    if line != "\n":
        formattedLines.append(line.strip())

#Finding Rhymes for the end words for each sentence (WORKS OUPUT: 228 lines with rhymes / 276 lines  )

rhymeDictForWords = {}

lineAndWordDict = {}


for line2 in formattedLines:
    noAN = re.sub("[,;:.!-?]", "", line2)
    splitString = noAN.split()
    rhymeForWord = pronouncing.rhymes(splitString[len(splitString)-1])
    rhymeDictForWords[splitString[len(splitString)-1]] = rhymeForWord
    lineAndWordDict[splitString[len(splitString)-1]] = line2

#Relating the rhyming words with the scentences (WORKS, OUTPUT = generates rhyming pairs)

keysList = list(rhymeDictForWords)

lineRhymesDict = {}

multipleRhymesDict = {}

rhymecount = 0

for key in rhymeDictForWords:
    lineRhymesDict[key] = []
    for rhyme in rhymeDictForWords:
        if key in rhymeDictForWords.get(rhyme):
            rhymecount += 1
            #print("WORD 1 - ", key, "WORD2 -  ", rhyme )
            lineRhymesDict[key].append(lineAndWordDict[rhyme])

coupletList = []
for key in lineRhymesDict:
    if len(lineRhymesDict.get(key)) != 0:
        bigList = lineRhymesDict.get(key)
        keyNum = lineAndWordDict.get(key)
        for number in bigList:
            coupletList.append([keyNum,number])
            coupletList.append([number, keyNum])

eightlinefile = open("DickensonIambicOuput8.txt", "r")
eightsylformatted = []

eightsyl = eightlinefile.readlines()

for line in eightsyl:
    if line != "\n":
        eightsylformatted.append(line.strip())

def quartain(sixlist, eightlist):
    quartainList = []
    line24 = sixlist[random.randint(0, len(sixlist)-1)]
    line1 = eightlist[random.randint(0, len(eightlist)-1)]
    counter = False
    while counter == False:
        place = random.randint(0, len(eightlist)-1)
        if place != eightlist.index(line1):
            line3 = eightlist[place]
            counter = True
    quartainList.append(line1)
    quartainList.append(line24[0])
    quartainList.append(line3)
    quartainList.append(line24[1])
    return quartainList

#INTERATE SENTIMENT ANALYSIS

sonnet = quartain(coupletList, eightsylformatted)

for x in sonnet:
    print(x, "\n")
