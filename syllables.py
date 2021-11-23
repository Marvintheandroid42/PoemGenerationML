import pronouncing
import re

file = open("sentimentgenerated.txt", "r")

poem = file.readlines()

linesList = []
for line in poem:
    splitline = line.split()
    wordlist = []
    for word in splitline:
        noAN = re.sub("[,;:.!-?']", "", word)
        phones = pronouncing.phones_for_word(noAN)
        wordlist.append(phones)
    linesList.append(wordlist)

delList = []

print(len(linesList))
finalList = []   


for index in range(0,len(linesList)):
    for subindex in linesList[index]:
        if len(subindex) == 0:
            delList.append(index)
            break


for x in linesList:
    if linesList.index(x) not in delList:
        finalList.append(x) 
        
    
for x in range(0,len(finalList)):
    for y in finalList[x]:
        if len(y) > 1:
            iNum = finalList[x].index(y)
            finalList[x][iNum] = [y[1]]


print(finalList)



#stresses = pronouncing.stresses(phones[0])
#print(stresses)
#wordlist.append(stresses)
#linesList.append(wordlist)


