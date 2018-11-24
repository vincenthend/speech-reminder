import os

fileW = open("hmm0/hmmdefs", "w+")
proto = ''
with open("hmm0/proto", "r") as fileProto:
    i = 0
    for line in fileProto:
        if i > 3:
            proto += line
        i += 1

with open("stats.txt", "r") as fileR:
    for line in fileR:
        fileW.write('~h "' + line[:len(line)-1] + '"\n')
        fileW.write(proto)

fileW.close()