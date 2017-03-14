#plagiarism detection of all files
#get the file names
def run():
	import settings
	import os
	#settings.OutputLogFile = open("logs\\settings.OutputLogFile.txt",'w',encoding='utf-8')
	import extract
	import create_pdg
	import similarity_detection
	plag = []
	done=[] #for i and j

	plagscore_code_size_names = list()
	# sorted(unsorted, key=lambda element: (element[1], element[2]), reverse=True)
	# file_name_size_dict = dict(zip(to_zip_w_filenames,code_size_name))

	ResFile = open(settings.folder+"/logs/res.txt",'w')

	for i in range(len(settings.graphs_per_file)):
		for j in range(len(settings.graphs_per_file)):
			if i<j:
				f1=settings.file_name_dict[i].split("\\")[-1]
				f2=settings.file_name_dict[j].split("\\")[-1]
				graphs_per_obj_1 = settings.graphs_per_file[i]
				graphs_per_obj_2 = settings.graphs_per_file[j]
				settings.OutputLogFile.write("FILE " + settings.file_name_dict[i] + "and file:" + settings.file_name_dict[j]+ " : "+'\n')
				print("FILE " + settings.file_name_dict[i] + "and file:" + settings.file_name_dict[j]+ " : ")
				plagiarism_score = similarity_detection.is_plagiarised(graphs_per_obj_1,graphs_per_obj_2)

				plagscore_code_size_names.append([plagiarism_score, settings.code_size_name_dict[i][0]+settings.code_size_name_dict[j][0], f1, f2])
				if plagiarism_score != -1: #-1 means it's not plagiarised.
					#done.append(files)
					#print("File:",settings.file_name_dict[i], "and file:",settings.file_name_dict[j] ,"are detected to be plagiarised by a plagiarism score of  ",plagiarism_score,'\n') #also find and print filenames			
					print("File:",f1, "and file:",f2 ,"are detected to be plagiarised by a plagiarism score of  ",plagiarism_score,'\n') #also find and print filenames			
					settings.OutputLogFile.write("File: "+f1.encode('utf-8','ignore').decode('utf-8')+" and file: "+f2.encode('utf-8','ignore').decode('utf-8')+" are detected to be plagiarised by a plagiarism score of  "+str(plagiarism_score)+'\n')
					ResFile.write(f1.encode('utf-8','ignore').decode('utf-8')+";;"+f2.encode('utf-8','ignore').decode('utf-8')+";;"+str(plagiarism_score)+'\n')
					
	ResMinFile = open(settings.folder+"/logs/res_min.txt",'w')
	print("Plagiarism scores:")
	print(plagscore_code_size_names)

	plagscore_code_size_names=sorted(plagscore_code_size_names,key=lambda element: (element[0], element[1]),reverse=True)
	print("Sorted:")
	print(plagscore_code_size_names)
	ResMinFile.write("Plagiarism scores:\n")

	for alist in plagscore_code_size_names:
		ResMinFile.write(str(alist)+'\n')

	'''		
	for i in range(len(settings.graphs_per_file)):
		for j in range(len(settings.graphs_per_file)):
			if i!=j:
				#files = set([i,j])
				#if(files in done):
				#	break
				graphs_per_obj_1 = settings.graphs_per_file[i]
				graphs_per_obj_2 = settings.graphs_per_file[j]
				f1=settings.file_name_dict[i].split("\\")[-1]
				f2=settings.file_name_dict[j].split("\\")[-1]
				settings.OutputLogFile.write("FILE " + f1 + "and file:" + f2+ " : ")
				plagiarism_score = is_plagiarised(graphs_per_obj_1,graphs_per_obj_2)
				if plagiarism_score != -1: #-1 means it's not plagiarised.
					#done.append(files)
					#print("File:",settings.file_name_dict[i], "and file:",settings.file_name_dict[j] ,"are detected to be plagiarised by a plagiarism score of  ",plagiarism_score,'\n') #also find and print filenames			
					print("File:",f1, "is detected to be plagiarised by file:",f2 ,"by a plagiarism score of  ",plagiarism_score,'\n') #also find and print filenames			
				else:
					print("File:",f1, "is detected to be plagiarised by file:",f2 ,"by a plagiarism score of  ",plagiarism_score,'\n') #also find and print filenames			
	'''
	ResMinFile.close()
	ResFile.close()
	settings.OutputLogFile.close()