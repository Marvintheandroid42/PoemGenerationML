import re
import pronouncing
from itertools import permutations
import random
from textblob import TextBlob

#file dependencies

file = open("MiltonIambicOutput.txt", "r")
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

""" for x in lineRhymesDict:
    if len(lineRhymesDict[x]) != 0:
        for y in lineRhymesDict[x]:
            print(x, " - ", y)
print(lineRhymesDict) """



# Generate Couplets:

""" keysList2 = list(lineRhymesDict)
coupletList = []
for key in lineRhymesDict:
    if len(lineRhymesDict.get(key)) != 0:
        bigList = lineRhymesDict.get(key)
        keyNum = int(keysList2.index(key))
        print(bigList)
        for number in bigList:
            coupletList.append([keyNum,number])
            coupletList.append([number, keyNum])
for x in coupletList:
    print("LINE 1 - ", formattedLines[int(x[0])])
    print("LINE 2 - ", formattedLines[int(x[1])]) """

keysList2 = list(lineRhymesDict)

coupletList = []

for key in lineRhymesDict:
    if len(lineRhymesDict.get(key)) != 0:
        bigList = lineRhymesDict.get(key)
        keyNum = lineAndWordDict.get(key)
        for number in bigList:
            coupletList.append([keyNum,number])
            coupletList.append([number, keyNum])

""" for x in coupletList:
    print("LINE 1 - ", x[0])
    print("LINE 2 - ", x[1])
 """

def quartain(numList):
    lineNumList = []
    quartainList = []
    line13 = numList[random.randint(0, len(numList)-1)]
    quartainList.append(line13[0])
    quartainList.append(line13[1])
    lineNumList.append(line13[0])
    lineNumList.append(line13[1])
    for line24 in numList:
        line24 = list(line24)
        if line24[0] not in quartainList and line24[1] not in quartainList:
            #print("if loop bypassed C2")
            quartainList.insert(1, line24[0])
            quartainList.insert(3, line24[1])
            lineNumList.append(line24[0])
            lineNumList.append(line24[1])
            break
    for line56 in numList:
        line56 = list(line56)
        if line56[0] not in quartainList and line56[1] not in quartainList:
            #print("if loop bypassed  C3")
            quartainList.insert(4, line56[0])
            quartainList.insert(5, line56[1])
            lineNumList.append(line56[0])
            lineNumList.append(line56[1])
            break
    for line78 in numList:
        line78 = list(line78)
        if line78[0] not in quartainList and line78[1] not in quartainList:
            #print("if loop bypassed C4")
            quartainList.insert(5, line78[0])
            quartainList.insert(7, line78[1])
            lineNumList.append(line78[0])
            lineNumList.append(line78[1])
            break
    for line910 in numList:
        line910 = list(line910)
        if line910[0] not in quartainList and line910[1] not in quartainList:
            #print("if loop bypassed C5")
            quartainList.insert(8, line910[0])
            quartainList.insert(9, line910[1])
            lineNumList.append(line910[0])
            lineNumList.append(line910[1])
            break
    for line1112 in numList:
        line1112 = list(line1112)
        if line1112[0] not in quartainList and line1112[1] not in quartainList:
            #print("if loop bypassed C6")
            quartainList.insert(9, line1112[0])
            quartainList.insert(11, line1112[1])
            lineNumList.append(line1112[0])
            lineNumList.append(line1112[1])
            break
    for line1314 in numList:
        line1314 = list(line1314)
        if line1314[0] not in quartainList and line1314[1] not in quartainList:
            #print("if loop bypassed C7")
            quartainList.append(line1314[0])
            quartainList.append(line1314[1])
            lineNumList.append(line1314[0])
            lineNumList.append(line1314[1])
            break

    return quartainList


outfile = open("MiltonSonnetGeneration.txt", "w")

count = 0 

while count != 1000:
    sonnet = quartain(coupletList)
    constant = 0
    constant1 = 0
    for x in sonnet:
        textBlob = TextBlob(x)
        polarizer = (textBlob.sentiment.polarity)*10
        constant += polarizer
        constant1 += 1
    constant = constant/constant1
    if round(constant) == 1 or round(constant) == -1:
        print(constant)
        for y in sonnet:
            outfile.write(str(x)+"\n")
        outfile.write("SENTIMENT SCORE - "+ str(constant))
    count += 1
