sampleText = ("As Python's creator, I'd like to say a few words about its "+
              "origins, adding a bit of personal philosophy.\n"+
              "Over six years ago, in December 1989, I was looking for a "+
              "'hobby' programming project that would keep me occupied "+
              "during the week around Christmas. My office "+
              "(a government-run research lab in Amsterdam) would be closed, "+
              "but I had a home computer, and not much else on my hands. "+
              "I decided to write an interpreter for the new scripting "+
              "language I had been thinking about lately: a descendant of ABC "+
              "that would appeal to Unix/C hackers. I chose Python as a "+
              "working title for the project, being in a slightly irreverent "+
              "mood (and a big fan of Monty Python's Flying Circus).")

#######################################################
##
##               CODE for QUESTION 1 - 4 
##
#######################################################

## Please write your code here, watch for your indentation
#function to remove the return \n
def remret(string):
    for i in xrange(0,len(string)-1):
            if string[i:i+1] == "\n":
                string = string[0:i] + " " + string[i+1:]
    return string

def splitText(text):
    text = remret(text)
    array = []
    carry = ""
    for charactor in text:
        if charactor == " " or charactor == "'":
            if len(carry)>0:
                array.append(carry)
                carry = ""
        elif charactor == "." or charactor == "(" or charactor == ")":
            pass
        else:
            carry = carry + charactor
    array.append(carry)
    return array


def getWordsStartingWith(text, letter):
    words = []
    for word in splitText(text):
        lowerWord = word.lower()
        if lowerWord[0:1] == letter.lower():
            words.append(lowerWord)
    return words

def getUniqueWordsStartingWith(text, letter):
        return list(set(getWordsStartingWith(text,letter)))

def printWordsFrequency(text):
        words = splitText(text.lower())
        wordDictionary = {}
        #inishiate each element of the dictionary 
        for word in list(set(words)):
            wordDictionary[word] = 0
        #count each words occurance
        for word in words:
                wordDictionary[word] +=1
        return wordDictionary

#get number of words in text 
def numberOfWords(text):
    return len(splitText(text))

def averageWordLength(text):
    words = splitText(text)
    total = 0
    count = len(words)
    for word in words:
            total += len(word)
    return total/count
def howManyWordsOfLength(text,length):
    words = splitText(text)
    count = 0
    for word in words:
        if len(word) == length:
            count +=1
    return count


def getFileLocation():
    location = raw_input("Please eneter the file location>")
    return location
def importText():
    location = getFileLocation()
    f = file(location,"r")
    return f.read()

