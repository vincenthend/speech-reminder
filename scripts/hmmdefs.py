import os

fileW = open("hmms/hmm0/hmmdefs", "w+")
proto = ''
with open("hmms/hmm0/proto", "r") as fileProto:
    i = 0
    for line in fileProto:
        if i > 3:
            proto += line
        i += 1

with open("generated/monophones0", "r") as fileR:
    for line in fileR:
        fileW.write('~h "' + line[:len(line)-1] + '"\n')
        fileW.write(proto)

fileW.close()