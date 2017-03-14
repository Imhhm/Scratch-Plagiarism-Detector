	
#ISOMORPHISM DETECTION

#we're going to make a list of G's (graphs) for each object,
#and we'll compare the list of pdg's of one object with the list of pdg's of all the other objects in the 
from extract import *
from create_pdg import *
from similarity_detection import *
import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.isomorphism as iso
#labelled subgraph isomorphism:
#DiGraphMatcher.__init__(G1, G2, node_match=None, edge_match=None)
#gamma is mature rate in isomorphism testing: default: 0.9
#returns 1 if the graphs are gamma-isomorphic else 0
#output: pdg pairs regarded to involve plagiarism

# settings.OutputLogFile = open("logs\\settings.OutputLogFile.txt",'a')

def isomorphism_check(G1,G2):
	plagiarised = -1
	#TODO: change gamma
	gamma = 0.9
	nm = iso.categorical_node_match('node_type','motion') #just putting motion as the default value anyway all nodes will have node_type 
	GM = iso.DiGraphMatcher(G1,G2,node_match=nm)
	num_nodes = min(nx.number_of_nodes(G1),nx.number_of_nodes(G2)) #----
	max_num_node = max(nx.number_of_nodes(G1),nx.number_of_nodes(G2))
	#settings.OutputLogFile.write("Isomorphism_check: min number of nodes = "+str(num_nodes)+"\n")
	#DiGraphMatcher.subgraph_isomorphisms_iter()
	#settings.OutputLogFile.write("Subgraphs:\n")
	for subgraph in GM.subgraph_isomorphisms_iter():
		#print("type of subgraph: ",type(subgraph)) #WAS COMMENTED OUT BEFORE
		#print(subgraph)	#WAS COMMENTED OUT BEFORE
		settings.OutputLogFile.write("subgraph:\n" + str(subgraph)+'\n')
		settings.OutputLogFile.write(str(subgraph)+'\n')
		if(len(subgraph)>=gamma*num_nodes): #passing it through the filter
			#settings.OutputLogFile.write("Plagiarised subgraph:\n" + str(subgraph)+'\n')
			#plagiarised = True
			plagiarised = (len(subgraph)/max_num_node if max_num_node!=0 else 0)
			break
	return plagiarised
	

'''
def is_plagiarised_pdgs(graph_list_1, graph_list_2):
	plagiarism_pairs = set()
	#print("Type of graph: ",type(graph_list_1[0]))
	for G1 in graph_list_1:
		for G2 in graph_list_2:
			if(isomorphism_check(G1,G2) == True):
				plagiarism_pairs.add((G1,G2))
	return plagiarism_pairs
'''

#CHECK THIS - more efficient version of the above
def is_plagiarised_pdgs(graph_list_1, graph_list_2):
	plagiarism_pairs = set()
	#print("Type of graph: ",type(graph_list_1[0]))
	graph_list_1_copy = copy.deepcopy(graph_list_1)
	graph_list_2_copy = copy.deepcopy(graph_list_2)
	#can make this more efficient by doing it the same way as is_plagiarised using the done list 
	for G1 in graph_list_1_copy:
		corr_plag_obj = None
		max_fraction = 0
		for G2 in graph_list_2_copy:
			if(isomorphism_check(G1,G2) > 0.5 or isomorphism_check(G2,G1) > 0.5): #CHANGE THIS
				fraction = isomorphism_check(G1,G2) if isomorphism_check(G1,G2) > isomorphism_check(G2,G1) else isomorphism_check(G2,G1) #check if this compiles
				#maxer_fraction = max(fraction, max_fraction)
				if(fraction > max_fraction):
					max_fraction = fraction
					corr_plag_obj = G2
					graph_list_2_copy.remove(G2)
		settings.OutputLogFile.write("Max fraction in is_plagiarised_pdgs : " + str(max_fraction))
		if max_fraction > 0.75:
			plagiarism_pairs.add((G1,corr_plag_obj))
	return plagiarism_pairs
	
