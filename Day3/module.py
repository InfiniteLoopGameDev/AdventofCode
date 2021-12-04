import numpy as np

f = open("data")

lines = f.read()
data = lines.split("\n")
data.pop(len(data) - 1)
count = []
for a in range(len(data[0])):
    count.append(0)
mostCommon = np.array(count, dtype='str')
leastCommon = np.array(count, dtype='str')
gammaStr = ""
epsilonStr = ""

for i in data:
    for e in range(0, len(count)):
        count[e] = int(i[e]) + count[e]

for f in range(0, len(count)):

    temp = count[f] / len(data)

    if temp > 0.5:
        valueG = "1"
        valueE = "0"
    else:
        valueG = "0"
        valueE = "1"

    gammaStr = gammaStr + valueG
    epsilonStr = epsilonStr + valueE

gamma = int(gammaStr, 2)
epsilon = int(epsilonStr, 2)
power = gamma * epsilon
print("Power: {}".format(power))

toRemove = []
count0 = []
for a in range(len(data[0])):
    count0.append(0)

count1 = []
for a in range(len(data[0])):
    count1.append(0)

oxyData = lines.split("\n")
oxyData.pop(len(oxyData) - 1)
coData = lines.split("\n")
coData.pop(len(coData) - 1)

for g in range(0, len(count0)):

    for h in oxyData:
        count0[g] = int(h[g]) + count0[g]
    temp = count0[g] / len(oxyData)

    if temp < 0.5:
        mostCommon[g] = "0"
    elif temp == 0.5:
        mostCommon[g] = "1"
    else:
        mostCommon[g] = "1"

    listPos = 0
    while len(oxyData) != listPos:
        if len(oxyData) == 1:
            break

        if oxyData[listPos][g] != mostCommon[g]:
            oxyData.pop(listPos)
            listPos -= 1

        if listPos >= 0:
            listPos += 1
        else:
            listPos = 0

for j in range(0, len(count1)):

    for k in coData:
        count1[j] = int(k[j]) + count1[j]

    temp0 = count1[j] / len(coData)

    if temp0 < 0.5:
        leastCommon[j] = "1"
    elif temp0 == 0.5:
        leastCommon[j] = "0"
    else:
        leastCommon[j] = "0"

    listPos0 = 0
    while len(coData) != listPos0:
        if len(coData) == 1:
            break

        if coData[listPos0][j] != leastCommon[j]:
            coData.pop(listPos0)
            listPos0 -= 1

        if listPos0 >= 0:
            listPos0 += 1
        else:
            listPos0 = 0

oxyRating = int(oxyData[0], 2)
coRating = int(coData[0], 2)
rating = oxyRating * coRating
print("""Oxygen Rating:{} 
CO2 Rating:{}
Life Support Rating:{}""".format(oxyRating, coRating, rating))
