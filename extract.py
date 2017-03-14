
import os,sys
import zipfile
import numpy
import copy
import settings
import subprocess
import json
# settings.folder =os.getcwd()

#Uncomment this when improving code

#os.path.abspath(path)




class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

#settings.allFolders=[]		
#changing the extension of all the files in the folder to zip:
#(have to change it back after extracting)
# settings.filenames=[]
for filename in os.listdir(settings.folder):
	infilename = os.path.join(settings.folder,filename)
	if not os.path.isfile(infilename): continue
	#print(infilename,infilename.split(".")[1])
	if(".sb2" not in infilename or ".sb" not in infilename): 
		settings.OutputLogFile.write(infilename+ ": Not an sb2 or sb file.\n")
		continue
	#oldbase = os.path.splitext(filename)
	#filesize = os.path.getsize(infilename)
	settings.filenames.append(infilename)
	#filesizes.append(filesize)
	newname = infilename.replace('.sb2', '.zip')
	output = os.rename(infilename, newname)
	#print("filename: ",filename,"  infilename",infilename,"  newname",newname)
	settings.OutputLogFile.write("filename: "+filename+"  infilename  "+infilename+"  newname  "+newname+"\n")
	if(newname.split(".")[-1]=="zip"):
		settings.allFolders.append(newname.split(".zip")[0])
		with zipfile.ZipFile(newname, "r") as z:
			z.extractall(newname[:-4])

#changing back the extension of the files to sb2:
for filename in os.listdir(settings.folder):
	infilename = os.path.join(settings.folder,filename)
	if not os.path.isfile(infilename): continue
	oldbase = os.path.splitext(filename)
	newname = infilename.replace('.zip', '.sb2')
	output = os.rename(infilename, newname)
	#settings.filenames.append(infilename);
	#print("filename: ",filename,"  infilename",infilename,"  newname",newname)

#settings.projectjsonfiles=[]

for folderName in settings.allFolders:
	with cd(folderName):
		subprocess.call("ls")
		with open('project.json', encoding="utf-8") as json_data:
			d = json.load(json_data)
			#pprint.pprint(d)
			settings.projectjsonfiles.append(d)
