from re import split
import pronouncing
import re

file = open("sentimentgenerated.txt", "r")

sentLines = file.readlines()
rhymeLines = []
rhymedict = {}
for x in sentLines:
    noAN = re.sub("[,;:.!-?]", "",x)
    splitString = noAN.split()   
    rhymes = pronouncing.rhymes(splitString[len(splitString)-1])
    for y in rhymes:
        if splitString[len(splitString)-1] == y:
            for z in rhymes:
                if z in rhymedict:
                    rhymedict[z] = rhymedict[z].append(x)

    #print(splitString[len(splitString)-1])
    #print(rhymes)
    #rhymeLines.append(splitString)
        else:
            rhymedict.update({splitString[len(splitString)-1]:[x]})

print(rhymedict)
