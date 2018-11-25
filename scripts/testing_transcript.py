transcript_f = open("generated/testprompts", "r")
transcript_arr = transcript_f.readlines()
transcript_f.close()

files = open("generated/open_test_transcript.mlf", "w")
files.write('#!MLF!#\n')
for transcript in transcript_arr:
    t = transcript.split(' ')
    files.write('"*/'+t[0]+'lab"\n')
    for x in t[1:]:
        files.write(x.splitlines()[0]+"\n")
    files.write('.\n')
files.close()