day = input("Input day number: ")
location = "Day{}/module.py".format(day)

exec(open(location).read())
