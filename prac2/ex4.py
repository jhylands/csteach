def get_year():
	year = int(raw_input("Please enter the year you wish to check."))
	return year 
#if a is devisible by b
def dvsbl(a,b):
	return a%b ==0

def is_leap_year(year):
	if dvsbl(year,4) and not  dvsbl(year,100) or dvsbl(year,400):
		return True
	else:
		return False

def main():
	year = get_year()
	if is_leap_year(year):
		print year , " is a leap year!"
	else:
		print year , " is not a leap year!"

main()
