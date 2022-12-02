import re
with open("Year2022/Day2/data", "r") as file:
    raw_data = file.read()
data = re.split("\W+", raw_data)
score1 = 0
score2 = 0
winners = [
  ["C", "B", "A"],
  ["X", "Z", "Y"]
]
loser = [
    ["C" , "B", "A"],
    ["Y" , "X", "Z"]
]


for i in range(0, len(data), 2):
    if ord(data[i]) + 23 == ord(data[i + 1]):
        score1 += 3
    elif winners[1][winners[0].index(data[i])] == data[i + 1]:
        score1 += 6
    score1 += ord(data[i + 1]) - 87
    if data[i+1] == "X":
        score2 += ord(loser[1][loser[0].index(data[i])]) - 87
    elif data[i+1] == "Y":
        score2 += 3
        score2 += ord(data[i]) - 64
    else:
        score2 += 6
        score2 += ord(winners[1][winners[0].index(data[i])]) - 87

print(score1)
print(score2)
