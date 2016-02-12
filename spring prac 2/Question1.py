def create_board(size):
    for n in xrange(0,size):
        holderA = ""
        holderB = ""
        for i in xrange(0,size):
            if (i % 2 == 0) == (n % 2 == 0):
                holderA = holderA + "1.1.1"
                holderB = holderB + "1.1.1"
            else:
                holderA = holderA + "..."
                holderB = holderB + "---"
        for x in xrange(0,2):
            print holderA
            print holderB
create_board(5)