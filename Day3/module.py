f = open("Day3/data")

lines = f.read()
data = lines.split("\n")
count = [0,0,0,0,0,0,0,0,0,0,0,0]
mostCommon = ["0","0","0","0","0","0","0","0","0","0","0","0"]
leastCommon = ["0","0","0","0","0","0","0","0","0","0","0","0"]
gammaStr = ""
epsilonStr = ""

for i in data:
  for e in range(0, len(count)):
    count[e] = int(i[e]) + count[e]

for f in range(0, len(count)):
  temp = count[f] / 1000
  if temp > 0.5:
    valueG = "1"
    mostCommon[f] = "1"
    valueE = "0"
    leastCommon[f] = "0"
  else:
    valueG = "0"
    mostCommon[f] = "0"
    valueE = "1"
    leastCommon[f] = "1"
  gammaStr = gammaStr + valueG
  epsilonStr = epsilonStr + valueE

gamma = int(gammaStr, 2)
epsilon = int(epsilonStr, 2)

power = gamma * epsilon
print("Power: {}".format(power))

oxyData = data

for g in range(0, len(count)):
  for h in filter:
    if h[g] != mostCommon[g]:
      oxyData.pop(g)

print(filter)