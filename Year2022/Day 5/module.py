import re

cargo_string = \
"""                [V]     [C]     [M]
[V]     [J]     [N]     [H]     [V]
[R] [F] [N]     [W]     [Z]     [N]
[H] [R] [D]     [Q] [M] [L]     [B]
[B] [C] [H] [V] [R] [C] [G]     [R]
[G] [G] [F] [S] [D] [H] [B] [R] [S]
[D] [N] [S] [D] [H] [G] [J] [J] [G]
[W] [J] [L] [J] [S] [P] [F] [S] [L]
 1   2   3   4   5   6   7   8   9 """

with open("Year2022/Day 5/data", "r") as file:
    raw_data = file.readlines()

data: list = [re.findall("\d+", i) for i in raw_data]

cargo_width = int(cargo_string[-2])
cargo_height = len(cargo_string.splitlines())
cargo = [[[""] * cargo_width] * cargo_height]

x, y = 0, 0

for i in range(1, len(cargo_string) - (cargo_width * 4), 4):

    cargo = cargo_string[i]