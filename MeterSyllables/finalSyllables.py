from big_phoney import BigPhoney

phoney = BigPhoney()

file = open("finalEDK.txt", "r")

fileouput = open("DickensonIambicOuput8.txt", "w")

lines = file.readlines()

for line in lines:
    line.strip().rstrip()
    if phoney.count_syllables(line) == 8:
        print("WORKING")
        print(phoney.count_syllables(line))
        fileouput.write(line+"\n")
    

