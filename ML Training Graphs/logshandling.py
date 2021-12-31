import matplotlib.pyplot as plt
import numpy as np

file = open("logs.txt", "r")

lines = file.readlines()

lines1 = []

for x in lines:
    lines1.append(x.strip().rstrip())

for y in lines1:
    if "Epoch" in y:
        lines1.pop(lines1.index(y))

lines1.pop(0)

loss = []

accuracy = []

for z in lines1:
    d = str(z)
    f = d.split(" - ")
    loss.append(float(f[2].replace("loss:", "")))
    accuracy.append(float(f[3].replace("accuracy:", "")))

count = 0

xlist = []

while count != 40:
    count += 1
    xlist.append(count)

print(xlist)
print(len(loss))

xlist1 = xlist

print(loss)
print(accuracy)

plot = plt.plot(xlist, loss, label = "loss")

plot1 = plt.plot(xlist1, accuracy, label = "accuracy")

plt.xlabel('epochs')

plt.legend()

plt.show()
    

