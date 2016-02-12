#!/usr/local/bin/python2.7

#function to get the number of hours from the user 
def get_time():
	hours = float(raw_input("How many hours did you work this week?"))
	return hours 
  
#function to get the wage per hour from the user 
def get_wage():
	wage = float(raw_input("How much do you get paid an hour for normal time? (In pounds)"))
	return wage

#calculate earnings 
def calculate_wage(wage,time):
	if time <= 40:
	  	standard_earnings = wage * time
	else:
      		standard_earnings = 40 * wage 
      		overtime_earnings =  (time - 40) * wage * 1.5
    	return standard_earnings, overtime_earnings
    
#dispay calculated values
def display_earnings(standard_earnings,overtime_earnings, time_worked, wage):
  	total_earnings = standard_earnings + overntime_earnings
	print "This week you have a total earnings of £" , total_earnings
  	if overtime == 0: 
   		print "This is made up of:"
    		print "£" , standard_earnings , " standard earnings at £", wage , " for ", time , " hours"
  	else:
	print "This is made up of:"
    	print "£" , standard_earnings , " standard earnings at £", wage , " for 40 hours"
    	print "and"
    	print "£" , overtime_earnings , " overtime earnings at £" , (1.5*wage) , " for ", (time-40) , " hours"

#call the function in the progeram
def main():
  	time = get_time()
  	wage = get_wage()
  	standard_earnings, overtime_earnings = calculate_wage(wage,time)
  	display_earnings(standard_earnings, overtime_earnings, wage, time)
  
  
  
main()
