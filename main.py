import sys

arg = sys.argv
arg.pop(0)

if len(arg) == 1:
    date = str(arg[0]).split("/")
    year = date[0]
    day = date[1]
elif len(arg) > 1:
    print("Only one argument needed")
    sys.exit()
else:
    year = input("Input year: ")
    day = input("Input day number: ")

location = f"Year{year}/Day{day}/module.py"
exec(open(location).read())
