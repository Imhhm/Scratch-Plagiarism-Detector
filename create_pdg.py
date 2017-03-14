
from node_classification import *
import settings
import networkx as nx
import matplotlib.pyplot as plt
# just to call an arbitrary command e.g. 'ls'
# enter the directory like this:

		#full=f.readlines()
		#settings.projectjsonfiles.append(full.join(""))
pdg_scripts=[]#script for each file
count=-1
graph=[]
childgraph=[]
per_file=[]
#I'm numbering objects here, instead of using their names. graphs_dict[0] = graph (i.e. graphs of the stage)
#graphs_dict={}
vars_dict={}
lists_dict={}
codesizes=[]
size=0
	
#settings.OutputLogFile = open("logs\\settings.OutputLogFile.txt",'a', encoding='utf-8')

def count_size(x):
    f = lambda x: 0 if not isinstance(x,list) else (f(x[0]) + f(x[1:]) if len(x) else 1)
    return f(x) - 1

#NEED TO ADD VARIABLES AND LISTS IN THE PARSER - DON'T FORGET
for i in settings.projectjsonfiles:
	obj_count = 0
	childgraph=[]
	graphs_dict={}
	graph=[]
	count+=1  
	size=0 #code size
	script_file=[]
	#NEED TO ADD VARIABLES AND LISTS IN THE PARSER - DON'T FORGET
	for x in i:
		if x=='children':
			#print("TYPE FOR CHILD:",type(i[x])) #list.
			'''for child in i[x]: #i[x] refers to the value of 'children'. child iterates through each child in the children list 
				#print("TYPE,LEN OF CHILD:",type(child),len(child) #should be dict if there's only 1 child
				print("child: ",child)
			'''
			for k in range(len(i[x])): #i[x] refers to the value of 'children'. child iterates through each child in the children list 
				#print("TYPE,LEN OF CHILD:",type(child),len(child) #should be dict if there's only 1 child
				if("objName" in i[x][k]):
					obj_count+=1
					#print("child: ",i[x][k])
					graphs_dict[obj_count]=[]
				if('scripts' in i[x][k]):
					for each_script in i[x][k]['scripts']:
						size+=count_size(each_script)
						for each in each_script[2:]:
							graphs_dict[obj_count].append(each)
		if x=='scripts': #scripts of the stage object
			for each_script in i[x]:
				size+=count_size(each_script)
				for each in each_script[2:]:
					graph.append(each)
	#NEED TO ADD VARIABLES AND LISTS IN THE PARSER - DON'T FORGET
	#print("NUMBER OF OBJECTS: ",obj_count)
	graphs_dict[0]=graph
	codesizes.append(size)
	per_file.append(graphs_dict)

filename_per_file=list(zip(settings.filenames,per_file))

code_size_name=list(zip(codesizes,settings.filenames))

code_size_name_perfile=list(zip(codesizes,filename_per_file))

code_size_name = sorted(code_size_name,reverse=True)
code_size_name_perfile = sorted(code_size_name_perfile,reverse=True)

to_zip_w_filenames=[i for i in range(len(settings.filenames))]
settings.code_size_name_dict = dict(zip(to_zip_w_filenames, code_size_name))

#file_names_desc has all the file names in desc order
file_names_desc = [fsn[1] for fsn in code_size_name]
settings.file_name_dict = dict(zip(to_zip_w_filenames,file_names_desc))

new_per_file=[x[1][1] for x in code_size_name_perfile]
per_file=new_per_file
all_folders_sorted = []
for fsn in code_size_name:
	all_folders_sorted.append(fsn[1].split(".sb2")[0])
	
