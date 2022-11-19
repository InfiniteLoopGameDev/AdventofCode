f = open("Year2021/Day6/data")

lines = f.read()
dataStr = lines.split(",")
data = []
for i in dataStr:
    data.append(int(i))

fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in data:
    fishes[i] += 1

for i in range(256):
    temp = fishes[0]
    fishes[0] = fishes[1]
    fishes[1] = fishes[2]
    fishes[2] = fishes[3]
    fishes[3] = fishes[4]
    fishes[4] = fishes[5]
    fishes[5] = fishes[6]
    fishes[6] = fishes[7] + temp
    fishes[7] = fishes[8]
    fishes[8] = temp
    if i == 79:
        print("80 days: {}".format(sum(fishes)))

print("256 days: {}".format(sum(fishes)))
