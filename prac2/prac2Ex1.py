#!/usr/local/bin/python2.7

#retrive an array of numbers from the user
def get_numbers(number_of_numbers):
  numbers= []
  for x in xrange(0,number_of_numbers):
	numbers.append(int(raw_input("Please enter a number>")))
  return numbers

#finds largest number from a list
def find_max(numbers):
  max_value = numbers[0]
  max_name = 0
  for x in xrange(1,len(numbers)):
    if numbers[x] > max_value:
      max_value = numbers[x]
      max_name = x
  return max_name
  
def main():
    print "You need to enter three numbers:"
    numbers = get_numbers(3)
    max_number = numbers[find_max(numbers)]
    print "The largest of those three numbers was " , max_number
    
main()
