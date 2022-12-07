with open("Year2022/Day7/data") as file:
    data = file.readlines()[1:]

dirs = {}

total_files = 0
closest_num = 9999999999999999

prev_dirs = []
cur_dir = dirs
for line in data:
    words = line.split(" ")
    if "cd" == words[1]:
        if "..\n" == words[2]:
            cur_dir = prev_dirs[-1]
            prev_dirs.pop(-1)
            continue
        else:
            prev_dirs.append(cur_dir)
            cur_dir = cur_dir[line[5:].rstrip()]
    if "dir" == words[0]:
        cur_dir[words[1].rstrip()] = {}
    if words[0][0].isdigit():
        cur_dir[words[1].rstrip()] = int(words[0])

def get_sum(file):
    global total_files
    global closest_num
    if type(file) == int:
        return file
    if type(file) == dict:
        total = 0
        for key in file:
            total += get_sum(file[key])
        if total <= 100000:
            total_files += total
        try:
            if total >= total_needed and total < closest_num:
                closest_num = total
        except NameError:
            pass
        return total
                
total_used = get_sum(dirs)
total_needed = total_used - (70000000 - 30000000)
print(total_files)
get_sum(dirs)
print(closest_num)
