with open("data") as file:
    data = file.readlines()[1:]

dirs = {}

cur_dir_name = ""
for line in data:
    if "cd" in line:
        if ".." in line:
            continue
        else:
            dirs[line[5:]] = []