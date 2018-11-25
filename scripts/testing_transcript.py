transcript_f = open("test/testprompts", "r")
transcript_arr = transcript_f.readlines()
transcript_f.close()

files = open("generated/open_test_transcript.mlf", "w")
files.write('#!MLF!#\n')
for transcript in transcript_arr:
    t = transcript.split(' ')
    files.write('"*/'+t[0]+'lab"\n')
    for x in t[1:-1]:
        if(x != "SENT-START" and x != "SENT-END" and x != ""):
            a = x.replace("\n", "")
            a = a.replace("\r", "")
            files.write(a+"\n")
    files.write('.\n')
files.close()