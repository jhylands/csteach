import sys
def palindrome(word):
	if len(word) <2:
		return True
	else:
		#check first and last values
		if word[0] == word[-1]:
			#if they are the same check the next two
			if palindrome(word[1:-1]):
				return True
			else:
				return False
		else:
			return False

def clean_word(word):
	word = word.lower()
	str_clean_word = ""
	for charactor in word:
		if charactor.isalpha():
			str_clean_word = str(str_clean_word) + str(charactor)
	return str_clean_word

def get_word():
	word = raw_input("Please enter a word to check if it is a palindrome")
	return word


        
word = clean_word(get_word())

sys.setrecursionlimit(len(word)/2+5)
if palindrome(word):
        print word , " is a palindrome"
else:
        print word , " is not a palindrome"

sys.setrecursionlimit(2000)
