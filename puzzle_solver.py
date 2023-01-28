import puzzle as pz

# magic numbers for decide_puzzle
WORDS_IN_PLUS_MINUS = 4
FIRST_WORD_IN_MULTIPLICATION = 0
LAST_WORD_IN_MULTIPLICATION = -1

def decide_puzzle(words: list[str]) -> pz.Puzzle:
	# plus_minus is the shorter puzzle in a manner of number of words.
	# multiplication is currently the only puzzle that its first word is shorter then its last word.
	if len(words) == WORDS_IN_PLUS_MINUS:
		return pz.PlusMinus(words)
	elif len(words[FIRST_WORD_IN_MULTIPLICATION]) < \
		 len(words[LAST_WORD_IN_MULTIPLICATION]):
		return pz.Multiplication(words)
	else:
		return pz.Division(words)

class PuzzleSolver:
	def __init__(self, words: list[str]):
		self.puzzle = decide_puzzle(words)
		self.name = self.puzzle.name

	def solve(self):
		self.puzzle.solve()
		self.solution = self.puzzle.solution

	def print(self):
		self.puzzle.print()

	def solve_with_prints(self):
		self.print()
		self.solve()
		self.print()