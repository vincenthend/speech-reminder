import os

def listFiles(relativePath):
	walkTuple = os.walk(os.curdir+relativePath)
	listItem = list(map(list,walkTuple))
	listItem = listItem[0]
	
	return {
		"dirs" : listItem[1],
		"files" : listItem[2]
	}
	
list = listFiles("/train/dataset")
filesList = list["files"]

file1 = open("generated/open_train_codetrain.scp", "w+")
file2 = open("generated/open_train_train.scp", "w+")

for file in filesList:
	file1.write('train/dataset/'+file.split(".")[0]+'.wav train/mfcc/'+file.split(".")[0]+".mfc\n")
	file2.write("train/mfcc/"+file.split(".")[0]+".mfc\n")

file1.close()
file2.close()