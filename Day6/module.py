f = open("Day6/data")

lines = f.read()
dataStr = lines.split(",")
data = []
for i in dataStr:
  data.append(int(i))
count = 0

for e in range(80):
  count += 1
  print(data)
  for i in range(0, len(data)):
    if int(data[i]) == 0:
      data[i] = 6
      data.append(8)
    else:
      data[i] -= 1

print(len(data))