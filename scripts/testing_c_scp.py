import os

def listFiles(relativePath):
	walkTuple = os.walk(os.curdir+relativePath)
	listItem = list(map(list,walkTuple))
	listItem = listItem[0]
	
	return {
		"dirs" : listItem[1],
		"files" : listItem[2]
	}
	
# list = listFiles("/test/dataset")
# filesList = list["files"]

file1 = open("generated/closed_test_codetrain.scp", "w+")
file2 = open("generated/closed_test_train.scp", "w+")

for n in range(76,151):
	file1.write('train/dataset/'+str(n)+'.wav train/mfcc/'+str(n)+".mfc\n")
	file2.write("train/mfcc/"+str(n)+".mfc\n")

file1.close()
file2.close()