import sys

arg = sys.argv
arg.pop(0)

if len(arg) == 1:
    day = str(arg[0])
elif len(arg) > 1:
    print("Only one argument needed")
    sys.exit()
else:
    day = input("Input day number: ")

location = "Day{}/module.py".format(day)
exec(open(location).read())
