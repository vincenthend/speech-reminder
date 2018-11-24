import os

def listFiles(relativePath):
	walkTuple = os.walk(os.curdir+relativePath)
	listItem = list(map(list,walkTuple))
	listItem = listItem[0]
	
	return {
		"dirs" : listItem[1],
		"files" : listItem[2]
	}
	
list = listFiles("/dataset")
filesList = list["files"]

files = open("codetrain.scp", "w+")

for file in filesList:
	files.write('dataset/'+file.split(".")[0]+'.wav mfcc/'+file.split(".")[0]+".mfc\n")

files.close()