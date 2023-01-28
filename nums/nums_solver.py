import puzzle_solver
import os
import time

HOME = os.environ.get("HOME")
g_nums_folder = HOME + "/Documents/myProjects/nums_and_letters/"
g_archive_file = "samples/archived_solutions.txt"
g_nums_src = "nums/nums.txt"

# archiving is meant for future project of training a NN with data.
def archive_solution(words: list[str], nums: list[int]):
	file = open(g_nums_folder + g_archive_file, "a")
	line = "[["

	for i in range(len(words) - 1):
		line += "'" + words[i] + "', "

	line += "'" + words[-1] + "'], ["

	for i in range(len(nums) - 1):
		line += str(nums[i]) + ", "

	line += str(nums[-1]) + "]]\n"
	file.write(line)
	file.close()

def read_words_from_txt():
	with open(g_nums_folder + g_nums_src) as file:
		lines = file.readlines()
		lines = [line.rstrip() for line in lines]

	return lines

# measuring the test's running time just for fun.
def duration(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		end = time.time()
		print(f'\nIt took {(end - start):.3f}[sec] to solve.')

	return wrapper

@duration
def solving(solver: puzzle_solver.PuzzleSolver):
	solver.solve_with_prints()


if __name__ == "__main__":
	words = read_words_from_txt()
	solver = puzzle_solver.PuzzleSolver(words)
	solving(solver)
	archive_solution(words, solver.solution)