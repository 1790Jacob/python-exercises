# height + width
# immutability
# When the board changes, it will become a new board.
class Board:
	def __init__(self, height, width, checker_position, turn, number_of_checkers):
		self.height=height
		self.width=width
		self.checker_position=checker_position
		self.turn=turn
		self.number_of_checkers=number_of_checkers
		