def create_nodes_id(G,node_id, graph):
	#graph will be a list of networkx nodes.
	for node in graph:
		if(node_type.get(node[0]) is None):
			pass
		elif(node_type[node[0]] == 'control_cond1'): 
			node_id_candidate = nodes_ctrl_cond1(node_id, node, G) #adds the nodes to the graph
			if(node_id_candidate!=-1):
				node_id = node_id_candidate
			else:
				print("didn't make node for: ",str(node).encode('utf-8'))
		elif(node_type[node[0]] == 'control_cond2'):
			node_id_candidate = nodes_ctrl_cond2(node_id, node, G) #adds the nodes to the graph
			if(node_id_candidate!=-1):
				node_id = node_id_candidate
			else:
				print("didn't make node for: ",str(node).encode('utf-8'))
		elif(node_type[node[0]] == 'control_loop'):
			node_id = nodes_ctrl_loop(node_id,node,G) #adds the nodes to the graph
		elif(node_type[node[0]] == 'control_loop_cond'):
			node_id = nodes_ctrl_loop_cond(node_id,node,G) 
		else:
			node_id+=1
			#n[node_id]={node_type[node[0]],node} #node type and node text
			G.add_node(node_id,node_type = node_type.get(node[0],""), node_text=node) 
	return node_id
#creates a dictionary for a node with node id, node type and node text.
#creates a networkx graph with nodes, for a given block.
def create_nodes(graph):
	#global G
	G=nx.DiGraph()
	node_id = 0
	#graph will be a list of networkx nodes.
	for node in graph:
		if(node_type.get(node[0]) is None):
			pass
		elif(node_type[node[0]] == 'control_cond1'): 
			node_id_candidate = nodes_ctrl_cond1(node_id, node, G) #adds the nodes to the graph
			if(node_id_candidate!=-1):
				node_id = node_id_candidate
		elif(node_type[node[0]] == 'control_cond2'): 
			node_id_candidate = nodes_ctrl_cond2(node_id, node, G) #adds the nodes to the graph
			if(node_id_candidate!=-1):
				node_id = node_id_candidate
		elif(node_type[node[0]] == 'control_loop'):
			node_id = nodes_ctrl_loop(node_id,node,G) #adds the nodes to the graph
		elif(node_type[node[0]] == 'control_loop_cond'):
			node_id = nodes_ctrl_loop_cond(node_id,node,G)
		else:
			node_id+=1
			#n[node_id]={node_type[node[0]],node} #node type and node text
			G.add_node(node_id,node_type = node_type.get(node[0],""), node_text=node) 
	return G #returns the graph with all the nodes

#creates final nodes in the block.
#returns final node_id		


'''
["doIf", -1
							false,
							[["doIf", - 2 
									false,
									[["doIf", false, - 5  [["wait:elapsed:from:", 3.2] -6, ["wait:elapsed:from:", 3.2] -7, ["wait:elapsed:from:", 3.3]]]]],
								["wait:elapsed:from:", 1.2] - 3,
								["wait:elapsed:from:", 1.3] - 4]]
'''	
#add nodes to the graph. returns final node id
#for doIf
def nodes_ctrl_cond1(node_id, node, G):
	if node[0] == 'doIf':
		if_bl = (node[2] if node[2] is not None else [])
		if(len(if_bl)==0):
			print("returned -1 for ",str(node).encode("utf-8"))
			return -1
		cond_node = [node_type[node[0]],[node[0],node[1]],len(if_bl), if_bl] #node text for the if node  is [node[0],node[1]]. it will have doIf, condition 
		node_id+=1
		#n[node_id] = cond_node
		G.add_node(node_id, node_type = node_type.get(node[0],""), node_text = [node[0],node[1]], block_len = len(if_bl), if_block = if_bl)
		cond_true_block = if_bl #if the condition is true,the block will get executed
		node_id = create_nodes_id(G, node_id, cond_true_block)
	return node_id

