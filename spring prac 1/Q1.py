'''
Created on 14 Jan 2015

@author: jhh521
'''
def print_board_boarder(size):
    print "+" + "-"*(2*size) + "+"
        
def print_chessboard(size):
    print_board_boarder(size)
    for n in xrange(0,size):
        holder = "+"
        for i in xrange(0,size):
            if (i % 2 == 0) == (n % 2 == 0):
                holder = holder + "##"
            else:
                holder = holder + "  "
        print holder + "+"
        print holder + "+"
    print_board_boarder(size)

print_chessboard(33)