#have to do total plagiarised pairs/total num of pdg's for plagiarism score
def is_plagiarised(graphs_per_obj_1,graphs_per_obj_2):
	final_fraction = 0
	#if the number of objects in each file is different, it's not plagiarised
	settings.OutputLogFile.write("FYI\n")
	settings.OutputLogFile.write("object1:\n")
	for obj1 in graphs_per_obj_1:
		settings.OutputLogFile.write("len(graphs_per_obj_1["+str(obj1)+"])="+str(len(graphs_per_obj_1[obj1])) + "\n")
	for obj2 in graphs_per_obj_2:
		settings.OutputLogFile.write("len(graphs_per_obj_2["+str(obj2)+"])="+str(len(graphs_per_obj_2[obj2])) + "\n")
	settings.OutputLogFile.write("</FYI>\n")
	num_of_objs = (len(graphs_per_obj_1)+len(graphs_per_obj_2))//2
	max_num_of_objs = max(len (graphs_per_obj_1), len(graphs_per_obj_2))
	strnumobjs = "Number of objects: " + str(num_of_objs)
	total_plagiarism_pairs=0
	total_pdgs=0
	settings.OutputLogFile.write(strnumobjs+'\n')
	object_plagiarism_pairs = list()
	empty_script_objs=list()
	for obj1 in graphs_per_obj_1:
		maxfraction=0
		corr_plag_obj=None
		for obj2 in graphs_per_obj_2:
			if(obj2 in object_plagiarism_pairs):
				continue
			plagiarism_pairs = is_plagiarised_pdgs(graphs_per_obj_1[obj1],graphs_per_obj_2[obj2])
			#print("plagiarism pairs: ",plagiarism_pairs)
			#removed
			string = "Number of plagiarised blocks in objs " + str(obj1)+ " and "+str(obj2)+" respectively: =  "+str(len(plagiarism_pairs))
			settings.OutputLogFile.write(string+'\n')
			settings.OutputLogFile.write("Plagiarism pairs: "+str(plagiarism_pairs)+"\n")
			l1=len(graphs_per_obj_1[obj1])
			l2=len(graphs_per_obj_2[obj2])
			size_of_graphlist = min(l1,l2)
			if len(graphs_per_obj_1[obj1]) == len(graphs_per_obj_2[obj2]) == 0: 
					string = "len(graphs_per_obj_1[obj1]) = "+str(len(graphs_per_obj_1[obj1]))+'\n'
					string+= "len(graphs_per_obj_2[obj2]) = " + str(len(graphs_per_obj_2[obj2])) +'\n'
					string+= "Number of pdg's in objs " + str(obj1)+ " and "+str(obj2)+" =  0\n"
					settings.OutputLogFile.write(string+'\n')
					corr_plag_obj=obj2
					num_of_objs-=1
					max_num_of_objs-=1
					break
			elif len(graphs_per_obj_1[obj1])!=0:
				#num_of_pdgs= size_of_graphlist if l2!=0 else l1
				num_of_pdgs = max(l1,l2)
				fraction = len(plagiarism_pairs)/num_of_pdgs
				total_plagiarism_pairs+=len(plagiarism_pairs)
				total_pdgs+=num_of_pdgs
				string="Fraction of plagiarised blocks for the object pair: "+ str(fraction)					
				#print("fraction: ",fraction)
				#NEWLY INSERTED CODE
				if(fraction>maxfraction):
					maxfraction = fraction
					corr_plag_obj=obj2
				settings.OutputLogFile.write(string+'\n')
				if fraction>0:
					string="Fraction of plagiarised blocks for the object pair: "+ str(fraction)					
					#print("fraction: ",fraction)
		final_fraction += maxfraction
		if(corr_plag_obj is not None):
			object_plagiarism_pairs.append(corr_plag_obj)
		#have a done list for obj2's
		settings.OutputLogFile.write("Max fraction: " + str(final_fraction) + "\n")
	settings.OutputLogFile.write("Total plagiarism pairs = "+str(total_plagiarism_pairs) + "\n")
	settings.OutputLogFile.write("Total number of pdg's : "+str(total_pdgs) + "\n")
	#settings.OutputLogFile.write("WANNABE fraction: " + str(total_plagiarism_pairs/total_pdgs)+ "\n")
        #print("WANNABE fraction: " + str(total_plagiarism_pairs/total_pdgs)+ "\n")
	settings.OutputLogFile.write("Final fraction= "+str(final_fraction)+"/"+str(max_num_of_objs)+'\n')
	if num_of_objs > 0:
		final_fraction=final_fraction/max_num_of_objs
	else:
		final_fraction=0.0
	settings.OutputLogFile.write("Final fraction: "+str(final_fraction)+'\n')
	return final_fraction
					
	'''
	if(len(object_plagiarism_pairs)>0):
		print("Plagiarised object mappings : ",object_plagiarism_pairs)
		print("Number of plagiarised objects: ",len(object_plagiarism_pairs))
		return True
	else:
		return False
	'''		


#TO-INCLUDE - CODE FOR ISOMORPHISM DETECTION