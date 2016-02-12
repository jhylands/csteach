#inishiate the defualt decypher book
decypherbook = {'0000':8, '0001':1, '0010':0, '0011':9,
 '0100':5, '0101':3, '0110':7, '0111':2,
 '1110':4, '1111':6}
#inishiate the default cypher book
cypherbook = {8:'0000', 1:'0001', 0:'0010', 9:'0011',
 5:'0100', 3:'0101', 7:'0110', 2:'0111',
 4:'1110', 6:'1111'}

#function to encode a number
def encode(cypherbook,number):
	#if isinstance(number, type("str")):
	#	raise Exception("Error: number should be string type, " + str(type(number)) + " given")
	#	return none
	#create an empty string to concatinate the result to 
	cypherText = ""
	#loop through each digit converting it
	for digit in number:
		cypherText = cypherText + str(cypherbook[int(digit)])
	return cypherText
#function to decode a binary 
def decode(decypherbook,cypher):
        #if isinstance(cypher, type("str")):
        #        raise Exception("Error: cypher should be string type, " + str(type(cypher)) + " given.")
        #        return none
	plainText = ""
	#loop through the string looking at blocks of 4 charactors
	for x in xrange(0,len(cypher)/4):
		#convert the charactors
		plainText = plainText + str(decypherbook[cypher[4*x:4*x+4]])
	return plainText

#flip the dictionary so the names become the data and the data becomes the names
def flipDic(dictionary):
	try:
		flipped =  dict((v,k) for k, v in dictionary.iteritems())
	except:
		print "Error encoder not injective!"
		flipped = none
	return flipped


#function that takes the cypherbook and uses it to decode a cypher
def advancedDecode(cypherbook,cypher):	
	#flip the cypher dictionay and then use the standard decode function
	return decode(flipDic(cypherbook),cypher)
	
