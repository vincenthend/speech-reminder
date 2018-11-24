import os

fileW = open("generated/monophones0", "w+")

with open("generated/monophones1", "r") as fileR:
    for line in fileR:
        if not (line[:len(line)-1] == 'sp'):
            fileW.write(line)

fileW.close()