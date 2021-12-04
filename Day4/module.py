import numpy as np

f = open("Day4/data")

lines = f.read()
data = lines.split("\n")
boards = int(len(data) / 6)
grid = np.zeros((boards, 5, 5))
temp = ""
tempList = []
nums = data[0].split(",")

for i in range(2):
    data.pop(0)

for i in data:
    if i != "":
        temp = temp + " " + i
    else:
        tempList.append(temp.split())
        temp = ""

tempList = np.array(tempList, dtype='int')
grids = tempList.reshape(boards, 5, 5)
grid90 = np.rot90(grid, k=1, axes=(0, 1))
grid90 = grid90.reshape(boards, 5, 5)
validGrid = 899999
boardsWon = 0
count = 0
count0 = 0
winningGrids = [-1]

for i in nums:
    for j in range(0, len(grids)):
        for k in range(0, len(grids[j])):
            for m in range(0, len(grids[j][k])):
                grid90 = np.rot90(grid, 1, axes=(0, 1))
                grid90 = grid90.reshape(boards, 5, 5)
                if str(grids[j][k][m]) == str(i):
                    grid[j, k, m] = 1
                    if np.sum(grid[j, k]) == 5:
                        for s in winningGrids:
                            if s != j:
                                eligible = True
                            else:
                                eligible = False
                                break
                        if eligible:
                            winningGrids.append(j)
                            boardsWon += 1
                            if boardsWon == 1:
                                validGrid = j
                                validNum = int(i)
                                print("Found Valid Grid: {} @ {}".format(j, i))
                                for o in range(0, len(grids[validGrid])):
                                    for p in range(0, len(grids[validGrid][o])):
                                        if grid[validGrid][o][p] == 0:
                                            count += int(grids[validGrid][o][p])
                                score = count * validNum
                                print("Score was: {}".format(score))
                            # break
                            elif boardsWon == len(grids):
                                lastGrid = j
                                lastNum = int(i)
                                print("Last Valid Grid: {} @ {}".format(j, i))
                                for q in range(0, len(grids[lastGrid])):
                                    for r in range(0, len(grids[lastGrid][q])):
                                        if grid[lastGrid][q][r] == 0:
                                            count0 += int(grids[lastGrid][q][r])
                                score0 = count0 * lastNum
                                print("Score was: {}".format(score0))
                    elif np.sum(grid90[j, k]) == 5:
                        for s in winningGrids:
                            if s != j:
                                eligible = True
                            else:
                                eligible = False
                                break
                        if eligible:
                            winningGrids.append(j)
                            boardsWon += 1
                            if boardsWon == 1:
                                validGrid = j
                                validNum = int(i)
                                print("Found Valid Grid (90°): {} @ {}".format(j, i))
                                for o in range(0, len(grids[validGrid])):
                                    for p in range(0, len(grids[validGrid][o])):
                                        if grid[validGrid][o][p] == 0:
                                            count += int(grids[validGrid][o][p])
                                score = count * validNum
                                print("Score was: {}".format(score))
                            elif boardsWon == len(grids):
                                lastGrid = j
                                lastNum = int(i)
                                print("Last Valid Grid (90°): {} @ {}".format(j, i))
                                for q in range(0, len(grids[lastGrid])):
                                    for r in range(0, len(grids[lastGrid][q])):
                                        if grid[lastGrid][q][r] == 0:
                                            count0 += int(grids[lastGrid][q][r])
                                score0 = count0 * lastNum
                                print("Score was: {}".format(score0))
