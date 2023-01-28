import ast

def read_words_from_txt():
	with open("/home/tal/Documents/myProjects/nums_and_letters/samples/archived_solutions.txt") as file:
		lines = file.readlines()
		lines = [line.rstrip() for line in lines]

	return lines

lines = read_words_from_txt()
new_lines = list(set(lines))



file = open("/home/tal/Documents/myProjects/nums_and_letters/samples/tmp3.txt", "a")
for new_line in new_lines:
	file.write(str(new_line) + "\n")
file.close()