# Puzzle class declaration for allow use it inside Solver and Printer classes
class Puzzle():
	words : list[str]
	lens : list[int]
	is_x : bool
	solution : list[str]
	missing_num : int
	range_i : int
	range_j : int
	def init_nums(self, i: int, j: int) -> list[str]:
		pass
	def add_spaces(self, lines: list[str]) -> list[str]:
		pass
	def add_underscore(self, lines: list[str]) -> list[str]:
		pass
	pass


class Solver():
	def solve(self, puzzle: Puzzle):
		for i in self.range_by_order(puzzle.lens[puzzle.range_i]):
			for j in self.range_by_order(puzzle.lens[puzzle.range_j]):
				nums = puzzle.init_nums(i, j)

				if not self.is_same_length(nums, puzzle.words):
					continue

				if self.is_follows_pattern(nums, puzzle.words, puzzle.is_x):
					# 45 is the sum of all digits in base 10. the missing one can be found by
					# substracting the sum of all the digits that participate in the solution.
					puzzle.missing_num = 45 - sum(map(int, list(set("".join(nums)))))
					puzzle.solution = nums

					return

	def range_by_order(self, order: int) -> range:
		start = int(10 ** (order - 1))

		return range(start, start * 10)

	def is_same_length(self, nums: list[str], words: list[str]) -> bool:
		for (num, word) in zip(nums, words):
			if not len(num) == len(word):
				return False

		return True

	def is_follows_pattern(self, nums: list[str], words: list[str], is_x: bool) -> bool:
		concat_nums, concat_words = self.concat_nums_and_words(nums, words)
		ret_val = ((len(concat_nums) == len(concat_words)) and\
				self.is_l1_follows_l2(concat_words, concat_nums, is_x))

		if not is_x:
			ret_val = (ret_val and self.is_l1_follows_l2(concat_nums, concat_words, is_x))

		return ret_val

	def is_l1_follows_l2(self, l1: str, l2: str, is_x: bool) -> bool:
		mapping = {}

		for (i1, i2) in zip(l1, l2):
			if i2 not in mapping:
				mapping[i2] = i1
			elif mapping[i2] != i1:
				return False

		if is_x:
			if not list(mapping.values()).count("x") == 1 or (not len(mapping.values()) == 9):
				return False

		return True

	def concat_nums_and_words(self, nums: list[str], words: list[str]) -> tuple[str, str]:
		concat_nums = ""
		concat_words = ""

		for (num, word) in zip(nums, words):
			if not len(num) == len(word):
				# The return values' length compared against each other. So this return value is
				# equivalent to False.
				return ("12", "1")

			concat_nums += num
			concat_words += word

		return concat_nums, concat_words

	def order_of_number(self, num: int) -> int:
		return len(str(num))

	# An helper method to help Division handle with partial dividees.
	def minimum_dividee(self, num: int, divider: int) -> int:
		if num < divider:
			return 0

		divider_order = self.order_of_number(divider)
		num_order = self.order_of_number(num)
		ret_val = int(num / int(10 ** (num_order - divider_order)))

		if ret_val < divider:
			ret_val = int(num / int(10 ** (num_order - divider_order - 1)))

		return ret_val

	# Each puzzle defines by itself how 2 iterable numbers create the rest of the puzzle's numbers.
	def init_nums(self, puzzle: Puzzle, i: int, j: int) -> list[str]:
		pass


class Printer():
	def print(self, puzzle: Puzzle):
		# print method behave a bit different if called before the solve or after.
		# If before, it prints puzzle's name and prints the words. If after prints the solution.
		is_before = (len(puzzle.solution) == 0)
		if is_before:
			print(puzzle.__class__.__name__ + ("_x" if puzzle.is_x else "") + "\n")
		lines_to_print = (list(puzzle.words if is_before else puzzle.solution)).copy()
		lines_to_print = puzzle.add_spaces(lines_to_print)
		lines_to_print = puzzle.add_underscore(lines_to_print)
		self.add_missing_number(lines_to_print, puzzle, is_before)
		self.print_lines(lines_to_print)

	def add_missing_number(self, lines: list[str], puzzle: Puzzle, is_before: bool):
		if is_before:
			lines.append("")
		else:
			lines.append("\nmissing number is:" + str(puzzle.missing_num))

	def print_lines(self, lines: list[str]):
		for line in lines:
			print(line)

	# Helper methods to help virtual methods.
	def under_score(self, text: str) -> str:
		return "\033[4m"+text+"\033[0m"

	def spaces(self, num_of_spaces: int) -> str:
		return " " * num_of_spaces

	# Virtual methods that get the lines that later will be printed and modify them to look like the
	# original puzzle.
	def add_spaces(self, lines: list[str]) -> list[str]:
		pass

	def add_underscore(self, lines: list[str]) -> list[str]:
		pass


class Puzzle():
	def __init__(self, words: list[str], range_i: int=0, range_j: int=1):
		self.is_x = words[0][0] in ["x", "-"]
		self.words = words if self.is_x else list(word[::-1] for word in words)
		self.solver = Solver()
		self.printer = Printer()
		self.lens = list((len(word) for word in words))
		self.solution = []
		self.range_i = range_i
		self.range_j = range_j
		self.name = self.__class__.__name__ + ("_x" if self.is_x else "")

	def print(self):
		self.printer.print(self)

	def solve(self):
		self.solver.solve(self)


