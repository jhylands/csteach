player1 board = if hasWon b then return b else return player2 b
		where
		b = player1'sGo
	
player1'sGo b = 7

hasWon b = True
