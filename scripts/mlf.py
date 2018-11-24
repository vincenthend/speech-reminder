import os

def listFiles(relativePath):
	print(os.curdir+relativePath)
	walkTuple = os.walk(os.curdir+relativePath)
	listItem = list(map(list,walkTuple))
	listItem = listItem[0]
	
	return {
		"dirs" : listItem[1],
		"files" : listItem[2]
	}
	
list = listFiles("/train/dataset")
filesList = list["files"]

files = open("generated/words.mlf", "w+")
files.write('#!MLF!#\n')
for file in filesList:
	files.write('"*/'+file.split(".")[0]+'.lab"'+"\n")
	name_split = file.split('_')
	files.write(name_split[0].upper()+"\n")
	files.write('.'+"\n")

files.close()