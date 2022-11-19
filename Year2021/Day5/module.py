import numpy as np

f = open("Year2021/Day5/data")

lines = f.read()
data = lines.split("\n")
data.pop(-1)
x = [[], []]
y = [[], []]
grid = np.zeros((1000, 1000))
grid2 = np.zeros((1000, 1000))

for i in range(0, len(data)):
    temp = data[i].split(" -> ")
    x[0].append(int(temp[0].split(",")[0]))
    x[1].append(int(temp[1].split(",")[0]))
    y[0].append(int(temp[0].split(",")[1]))
    y[1].append(int(temp[1].split(",")[1]))

for i in range(0, len(data)):
    coordX = []
    coordY = []
    coords = []
    if y[0][i] == y[1][i]:
        minValue = min(x[0][i], x[1][i])
        diff = abs(x[0][i] - x[1][i])
        for j in range(0, (diff + 1)):
            coord = minValue + j
            grid[y[0][i]][coord] += 1
            grid2[y[0][i]][coord] += 1
    elif x[0][i] == x[1][i]:
        minValue = min(y[0][i], y[1][i])
        diff = abs(y[0][i] - y[1][i])
        for j in range(0, (diff + 1)):
            coord = minValue + j
            grid[coord][x[0][i]] += 1
            grid2[coord][x[0][i]] += 1
    else:
        diff = abs(x[0][i] - x[1][i])
        for j in range(0, (diff + 1)):
            if x[0][i] > x[1][i] and y[0][i] < y[1][i]:
                coordX = x[0][i] - j
                coordY = y[0][i] + j
            elif x[0][i] < x[1][i] and y[0][i] > y[1][i]:
                coordX = x[0][i] + j
                coordY = y[0][i] - j
            else:
                coordX = min(x[0][i], x[1][i]) + j
                coordY = min(y[0][i], y[1][i]) + j
            grid2[coordY][coordX] += 1

count = 0
count0 = 0

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if int(grid[j][i]) > 1:
            count += 1

for i in range(0, len(grid2)):
    for j in range(0, len(grid2[i])):
        if int(grid2[j][i]) > 1:
            count0 += 1

print("Horizontal & Vertical: {}".format(count))

print("Horizontal, Vertical & Diagonal: {}".format(count0))
