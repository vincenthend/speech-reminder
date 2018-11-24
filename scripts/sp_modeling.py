import os

fileW = open("hmms/hmm4/hmmdefs", "w+")

with open("hmms/hmm3/hmmdefs", "r") as fileR:
    record = ''
    startRecord = False
    mean25First = False
    step3 = False
    for line in fileR:
        if (line[:len(line)-1] == "<MEAN> 25" and startRecord):
            startRecord = False
            mean25First = True
        elif (line[:len(line)-1] == "~h \"sil\""):
            startRecord = True
            record += "~h \"sp\"\n"
        elif (line[:len(line)-1] == "<MEAN> 25" and mean25First):
            startRecord = True
            mean25First = False
            step3 = True
            record += line
        elif (line[:len(line)-1] == "<NUMSTATES> 5" and startRecord):
            record += "<NUMSTATES> 3\n"
        elif (line[:len(line)-1] == "<STATE> 4"):
            startRecord = False
        elif (startRecord):
            record += line

        fileW.write(line)
    record += '<TRANSP> 3\n'
    record += ' 0.0 1.0 0.0\n'
    record += ' 0.0 0.9 0.1\n'
    record += ' 0.0 0.0 0.0\n'
    record += '<ENDHMM>\n'
    fileW.write(record)
fileW.close()