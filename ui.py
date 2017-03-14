import tkinter
from tkinter import filedialog
from tkinter import Frame, Tk, BOTH, Text, Menu, END
import settings
settings.init()
import run
import os
root = tkinter.Tk()
root.geometry("1000x600+100+100")
root.title("Main window")
# create a main window


label1=tkinter.Label(root,text="Please select the folder containing the scratch files")#,bg='blue')
label1.pack()
# folder="init"
def run_it():
	run.run()
	# button4.pack()
	show_results()
	# print("Yo this is running with ",settings.folder)


def enable_run_button():
	global button3
	button3.pack()


# def readFile(filename):
    

def show_results():
	# dg = filedialog.Open()
	f = open(settings.folder+"/logs/res_min.txt", "r")
	text = f.read()
	txt = Text()
	txt.pack(fill=BOTH, expand=1)
	# return text
	txt.insert(END, text)



def change() :
	# root = tk.Tk()
	# root.withdraw()
	# global folder
	settings.folder = filedialog.askdirectory()
	newpath = settings.folder+"/logs"
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	settings.OutputLogFile = open(settings.folder+"\\logs\\OutputLogFile.txt",'w',encoding='utf-8')
	# print(file_path)
	# return file_path
	enable_run_button()

button1 = tkinter.Button(root, text='Browse directory',#background='red',
	command=change)

button3 = tkinter.Button(root, text='Run plagiarism detection', #background='red',
	command=run_it)

# button3 = tkinter.Button(root, text='Run plagiarism detection', #background='red',
# 	command=show_results)

	# button2 = tkinter.Button(root, text='Exit', background='red',
	# 	command=root.quit)


button1.pack()
# print("hey ",folder)
# button2.pack()
tkinter.mainloop()