def nodes_ctrl_cond2(node_id,node,G):
	#doIfElse
	if node[0] == 'doIfElse':
		#the dictionary for the node will have node id, node type, and node text
		print("Before error: IFELSE",str(node).encode('ascii','ignore'))
		if_block = node[2]
		else_block = node[3]
		if(if_block is None and else_block is None):
			print("returned -1 for ",str(node).encode("utf-8"))
			return -1
		node_id+=1
		len_if = (len(node[2]) if node[2] is not None else 0)
		len_else = (len(node[3]) if node[3] is not None else 0)
		cond_node = [node_type[node[0]],[node[0],node[1]],len_if,len_else] #node text for the if else node  is [node[0],node[1]]. it will have doIfElse, condition 
		if_bl = (node[2] if node[2] is not None else [])
		else_bl = (node[3] if node[3] is not None else [])
		#n[node_id] = cond_node
		# ADDED IF BLOCK AND ELSE BLOCK ALSO AS ATTRIBUTES OF THE NODE.
		G.add_node(node_id, node_type = node_type.get(node[0],""), node_text = [node[0],node[1]], if_len = len_if, else_len = len_else, if_block=if_bl, else_block=else_bl,block_len=len_if+len_else)
		if_block = node[2]
		else_block = node[3]
		# if(if_block is None and else_block is None):
		# 	return -1
		if(if_block is not None):
			node_id = create_nodes_id(G, node_id, if_block)
		else_block = node[3]
		if(else_block is not None):
			node_id = create_nodes_id(G, node_id, else_block)
	return node_id

def nodes_ctrl_loop(node_id,node,G):
	if node[0] == 'doForever': #["doForever", null]
		print("Before error: doForever",str(node).encode('ascii','ignore'))
		do_f_block = (node[1] if node[1] is not None else [])
		if(len(do_f_block)>0):
			node_id += 1
			G.add_node(node_id, node_type = node_type.get(node[0],""), node_text = [node[0]], block_len=len(do_f_block), block = do_f_block)
			block = node[1]
			node_id = create_nodes_id(G, node_id, block)
	return node_id

def nodes_ctrl_loop_cond(node_id, node, G):
	if node[0] == 'doUntil': #["doUntil", false, null]
		print("Before error: doUntil",str(node).encode('ascii','ignore'))
		du_block = (node[2] if node[2] is not None else [])
		if(len(du_block)>0):
			node_id+=1
			G.add_node(node_id, node_type = node_type.get(node[0],""), node_text = [node[0],node[1]], block_len = len(du_block), block = du_block)
			block = node[2]
			node_id = create_nodes_id(G, node_id, block)	
	elif node[0] == 'doRepeat': #["doRepeat", 10, null]
		dr_block = (node[2] if node[2] is not None else [])
		if(len(dr_block)>0):
			node_id += 1
			G.add_node(node_id, node_type = node_type.get(node[0],""), node_text = [node[0],node[1]], block_len=len(node[2]), block = node[2])
			block = node[2]
			node_id = create_nodes_id(G, node_id, block)	
	return node_id


	

def event_cond(node):
	#make edge from node to all other nodes in graph
	global G
	settings.OutputLogFile.write("event_cond:\n")
	for n in G:
		if n>1 and n<=G.number_of_nodes():
			G.add_edge(G.nodes()[node-1],n)#to all the elements in its block
	settings.OutputLogFile.write(str(G.edges())+'\n')
	return
	
'''
def event(node):
	#broadcast
    return
def control_cond(node):
	#same as event_cond
'''
def control_cond1(node):
	#["doIf", ["<", "", ""], [["forward:", 10]]]
	#make edge from node[0] to each element of node[2]
	settings.OutputLogFile.write("control_cond1: "+str(node)+'\n')
	n=node-1
	list1=G.node[node]['if_block']
	#settings.OutputLogFile.write(str(list1)+'\n')
	#this checks for only one level of nesting
	for ele in list1:
		if(node_type.get(ele[0]) is not None):
			node+=1
			print("g.nodes():",G.nodes())
			print("ELe: ",str(ele).encode('ascii','ignore'))
			print("WHAT: n (node-1)",n,node-1)
			if(node-1<len(G.nodes())):
				G.add_edge(G.nodes()[n],G.nodes()[node-1])
			# G.add_edge(G.nodes()[n],G.nodes()[node-1])
			#if str(node_type[ele[0]]).split("_")[0]=="control":
			#	node+=G.node[node]['block_len']
			#print("!!!",str(node_type[ele[0]]))
				if str(G.node[node]['node_type']) in ["control_cond1", "control_cond2", "control_loop_cond", "control_loop"]:
				#	print("Whhy")
					node+=G.node[node]['block_len']	-1
			#print("Yay")
	settings.OutputLogFile.write(str(G.edges())+'\n')
	return
	
