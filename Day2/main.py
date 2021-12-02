f = open("data.txt")

lines = f.read()
data = lines.split("\n")
values = []
aim = 0
x = 0
y = 0

for i in data:
    temp = i.split(" ")
    values.append((temp[0],int(temp[1])))

for e in values:
    if e[0] == "forward":
        x += e[1]
        y += (e[1]*aim)
    elif e[0] == "up":
#        y -= e[1]
        aim -= e[1]
    elif e[0] == "down":
#        y += e[1]
        aim += e[1]

print(x*y)