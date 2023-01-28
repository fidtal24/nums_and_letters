from nums import puzzle_solver

REF = 0
WORDS = 1

# Each test case contains: solution: list[int] and words: list[str].
test_cases = [
	[[8954, 7098, 1856, 5242], ['הנוי', 'יובל', 'שנים', 'אהאנ'], "PlusMinus"],
	[[7570, 4773, 2797, 1976], ['x-x-', '-xx-', '-x-x', '--x-'], "PlusMinus_x"],
	[[285, 697, 1995, 2565, 1710, 198645], ['מצב', 'חדש', 'מדדל', 'משמב', 'גלחל', 'מושצדל'], "Multiplication"],
	[[224, 233, 672, 672, 448, 52192], ['--x', '---', '---', '---', 'xx-', '-----'], "Multiplication_x"],
	[[8376, 251, 33, 93, 753, 846, 753], ['חורף', 'זמן', 'רר', 'רץ', 'רמו', 'חטף', 'רמו'], "Division"]
	]

class TestCase:
	def __init__(self, ref: list[int], words: list[str]) -> None:
		self.words = words
		self.ref = ref
		self.solver = puzzle_solver.PuzzleSolver(words)
		self.name = self.solver.name

	def run_test(self) -> int:
		self.solver.solve()
		cmp_result = self.cmp_test_result()
		self.print_test_result(cmp_result)

		return cmp_result

	def cmp_test_result(self):
		nums = (int(num) for num in self.solver.solution)

		return 1 if list(nums) == self.ref else 0

	def print_test_result(self, cmp_result):
		if cmp_result == 1:
			print_passed(self.name)
		else:
			print_failed(self.name)



def green(text: str):
	return "\033[92m" + text + "\033[0m"

def red(text: str):
	return "\033[91m" + text + "\033[0m"

def yellow(text: str):
	return "\033[93m" + text + "\033[0m"

def print_passed(test_name: str):
	print(test_name + ": " + green("Passed!"))

def print_failed(test_name: str):
	print(test_name + ": " + red("Failed!"))

def print_conclusion(passed: int, tests: int):
	conclusion = "\n=============== " + str(passed) + "/" + str(tests) + " passed ===============\n"

	if passed < tests:
		conclusion = red(conclusion)
	else:
		conclusion = green(conclusion)

	print(conclusion)

def print_menu():
	print("Please choose what tests you want to run:")

	for (index, test_case) in enumerate(test_cases):
		print("[" + str(index) + "]: " + test_case[2])

	print("[5]: all\n")

def run_menu():
	all_tests = [0, 1, 2, 3, 4]
	print_menu()
	tests_chosen = input("User choises are: ")
	test_nums = list(int(test) for test in tests_chosen.split())

	if 5 in test_nums:
		test_nums = all_tests

	return test_nums


if __name__ == "__main__":
	user_choises = run_menu()
	passed_count = 0
	print(yellow("\n============== Test Started ==============\n"))

	for i in user_choises:
		test = TestCase(test_cases[i][REF], test_cases[i][WORDS])
		passed_count += test.run_test()

	print_conclusion(passed_count, len(user_choises))