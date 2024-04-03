#!/usr/bin/python3

# plan:
# open the file "/proc/sys/fs/file-nr" in read mode
# first value is the number of open file descriptions (means files)
# so read file and get first value

def get_number_open_files():
	with open('/proc/sys/fs/file-nr', 'r') as file:
		number = file.read().rstrip().split()[0]
		return number


if __name__ == '__main__':
	print(get_number_open_files())