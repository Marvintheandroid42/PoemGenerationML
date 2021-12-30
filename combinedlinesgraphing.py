import matplotlib.pyplot as plt

file1 = open("losslists.txt", "r")
file2 = open("accuracylists.txt", "r")

file12 = []
file22 = []

for x in file1:
    file12.append(x.strip().rstrip())

for y in file2:
    file22.append(y.strip().rstrip())

count = 0

xlist = []

while count != 40:
    count += 1
    xlist.append(count)

for z in file22:
    plt.plot(xlist, eval(z))

plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.show()