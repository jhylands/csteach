#function to create base pattern 
def printBasePattern(size):
	#check the size is not less than three
	if size<3:
		#if it is return None and throw an exception
		raise Exception("Error:Size less than three")
		return None
	#inishiate the depth as 0
	depth = 0
	#loop through the lines
	for i in xrange(0,size):
		#create an empty string to concatinate the rest of the line to 
		line = ""
		#loop through each charactor in the line
		for n in xrange(0,size):
			#if an X should be placed
			if n == depth or n == size-depth-1:
				line = line + "x"
			else:
				line = line + "."
		#print the line
		print line
		#if less than half way through increase depth otherwise decrease depth
		if i < round(size/2,0):
			depth += 1
		elif i == float(size)/2:
			depth -= 2
		else:
			depth -= 1

printBasePattern(5)
