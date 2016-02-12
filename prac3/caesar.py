def caesar_encrypt(word, shift):
    encrypted = ""
    for charactor in word:
        if ord(charactor)>=97 and ord(charactor)<= 122:
            encrypted = encrypted + chr(((ord(charactor)-97+shift) %26)+97)
        else:
            encrypted = encrypted + charactor
    return encrypted

def caesar_decrypt(word,shift):
    return caesar_encrypt(word,(shift*-1))

def get_word():
    word = raw_input("Please enter the text you would like to encrypt/decrypt")
    return word

def get_shift():
    shift = int(raw_input("Please enter the shift"))
    return shift

def main():
    print "Please type the number of the option you would like to use"
    print "1. encrypt"
    print "2. decrypt"
    option = raw_input("")
    if option == "1":
        word = get_word()
        shift = get_shift()
        print caesar_encrypt(word,shift)
    elif option == "2":
        word = get_word()
        shift = get_shift()
        print caesar_decrypt(word,shift)
    else:
        print "Option not understood"

main()
