# default board dimensions are 7 columns and 6 rows
# MUTABLE version

#INITIALIZE BOARD
# every square is 0 to start
rows = ["A", "B", "C", "D", "E", "F"]
columns = ["1", "2", "3", "4", "5", "6", "7"]
squares = [i + j for i in rows for j in columns]
checker_positions = {s:0 for s in squares}


class Board:
	def __init__(self, checker_positions, turn, number_of_checkers, height=6, width=7):
		self.height=height
		self.width=width
		self.checker_positions=checker_positions
		self.turn=turn
		self.number_of_checkers=number_of_checkers
		self.column_to_play = None

	def __str__(self):
		""" Return a string representation of this board """
		board_symbol_mapping = { 0: ' ', 1: 'X', 2: 'O' }
		retVal = [ "  " + ' '.join([str(x) for x in range(self.width)]) ]
		retVal += [ str(i) + ' ' + ' '.join([self.board_symbol_mapping[x] for x in row]) for i, row in enumerate(self.checker_positions) ]
		return '\n' + '\n'.join(retVal) + '\n'

	def __repr__(self):
		""" The string representation of a board in the Python shell """
		return self.__str__()

	def getHeight(self):
		return self.height

	def getWidth(self):
		return self.width



#represent board array as a list of lists
	def whoseTurn(self):
		return self.turn

	def changeTurn(self):
		if self.turn==1:
			self.turn=2
		elif self.turn==2:
			self.turn=1
	
	def prompt(self):
		print "It's your move, Player", self.turn
		self.column_to_play=raw_input("Choose a column, Player", self.turn)

	def isEmpty(self, square):
		if checker_positions[square] == 0:
			return True
		else:
			return False

	def getLowestEmptySquareInColumn(self):
		
		#TODO
		# delete pass
		# if self.column_to_play==7:
		# if self.isEmpty("A7"):


	def placeChecker(self):
		lowest=self.getLowestEmptySquareInColumn(self.column_to_play)
		if lowest==None:
			print "There are no empty spots in that column"
			self.prompt()
		else: lowest=self.turn

	def game_over(self):
		#TODO
		#ends game if any player has 4 checkers in a row
