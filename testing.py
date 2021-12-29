import re
import pronouncing
from itertools import permutations
import random

file = open("MiltonIambicOutput.txt", "r")
file1 = open("rhymeStorage.txt", "w")
file2 = open("permutations.txt", "w")

sentLines = file.readlines()

""" newLines = []
#THIS WAS ABLE TO GENERALIZE BUT NOT OTHER
for xy in sentLines:
    l = xy.strip().rstrip()
    newLines.append(l)
    print(l)


for x in newLines:
    if x == "" or len(x) == 1:
        newLines.pop(int(newLines.index(x))) """

"""     if x.isalpha == False:
        print("notslpha", x) """

# !!!TALK ABOUT HOW THE BRUTE FORCE WAS DONE AS FORMATTING WAS DIFFERENT ON EVERYTHING;
# FIND A WAY TO GENERALIZE FORMATTING!!

newLines = []
for syllable in sentLines:
    if syllable != "\n":
        newLines.append(syllable.strip())

for x in newLines:
    file1.write(x)

rhymeLines = []
rhymedictforwords = {}
# THINK ABOUT WRITING CLEANER MORE EXPRESSIVE CODE

# !? Function that takes in the end of each line and then finds words that rhyme with it
for x in newLines:
    noAN = re.sub("[,;:.!-?]", "", x)
    print(x)

    splitString = noAN.split()
    rhymeForWord = pronouncing.rhymes(splitString[len(splitString)-1])
    rhymedictforwords[splitString[len(splitString)-1]] = rhymeForWord

print(rhymedictforwords)

# !? Makes the value of the word keys into lists for iteration
keys_list = list(rhymedictforwords)

print(keys_list)

linesDict = {}

for key in rhymedictforwords:
    linesDict[key] = []
    for list1 in rhymedictforwords:
        if key in rhymedictforwords.get(list1):
            linesDict[key].append(keys_list.index(list1))

print(linesDict)

# !? Generate Couplets

coupletDict = {}
keyList = []

for keyvalue in linesDict:
    keyList.append(keyvalue)

permutationsList = []
for key in linesDict:
    if len(linesDict.get(key)) != 0:
        bigList = linesDict.get(key)
        print(bigList)
        bigList.append(int(keyList.index(key)))
        print(bigList)
        smallList = list(permutations(bigList, 2))
        permutationsList.append(smallList)

# Flatten the list
flattenedList = []

for tuplegroup in permutationsList:
    for tuple in tuplegroup:
        flattenedList.append(tuple)

print(flattenedList)

wordList = []
lineList = []
subList = []

print(flattenedList)

# Convert to words
for numberTuple in flattenedList:
    numberTuple = list(numberTuple)
    for x in numberTuple:
        lineList.append(newLines[int(x)])
    wordList.append(lineList)
    lineList = []

print(wordList)

# Randomize  list

sonnetFile = open("sonnetFile.txt", "w")
sonnet = []

flattenedList2 = []

for gh in flattenedList:
    for xy in gh:
        flattenedList2.append(xy)
print(sorted(set(flattenedList2)))

# Quartain


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
            print("if loop bypassed C2")
            quartainList.insert(1, line24[0])
            quartainList.insert(3, line24[1])
            lineNumList.append(line24[0])
            lineNumList.append(line24[1])
            break
    for line56 in numList:
        line56 = list(line56)
        if line56[0] not in quartainList and line56[1] not in quartainList:
            print("if loop bypassed  C3")
            quartainList.insert(4, line56[0])
            quartainList.insert(5, line56[1])
            lineNumList.append(line56[0])
            lineNumList.append(line56[1])
            break
    for line78 in numList:
        line78 = list(line78)
        if line78[0] not in quartainList and line78[1] not in quartainList:
            print("if loop bypassed C4")
            quartainList.insert(5, line78[0])
            quartainList.insert(7, line78[1])
            lineNumList.append(line78[0])
            lineNumList.append(line78[1])
            break
    for line910 in numList:
        line910 = list(line910)
        if line910[0] not in quartainList and line910[1] not in quartainList:
            print("if loop bypassed C5")
            quartainList.insert(8, line910[0])
            quartainList.insert(9, line910[1])
            lineNumList.append(line910[0])
            lineNumList.append(line910[1])
            break
    for line1112 in numList:
        line1112 = list(line1112)
        if line1112[0] not in quartainList and line1112[1] not in quartainList:
            print("if loop bypassed C6")
            quartainList.insert(9, line1112[0])
            quartainList.insert(11, line1112[1])
            lineNumList.append(line1112[0])
            lineNumList.append(line1112[1])
            break
    for line1314 in numList:
        line1314 = list(line1314)
        if line1314[0] not in quartainList and line1314[1] not in quartainList:
            print("if loop bypassed C7")
            quartainList.append(line1314[0])
            quartainList.append(line1314[1])
            lineNumList.append(line1314[0])
            lineNumList.append(line1314[1])
            break

    print(quartainList)
    print(lineNumList)
    return quartainList

# USE LINENUMLIST AS MASTER LIST AND ADD BY CHECKING BACK TO IT
# NOT ENOUGH UNIQUE LINES; GENERATE MORE LINES


sonnet = quartain(flattenedList)

for sonnetline in sonnet:
    print(str(newLines[sonnetline])+"\n")
