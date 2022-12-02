with open("Year2022/Day2/data", "r") as file:
    raw_data = file.readlines()
data = []
for i in raw_data:
    data += [x.strip("\n") for x in i.split(" ")]

score = 0
winners = [
  ["C", "B", "A"],
  ["X", "Z", "Y"]
]


for i in range(0, int(len(data) / 2), 2):
  if ord(data[i]) + 23 == ord(data[i + 1]):
    score += 3
  elif winners[1][winners[0].index(data[i])] == data[i + 1]:
    score += 6
  score += ord(data[i + 1]) - 87

print(score)