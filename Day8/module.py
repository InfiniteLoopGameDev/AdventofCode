f = open("Day8/data")

lines = f.read()
dataStr = lines.split("\n")
data = []
for i in dataStr:
    data.append(int(i))