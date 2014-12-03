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



	def changeTurn(self):
		if self.turn==self.player1:
			self.turn=self.player2
		elif self.turn==self.player2:
			self.turn=self.player1
	
	def prompt(self):
		print "It's your move, Player", self.turn
		self.column_to_play=raw_input("Choose a column, Player", self.turn)
		if self.column_to_play < 0 or self.column_to_play > 6 or type(self.column_to_play) != int:
			print "Invalid move. Please pick a column between 0 and 6."
			return self.prompt()

	def isEmpty(self, row, column):
		if self.board[row][column] == " ":
			return True
		else:
			return False




	def getLowestEmptyRowInColumn(self, column):
		'''
		Given a column, returns the row index of the lowest empty square.
		'''
		if self.isEmpty(5, column):
			return 5
		elif self.isEmpty(4, column):
			return 4
		elif self.isEmpty (3, column):
			return 3
		elif self.isEmpty (2, column):
			return 2
		elif self.isEmpty (1, column):
			return 1
		elif self.isEmpty (0, column):
			return 0
		else: # no empty squares in this column
			return None	
				
			


	def placeChecker(self):
		'''
		place a checker unless column is full
		'''
		lowest=self.getLowestEmptyRowInColumn(self.column_to_play)
		if lowest==None:
			print "Sorry, this column is full. Please choose another"
			self.prompt()
		else: 
			self.board[lowest][self.column_to_play] = self.turn

	def game_over(self):
		pass
		#TODO
		#ends game if any player has 4 checkers in a row
		#have to check all cases where this could happen
		

board = Board()
print board.__str__()