import random
import os

HOME = os.environ.get("HOME")
nums_folder = "Documents/Friday/nums/"
arcive_file = "archived_solutions.txt"
generated_file = "generated_solutions.txt"

letters = [
	b'\xd7\x90', b'\xd7\x91', b'\xd7\x92', b'\xd7\x93', b'\xd7\x94',
	b'\xd7\x95', b'\xd7\x96', b'\xd7\x97', b'\xd7\x98', b'\xd7\x99',
	b'\xd7\x9a', b'\xd7\x9b', b'\xd7\x9c', b'\xd7\x9d', b'\xd7\x9e',
	b'\xd7\x9f', b'\xd7\xa0', b'\xd7\xa1', b'\xd7\xa2', b'\xd7\xa3',
	b'\xd7\xa4', b'\xd7\xa5', b'\xd7\xa6', b'\xd7\xa7', b'\xd7\xa8',
	b'\xd7\xa9', b'\xd7\xaa'
]

def read_nums(row):
	with open(HOME+"/"+nums_folder+arcive_file, 'r') as file:
		for i, line in enumerate(file):
			if i == row:
				text = line.rstrip()
	start = text.rfind('[')
	nums_str = text[(start + 1):-1].split(', ')
	nums = []
	for num in nums_str:
		nums.append(int(num))
	return nums

def translate_to_letters(num):
	digits = random.sample(range(0, 26), 10)
	num_str = str(num)
	word = ""
	for i in num_str:
		word += letters[digits[int(i)]].decode()
	return word

def create_regular_words(nums):
	words = []
	for num in nums:
		words.append(translate_to_letters(num))
	return words

def create_x_words(nums, x):
	words = []
	for num in nums:
		num_str = str(num)
		word = ""
		for letter in num_str:
			if int(letter) == x:
				word += 'x'
			else:
				word += '-'
		words.append(word)
	return words

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
	nums = read_nums(row)
	words = create_regular_words(nums)
	archive_solution(words, nums)

def write_to_archive_x(row):
	nums = read_nums(row)
	for i in range(10):
		words_x = create_x_words(nums, i)
		archive_solution(words_x, nums)

def generate_samples_from_line(row):
	for j in range(10):
		write_to_archive_regular(i)
	write_to_archive_x(i)

if __name__ == "__main__":
	with open(HOME+"/"+nums_folder+arcive_file, 'r') as fp:
		for count, line in enumerate(fp):
			pass
	for i in range(count + 1):
		generate_samples_from_line(i)
