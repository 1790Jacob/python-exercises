# TIC TAC TOE

class Board:
	def __init__(self):
		self.player1="X"
		self.player2="O"
		self.turn=self.player1
		self.height=3 
		self.length=3
		self.board = [[" " for i in range(self.length)] for j in range(self.height)]
		
	def __str__(self):
		column_labels = "       0     1     2\n\n"
		vertical = "          |     |\n"
		horizontal = "     -----------------\n"
		top_row = "0      " + self.board[0][0] + "  |  " + self.board[0][1] + "  |  " + self.board[0][2] + " \n"
		middle_row = "1      " + self.board[1][0] + "  |  " + self.board[1][1] + "  |  " + self.board[1][2] + " \n"
		bottom_row = "2      " + self.board[2][0] + "  |  " + self.board[2][1] + "  |  " + self.board[2][2] +" \n"
		return "\n" + column_labels + vertical + top_row + vertical + horizontal + vertical + middle_row + vertical + horizontal + vertical + bottom_row + vertical 

	def __repr__(self):
		return self.__str__()

	def prompt(self):
		print "\n========================================\n     It's your turn, " + self.Whose_Turn() + "\n========================================"
		print self.__str__()
		row = int(raw_input("Specify which row you want to move in. "))
		column = int(raw_input("Specify which column you want to move in. "))
		if self.invalid_move(row, column, self.Whose_Turn()): # if invalid move
			return self.prompt() # prompt again
		else:
			self.move(row, column, self.Whose_Turn())

	def is_winner(self, player):
	    # Given the board and a player, this function returns True if that player has won.
	    return ((self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player) or # across the top
	    (self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player) or # across the middle
	    (self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player) or # across the bottom
	    (self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player) or # down the left side
	    (self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player) or # down the middle
	    (self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player) or # down the right side
	    (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player) or # diagonal
	    (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player)) # diagonal

	def game_over(self):
		return self.is_winner(self.player1) or self.is_winner(self.player2)

	def who_won(self):
		if self.is_winner(self.player1):
			return self.player1
		if self.is_winner(self.player2):
			return self.player2

	def invalid_move(self, row, column, player):
		if row < 0 or row > 2 or column < 0 or column > 2:
			print "Invalid Move. Try again."
			return True
		elif self.board[row][column] != " ":
			print "Spot already taken. Try again."
			return True
		else:
			return False

	def move(self, row, column, player):
		self.board[row][column]=player
		return self.__str__()

	def change_turn(self):
		if self.turn==self.player1:
			self.turn=self.player2
		elif self.turn==self.player2:
			self.turn=self.player1

	def Whose_Turn(self):
		return self.turn



playing_board = Board() # make a board
game_in_progress = True # variable for whether game is over yet or not
while game_in_progress:
	playing_board.prompt()
	playing_board.change_turn()
	if playing_board.game_over():
		print playing_board.__str__()
		print "Game Over. " + playing_board.who_won() + " is the winner."
		game_in_progress = False
