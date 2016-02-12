def matrixSize(matrix):
        print "Size:, " + str(len(matrix)) + "x" + str(len(matrix[0]))

def addMatrix(a,b):
    c = []
    for n in xrange(0,len(a)):
        c.append([])
        for i in xrange(0,len(b)):
            c[n].append(a[n][i] + b[n][i])
    return c
def T(a):
    c = []
    for i in xrange(0,len(a[0])):
        c.append([])
        for n in xrange(0,len(a)):
            c[i].append(a[n][i])
    return c
