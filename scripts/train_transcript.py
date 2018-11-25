transcript_f = open("train/trainprompts", "r")
transcript_arr = transcript_f.readlines()
transcript_f.close()

files = open("generated/open_train_transcript.mlf", "w")
files.write('#!MLF!#\n')
for transcript in transcript_arr:
    t = transcript.split(' ')
    files.write('"*/'+t[0]+'lab"\n')
    if(len(t) == 2):
        for x in t[1:]:
            if(x != ""):
                a = x.replace("\n", "")
                a = a.replace("\r", "")
                files.write("SENT-START\n")
                files.write(a+"\n")
                files.write("SENT-END\n")
    else:
        for x in t[1:-1]:
            if(x != ""):
                a = x.replace("\n", "")
                a = a.replace("\r", "")
                files.write(a+"\n")
    files.write('.\n')
files.close()