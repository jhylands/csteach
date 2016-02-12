def get_vector(dimentions):
	vector = []
	for x in xrange(0,dimentions):
		vector.append(float(raw_input("Please enter the value corrisponding to dimention " + str(x) + " of the vector")))
	return vector

def get_scalar():
	scalar = float(raw_input("Please enter a scalar value."))
	return scalar

def get_dimentions():
	dimentions = int(raw_input("Please enter the number of dimentions you want the vectors to be."))
	return dimentions

def add_vectors(a,b):
	c = []
	if len(a) == len(b):
		for x in xrange(0,len(a)):
			c.append(float(a[x])+float(b[x]))
		return c
	else:
		return False

def scalar_product(scalar, vector):
	new_vector = []
	for x in vector:
		new_vector.append(float(scalar*x))
	return new_vector


def main():
	print "Please use one of the following operations..."
	print "1. Add two vectors"
	print "2. Multiply a vector by a scalor"
	opperation = raw_input("")
	if opperation == "1":
		dimention = get_dimentions()
		vector1 = get_vector(dimention)
		vector2 = get_vector(dimention)
		print add_vectors(vector1,vector2)
	elif opperation == "2":
		dimention = get_dimentions()
		scalar = get_scalar()
		vector = get_vector(dimention)
		print scalar_product(scalar,vector)
	else:
		print "Command not recognised program terminated"
main()
