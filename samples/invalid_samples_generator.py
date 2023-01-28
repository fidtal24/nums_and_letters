import random
import os

HOME = os.environ.get("HOME")
nums_folder = "Documents/Friday/nums/"
arcive_file = "archived_solutions.txt"
generated_file = "generated_invalid_solutions.txt"

def read_words(row):
	with open(HOME+"/"+nums_folder+arcive_file, 'r') as file:
		for i, line in enumerate(file):
			if i == row:
				text = line.rstrip()
	start = text.find('[')
	end = text.find(']')
	words = text[(start + 1):(end)].split(', ')
	new_words = []
	for word in words:
		new_words.append(word[1:-1])

	return new_words

def create_nums(words):
	nums = []
	for word in words:
		nums.append(random.randint(10 ** (word.__len__() - 1), 10 ** (word.__len__())))
	return nums

def archive_solution(words, nums):
	file = open(HOME+"/"+nums_folder+generated_file, "a")
	line = "["
	for i in range(words.__len__() - 1):
		line += "'"+words[i]+"', "
	line += "'"+words[-1]+"'], ["
	for i in range(nums.__len__() - 1):
		line += str(nums[i])+", "
	line += str(nums[-1])+"]\n"
	file.write(line)
	file.close()

def write_to_archive_regular(row):
	words = read_words(row)
	nums = create_nums(words)
	archive_solution(words, nums)

if __name__ == "__main__":
	words = read_words(47)
	nums = create_nums(words)
	archive_solution(words, nums)