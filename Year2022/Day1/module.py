with open("Year2022/Day1/data", "r") as file:
    raw_data = file.readlines()
    raw_data = "".join(raw_data)

current_lines = []
all_lines = []
current = ""
for character in raw_data:
    if character == "\n":
        if current == "":
            all_lines.append(sum(current_lines))
            current_lines = []
            current = ""
        else:
            current_lines.append(int(current))
            current = ""
    else:
        current += character

print(max(all_lines))
print(sum(sorted(all_lines)[-3:]))
