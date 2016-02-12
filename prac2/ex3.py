def get_speed():
	speed = int(raw_input("What was the vehicle's speed? (mph)"))
	return speed

def get_limit():
	limit = int(raw_input("What was the speed limit in that location? (mph)"))
	return limit

def get_standard_fine(speed,limit):
	if speed > limit:
		return 100
	else:
		return 0

def get_over_fine(speed,limit):
	return (speed-limit)*5
def get_high_speed_fine(speed):
	if speed > 90:
		return 200
	else:
		return 0
def get_fine(speed, limit):
	standard_fine = get_standard_fine(speed,limit)
	if standard_fine:
		over_fine = get_over_fine(speed,limit)
		high_speed_fine = get_high_speed_fine(speed)
	total_fine = standard_fine + over_fine + high_speed_fine
	return total_fine
def main():
	limit = get_limit()
	speed = get_speed()
	fine = get_fine(speed,limit)
	if fine:
		print "You have been fined: " , fine , " Your speed was illegal"
	else:
		print "The speed was legal"

main()
