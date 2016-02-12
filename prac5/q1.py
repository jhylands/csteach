def file_to_list(location):
        f = open(location)
        #read the lines of the file to a list 
        lines = f.readlines()
        f.close()
        return lines

#function to convert a csv file to list
#function removes comments but not column headers
def csv_to_list(location):
    #define the list
    arrList = []
    #get the lines of the file
    lines = file_to_list(location)
    #for each line of the file if the line is not a comment then split it by comma and add that to an element of the list
    for line in lines:
        if line[0:2] != "##":
            #not a comment so add to the array
            arrList.append((line.rstrip('\n')).split(","))
    return arrList


def average_Percipitation(dataLocation):
        data = csv_to_list(dataLocation)
        total = float(0)
        number = 0
        for year in data:
            total = total + float(year[1])
            number +=1
        return float(total)/float(number)

#returns maxpercipitation, year
def max_Percipitation(dataLocation):
    data = csv_to_list(dataLocation)
    maxLoc = 0
    maxVal = data[0][1]
    for x in xrange(1,len(data)):
        if data[x][1]>maxVal:
            maxLoc = x
            maxVal = data[x][1]
    return maxVal , data[maxLoc][0]

#returns minpercipitation, year
def min_Percipitation(dataLocation):
    data = csv_to_list(dataLocation)
    print data
    minLoc = 0
    minVal = data[0][1]
    for x in xrange(1,len(data)):
        if data[x][1]<minVal:
            minLoc = x
            minVal = data[x][1]
    return minVal , data[minLoc][0]

def collatePercipitationFile(fileNames,outputFile):
        tdata = []
        fdata = []
        data = []
        endform = {}
        for fileName in fileNames:
                #data.append(csv_to_list(fileName))
                data = csv_to_list(fileName)
                tdata.append(data)
                #print data
                ##for row in data:
                ##    if not row[0] in endform:
                ##        endform[int(row[0])] = {fileName:row[1]}
                ##    else:
                ##        endform[int(row[0])][fileName] = row[1]
        #data = year, location, location
         #           data

        #print tdata
        fdata = zip(*tdata)
        
        #data = [['Year'] + fileNames]
    #    for year in endform:
     #       smallList = ['
        print fdata

names = ['Data/precipitations-Europe.txt','Data/precipitations-NAmerica.txt','Data/precipitations-world.txt']
        
