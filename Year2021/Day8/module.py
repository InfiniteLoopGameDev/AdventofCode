import re
import math

f = open("Year2021/Day8/data")

lines = f.read()
dataStr = lines.split("\n")
dataStr.pop(-1)
dataList = []
data = []
# for i in dataStr:
#     dataList.append(i.split("|")[1])
for i in dataStr:
    data = data + i.split(" ")

# data.pop(0)
segmentsCipher = []
segmentsDecode = []

near = False
count = 0
temp = []
for i in data:
    if i != "|":
        temp.append(i)
        if near:
            count += 1
    if i == "|":
        temp.append(i)
        near = True
    if count == 4:
        segmentsCipher.append(temp)
        temp = []
        near = False
        count = 0

value = ""
temp2 = []
for i in segmentsCipher:
    for j in i:
        if len(j) == 2:
            value += "1"
        elif len(j) == 3:
            value += "7"
        elif len(j) == 4:
            value += "4"
        elif len(j) == 7:
            value += "8"
        elif j == "|":
            temp2.append(value)
            value = ""
        else:
            value += "."
    temp2.append(value)
    temp.append(temp2)
    temp2 = []
    for j in i:
        if len(j) == 5:
            help

print(temp)
