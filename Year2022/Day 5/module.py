import re


def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

cargo_string = \
"""                [V]     [C]     [M]
[V]     [J]     [N]     [H]     [V]
[R] [F] [N]     [W]     [Z]     [N]
[H] [R] [D]     [Q] [M] [L]     [B]
[B] [C] [H] [V] [R] [C] [G]     [R]
[G] [G] [F] [S] [D] [H] [B] [R] [S]
[D] [N] [S] [D] [H] [G] [J] [J] [G]
[W] [J] [L] [J] [S] [P] [F] [S] [L]
 1   2   3   4   5   6   7   8   9 
"""

with open("Year2022/Day 5/data", "r") as file:
    raw_data = file.readlines()

data = [re.findall("\d+", i) for i in raw_data]

cargo_width = int(cargo_string[-2])
cargo_height = len(cargo_string.splitlines())
cargo = []
x = 0
current = []
for i in range(1, len(cargo_string) - (cargo_width * 4), 4):
    current.append(cargo_string[i])
    x += 1
    if x >= cargo_width:
        x = 0
        cargo.append(current)
        current = []

cargo = rotated(cargo)

cargo = [[i for i in item if i != ' '] for item in cargo]
print(cargo)

for i in data:
    y = int(i[1]) - 1
    x = int(i[0])
    new_y = int(i[2]) - 1
    exctracted = cargo[y][-x:]
    cargo[new_y] += exctracted
    del cargo[y][-x:]

final = ""
for i in cargo:
    final = final + i[-1]

print(final)
