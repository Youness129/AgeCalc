def printWithFor(text):
	import sys
	import time
	speed = 0.1
	print()
	for char in text:
	    sys.stdout.write(char)
	    sys.stdout.flush()
	    time.sleep(speed)
	print()
def ageCalculator(y, m, d):
	import datetime
	today = datetime.datetime.now().date()
	dob = datetime.date(y, m, d)
	age = int((today-dob).days / 365.25)
	printWithFor(f"your age is \033[1;32m{age}\033[0;29m")

year, month, day = int(input("year : ")), int(input("month: ")), int(input("day  : "))
ageCalculator(year, month, day)