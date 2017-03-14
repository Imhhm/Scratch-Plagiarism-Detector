#contains all global variables
def init():
	global allFolders
	allFolders = []
	global graphs_per_file
	graphs_per_file = []
	global file_name_dict
	file_name_dict = dict()
	global code_size_name_dict
	code_size_name_dict  = dict()
	global projectjsonfiles
	projectjsonfiles = []
	global filenames
	filenames=[]
	global folder
	import os
	folder = ""
	global OutputLogFile
	OutputLogFile = ""
