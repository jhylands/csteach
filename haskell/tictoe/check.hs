checkRow board row = (board[row][0]==board[row][1]) && (board[row][1] == board[row][2])
checkColumn board column = (board[0][column]==board[1][column]) && (board[1][column] == board[2][column])
checkDiagonal board = (board[0][0]==board[1][1] && board[1][1]==board[2][2]) || (board[0][2]==board[1][1] && board[1][1]==board[2][0])

hasWon board = or ([(checkRow board x || checkColumn board x) | x <- [0..2]] )