class PlusMinus(Puzzle):
	def __init__(self, words: list[str]):
		super().__init__(words, 2, 3)

	# [sum, num1, num2, diff]: init_nums gets (num2, diff) and returns the rest.
	def init_nums(self, i: int, j: int) -> list[str]:
		return [str(i + j + i), str(i + j), str(i), str(j)]

	def add_spaces(self, lines: list[str]) -> list[str]:
		for i in range(1, 4):
			lines[i] = self.printer.spaces(self.lens[0] - self.lens[i]) + lines[i]
		return lines

	def add_underscore(self, lines: list[str]) -> list[str]:
		lines[0] = self.printer.under_score(lines[0])
		lines[2] = self.printer.under_score(lines[2])

		return lines


class Multiplication(Puzzle):
	def __init__(self, words: list[str]):
		super().__init__(words)
	# words[i, j, [a, b, c, ...], p] -> [a, b, c, ...]: are the partial productions.
	def init_nums(self, i: int, j: int) -> list[str]:
		nums = [str(i), str(j)]
		j_to_str = str(j)

		for k in range(self.lens[1]):
			nums.append(str(i * int(j_to_str[- 1 -k])))

		nums.append(str(i * j))

		return nums

	def add_spaces(self, lines: list[str]) -> list[str]:
		longest = self.lens[-1]

		for i in range(2):
			lines[i] = self.printer.spaces(longest - self.lens[i]) + lines[i]

		for i in range(2, len(lines) - 1):
			lines[i] = self.printer.spaces(longest - self.lens[i] - i + 2) + lines[i]

		return lines

	def add_underscore(self, lines: list[str]) -> list[str]:
		longest = self.lens[-1]
		start_num1 = longest - self.lens[0]
		start_num_2 = longest - self.lens[-2]
		lines[1] = lines[1][:start_num1] + self.printer.under_score(lines[1][start_num1:])
		lines[-2] = self.printer.under_score(lines[-2] + self.printer.spaces(start_num_2))

		return lines


class Division(Puzzle):
	def __init__(self, words: list[str]):
		super().__init__(words)

	# [i, j, q, m, [mid_dividers]]
	def init_nums(self, i: int, j: int) -> list[str]:
		q = (int)(i / j)
		m = i % j
		nums = [str(i), str(j), str(q), str(m)]
		num_of_iterations = int((len(self.words) - 3) / 2)
		dividee = i

		for k in range(num_of_iterations):
			min_dividee = self.solver.minimum_dividee(dividee, j)

			if k > 0:
				nums.append(str(min_dividee))

			power = self.solver.order_of_number(dividee)
			power -= self.solver.order_of_number(min_dividee)
			rest = dividee % (10 ** power)
			substractor = j * int(min_dividee / j)
			nums.append(str(substractor))
			power = self.solver.order_of_number(rest)
			dividee = (min_dividee - substractor) * (10 ** power) + rest

		return nums

	def add_spaces(self, lines: list[str]) -> list[str]:
		new_lines = []
		line0_spaces = max(self.lens[2] - self.lens[1], 0)
		new_lines.append(lines[0] + "|" + self.printer.spaces(line0_spaces) + lines[1])
		line1_spaces = len(new_lines[0]) - self.lens[4] - self.lens[2]
		new_lines.append(lines[4] + self.printer.spaces(line1_spaces) + lines[2])
		intermediate = int((len(self.lens) - 3) / 2) - 1

		for i in range(intermediate):
			num_of_spaces = self.lens[0] - self.lens[(i * 2) + 5] - (intermediate - i - 1)
			new_lines.append(self.printer.spaces(num_of_spaces) + lines[(i * 2) + 5])
			line_to_space = self.lens[(i * 2) + 5] - self.lens[(i * 2) + 6]
			under_scored = self.printer.spaces(line_to_space) + lines[(i * 2) + 6]
			new_lines.append(self.printer.spaces(num_of_spaces) + under_scored)

		new_lines.append(self.printer.spaces(self.lens[0] - self.lens[3]) + lines[3])

		return new_lines

	def add_underscore(self, lines: list[str]) -> list[str]:
		# lines 0, 1 need a special treatment.
		line0_underscored_part = self.printer.under_score(lines[0][(self.lens[0] + 1):])
		lines[0] = lines[0][:(self.lens[0] + 1)] + line0_underscored_part
		lines[1] = self.printer.under_score(lines[1][:self.lens[4]]) + lines[1][self.lens[4]:]

		# rest of the lines get looped
		intermediate = int((len(self.lens) - 3) / 2) - 1

		for i in range(1, int(len(lines) / 2)):
			num_pos = self.lens[0] - self.lens[(i * 2) + 3] - (intermediate - i - 1)
			spaces = lines[(i * 2) + 1][:num_pos - 1]
			underscored = lines[(i * 2) + 1][num_pos - 1:num_pos + self.lens[(i * 2) + 4]]
			lines[(i * 2) + 1] = spaces + self.printer.under_score(underscored)

		return lines