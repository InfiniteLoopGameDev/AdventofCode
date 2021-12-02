import numpy as np

count = 0

f = open("Day1/data")

lines = f.read()
data = lines.split("\n")
data.pop(2000)
data = np.array(data, dtype='int')

window = []

for i in range(0, (len(data)-2)):
    window.append(data[i] + data[(i + 1)] + data[(i + 2)])

for e in range(0, (len(window))):
    if window[e] > window[(e - 1)]:
        print("{sum}, increased".format(sum=window[e]))
        count += 1
    else:
        print("{sum}, decreased".format(sum=window[e]))


print(count)
