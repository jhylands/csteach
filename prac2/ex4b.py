import calendar
def get_date():
	date = raw_input("Please eneter a date DD/MM/YYYY")
	dates = date.split("/")
	if len(dates) == 3:
		return map(int,dates)
	else:
		return none

def check_month(date):
	return date[1] <= 12 and date[1] > 0
def check_day(date):
	return date[0]>0 and date[0] <= calendar.monthrange(date[2],date[1])[1]
def main():
	date = get_date()
	if check_month(date) and check_day(date):
		print "Valid date"
	else:
		print "Date Invalid!"
main()
