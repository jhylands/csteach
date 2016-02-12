#function to print patern 
def printMultipleBasePattern(row,column):
	if row > 0 and column > 0:
		raise Exception("Error: row or column less than or equal to zero")
		return none
	#define the layers of the patern
	pattern = ['O--O','-OO-','-OO-','O--O']
	#loop through each vertical repeat of the patter
	for i in xrange(0,row):
		#loop through each line of a particular repeat of the pattern
		for lineNo in xrange(0,4):
			#create an empty string to concatinate patterns to 
			line = ""
			#loop through each pattern repeat within a line
			for n in xrange(0,column):
				line = line + pattern[lineNo]
			#print the line
			print line


printMultipleBasePattern(2,3)
