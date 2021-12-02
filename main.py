import subprocess

day = input("Input day number: ")
location = "Day{}/module.py".format(day)

subprocess.call(["python", location])