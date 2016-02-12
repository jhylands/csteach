player1 board = if hasWon update board move 'X' then board else player2 update board 
	where move <- getLine

player2 board = if hasWon update board move 'O' then board else player1 update board 
	where move <- getLine

update :: [[Char]] -> Int -> [[Char]]
update board move token= board 
      where board!!move=token


main main= if(hasWon) putStrLine "We have a winner" else main

player1 board= do 
	print board
	putStrLine "Enter coordinates:"
	x :: int
	y :: int
	putStrLine "x:"
	x <- getLine
	putStrLine "y:"
	y <- getLine
	board = move board x y

move board x y = if board[x][y]=="-" then 
	
