import os
import re
import sys

year_re = re.compile("((20|19)\d\d)")


os.chdir(".")


print(os.getcwd())
for f in os.listdir('.'):
	file_name, file_ext = os.path.splitext(f)
	file_name = file_name.replace("(", "")
	file_name = file_name.replace(".", " ")
	start=0
	while True:
		match = year_re.search(file_name, start)

		if not match:
			break

		last_match = match
		start = last_match.end()

	final = file_name[:last_match.end()] + file_ext
	print(final)
	#remove commenting to start the batch renaming
	#os.rename(f, final)
