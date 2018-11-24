import os

fileW = open("hmms/hmm0/macros", "w+")

with open("hmms/hmm0/proto", "r") as fileR:
    i = 0
    for line in fileR:
        if(i < 3):
            fileW.write(line)
        else:
            break
        i += 1

with open("hmms/hmm0/vFloors", "r") as fileR:
    for line in fileR:
        fileW.write(line)
fileW.close()