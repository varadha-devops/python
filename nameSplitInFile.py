import os, os.path

homedir = os.path.expanduser('~')
INPUT_FILE = os.path.join(homedir, "data.txt")
with open("data.txt") as f:
    for line in f:
        #linedata = line.split(':')
        linedata = line.partition(":")

        print(linedata[1])
