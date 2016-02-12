rice = 1
total = 0
for i in range(0,8):
	for n in range(0,8):
		print "In square: " , i , "," , n , " the mass of rice is " , rice * 0.03 , "grams"
		rice = rice * 2
		total = total + rice
print "Thats " , total * 0.03 , "grams in total"
