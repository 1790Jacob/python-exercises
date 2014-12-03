# mutable version - make one board, that board gets changed as the game goes along
class Board:
	def __init__(self):
		self.height=6
		self.width=7
		self.player1 = 'X'
		self.player2 = 'O'
		self.board = [[" " for i in range(self.width)] for j in range(self.height)] #represent board array as a list of lists
		self.turn = self.player1
		self.column_to_play = None

	def __str__(self):
		rows = [str(x) + " " + self.board[x][0] + " " + self.board[x][1] + " "  + self.board[x][2] + " "  + self.board[x][3] + " "  + self.board[x][4] + " "  + self.board[x][5] + " "  + self.board[x][6] + " \n" for x in range(self.height)]
		return "\n  0 1 2 3 4 5 6\n"+rows[0]+rows[1]+rows[2]+rows[3]+rows[4]+rows[5] + "\n"

	def __repr__(self):
		return self.__str__()

	def whoseTurn(self):
		return self.turn

	def changeTurn(self):
		if self.turn==self.player1:
			self.turn=self.player2
		elif self.turn==self.player2:
			self.turn=self.player1
	
	def prompt(self):
		print "It's your move, Player", self.turn
		self.column_to_play=raw_input("Choose a column, Player", self.turn)
		if self.column_to_play < 0 or self.column_to_play > 6:
			print "Invalid move. Please pick a column between 0 and 6."
			return self.prompt()

	def isEmpty(self, row, column):
		if checker_positions[row][column] == " ":
			return True
		else:
			return False




	def getLowestEmptySquareInColumn(self, column):
		pass
		# TODO
		# so given a column, find the lowest square in self.board which is " "
		# ie for column 3 
		# check self.board[5][3], then self.board[4][3], then self.board[3][3], and so on until you find an empty square
		# return None if there are no empty squares in given column
		


	def placeChecker(self):
		lowest=self.getLowestEmptySquareInColumn(self.column_to_play)
		if lowest==None:
			print "There are no empty spots in that column"
			self.prompt()
		else: 
			lowest=self.turn

	def game_over(self):
		pass
		#TODO
		#ends game if any player has 4 checkers in a row
		#have to check all cases where this could happen
		

board = Board()
print board.__str__()