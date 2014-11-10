# default board dimensions are 7 columns and 6 rows
# MUTABLE version

board_symbol_mapping = { 0: ' ', 1: 'X', 2: 'O' }

class Board:
	def __init__(self, height=6, width=7, checker_positions, turn, number_of_checkers):
		self.height=height
		self.width=width
		self.checker_positions=checker_positions
		self.turn=turn
		self.number_of_checkers=number_of_checkers

	def __str__(self):
        """ Return a string representation of this board """
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