def control_cond2(node):
	#["doIfElse", ["<", "3", "2"], [["forward:", 10]], [["turnRight:", 15]]]
	#	make edge from node[0] to each element of node[2] and node[3]
	#print("control_cond2:",node)
	n=node-1
	list1=G.node[node]['if_block']+G.node[node]['else_block']
	for ele in list1:
		if(node_type.get(ele[0]) is not None):
			node+=1
			print("g.nodes():",G.nodes())
			print("ELe: ",str(ele).encode('ascii','ignore'))
			print("WHAT: n (node-1)",n,node-1)
			if(node-1<len(G.nodes())):
				G.add_edge(G.nodes()[n],G.nodes()[node-1])
			# G.add_edge(G.nodes()[n],G.nodes()[node-1])
			#"control_cond1", "control_cond2", "control_loop_cond", "control_loop", 
			#if str(node_type[ele[0]]).split("_")[0]=="control":
			#	node+=G.node[node]['block_len']		
				if str(G.node[node]['node_type']) in ["control_cond1", "control_cond2", "control_loop_cond", "control_loop"]:
					settings.OutputLogFile.write("control node: "+str(ele).encode('utf-8','ignore').decode('utf-8')+" node type: "+str(node_type[ele[0]])+'\n')
					node+=G.node[node]['block_len']	-1
	settings.OutputLogFile.write(str(G.edges())+'\n')
	return
	
def control_loop_cond(node):	
	#["doRepeat", 10, [["say:duration:elapsed:from:", "Hello!", 2]]]
	#["doUntil", false, [["say:", "Hello!"]]]
	#make edge from node[0] to each element of node[2]
	#make edge from last element of node[2] to node[0]
	#print("control_loop_cond:")
	#print("Node number: ",str(node))
	settings.OutputLogFile.write("control_loop_cond:\nnode:"+str(G.node[node]))
	settings.OutputLogFile.write(" node number: "+str(node)+"\n")
	n=node-1
	#node=node-1
	list1=G.node[node]['block']
	for ele in list1:
			#if str(node_type[ele[0]]).split("_")[0]=="control":
			#	node+=G.node[node]['block_len']	
			#print(ele)
			if(node_type.get(ele[0]) is not None):
				node+=1
				print("g.nodes():",G.nodes())
				print("ELe: ",str(ele).encode('ascii','ignore'))
				print("WHAT: n (node-1)",n,node-1)
				#print("WHAT: (node-1)",node-1)
				if(node-1<len(G.nodes())):
					G.add_edge(G.nodes()[n],G.nodes()[node-1])
				# G.add_edge(G.nodes()[n],G.nodes()[node-1])
					if str(G.node[node]['node_type']) in ["control_cond1", "control_cond2", "control_loop_cond", "control_loop"]:
						node+=(G.node[node]['block_len']-1)
				
	#print("BEfore error: ",G.nodes(),"\n",node-1,n)
	if(len(list1)>0):
		if((n)<len(G.nodes()) and node-1 < len(G.nodes())):
			G.add_edge(G.nodes()[node-1],G.nodes()[n])
	settings.OutputLogFile.write(str(G.edges())+'\n')
	return
	'''
	settings.OutputLogFile.write("control_loop_cond:\nnode:"+str(G.node[node])+"\n")
	n=node-1
	list1=G.node[node]['block']
	for ele in list1:
			node+=1
			#old=node
			G.add_edge(G.nodes()[n],G.nodes()[node-1])
			#if str(node_type[ele[0]]).split("_")[0]=="control":
			#	node+=G.node[node]['block_len']	
			#if str(node_type[ele[0]]) in ["control_cond1", "control_cond2", "control_loop_cond", "control_loop"]:
			if str(G.node[node]['node_type']) in ["control_cond1", "control_cond2", "control_loop_cond", "control_loop"]:
				all_the_keys = [i for i in G.node[node].keys()]
				settings.OutputLogFile.write("Keys of node "+str(node) + " are: "+str(all_the_keys)+' node type of ele: '+str(node_type[ele[0]])+'\n')
				node+=G.node[node]['block_len']	
	G.add_edge(G.nodes()[old-1],G.nodes()[n+1])
	settings.OutputLogFile.write(str(G.edges())+'\n')
	return'''


