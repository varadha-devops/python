import os, os.path

homedir = os.path.expanduser('~')
INPUT_FILE = os.path.join(homedir, "data.txt")
with open("data.txt") as f:
    for line in f:
        names = line.split(":")
	if len(names) == 2:
		print("Lastname: "+ names[1])