'''
G.add_node(node_id, node_type = node_type.get(node[0],""), node_text = node[0],
		block_len=len(node[1]), block = node[1])
'''
def control_loop(node):
	#["doForever", [["think:duration:elapsed:from:", "Hmm...", 2]["say:", "Hello!"]]]
	# make edge from node[0] to each element of node[1]
	# make edge from last element of node[1] to first element of node[1]

	#settings.OutputLogFile.write("control_loop:\nnode:"+str(G.node[node]))
	print("in control_loop")
	settings.OutputLogFile.write(" node number: "+str(node)+"\n")
	n=node-1
	list1=G.node[node]['block']
	old=node
	for ele in list1:
			if(node_type.get(ele[0]) is not None):
				node+=1
				print("g.nodes():",G.nodes())
				print("ELe: ",str(ele).encode('ascii','ignore'))
				print("WHAT: n (node-1)",n,node-1)
				#old=node
				if(node-1<len(G.nodes())):
					G.add_edge(G.nodes()[n],G.nodes()[node-1])
				#if str(node_type[ele[0]]).split("_")[0]=="control":
				#	node+=G.node[node]['block_len']	
				#if str(node_type[ele[0]]) in ["control_cond1", "control_cond2", "control_loop_cond", "control_loop"]:
					if str(G.node[node]['node_type']) in ["control_cond1", "control_cond2", "control_loop_cond", "control_loop"]:
						all_the_keys = [i for i in G.node[node].keys()]
						settings.OutputLogFile.write("Keys of node "+str(node) + " are: "+str(all_the_keys)+' node type of ele: '+str(node_type[ele[0]])+'\n')
						node+=G.node[node]['block_len']	-1

	if(len(list1)>0):
		print("n+1: ",n+1,"node-1",node-1)
		if((n+1)<len(G.nodes()) and node-1 < len(G.nodes())):
			G.add_edge(G.nodes()[node-1],G.nodes()[n+1])
	settings.OutputLogFile.write(str(G.edges())+'\n')
	return

def graph_dep(graph): #graph is a list
	for node in graph.nodes():
		fun=graph.node[node]['node_type']
		'''locals doesnt work
		as fun is an str object
		print(fun.type())
		if fun in locals():
			func=locals()[fun]
			func(node)
		'''
		if fun=="event_cond":
			event_cond(node)
		elif fun=="control_cond1":
			control_cond1(node)
		elif fun=="control_cond2":
			control_cond2(node)
		elif fun=="control_loop":
			control_loop(node)
		elif fun=="control_loop_cond":
			control_loop_cond(node)

#print("graphs for each file: ")
ind = 0
#settings.graphs_per_file=[]
for graphs_dict in per_file:
	ind+=1
	settings.OutputLogFile.write("Graphs dictionary for file no. "+str(ind)+" "+"filename: "+settings.allFolders[ind-1] +": (0 is stage and the following numbers are child objects of the stage)\n")
	print("Graphs dictionary for file no. "+str(ind)+" "+"filename: "+settings.allFolders[ind-1] +": (0 is stage and the following numbers are child objects of the stage)\n")
	graphs_per_obj={}
	for obj in graphs_dict: #here, obj is a number denoting the distinct object
		settings.OutputLogFile.write(str(obj)+":"+"\n")
		graphs_per_obj[obj] = []
		i=0
		for graph in graphs_dict[obj]:
			G=nx.DiGraph()
			G = create_nodes(graph)
			if(i==0):
				pass
				#print("Nodes: ",type(G.nodes()))
				#print(G.nodes())
			print("The nodes created are: ", G.nodes())
			for node in G.nodes(): #+str(G.node[node]['block_len'])
				print(str(G.node[node]).encode('utf-8','ignore'))
				settings.OutputLogFile.write(str(node)+" "+str(G.node[node]['node_type'])+"  "+'\n') #+str(G.node[node]['node_text'])
			graph_dep(G)
			graphs_per_obj[obj].append(G)
			i+=1
	settings.graphs_per_file.append(graphs_per_obj)
#settings.OutputLogFile.close()