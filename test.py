from Tkinter import *

def callback():
	print listbox.selection_get()
	master.destroy()

	
master = Tk()

listbox = Listbox(master, selectmode=MULTIPLE)

def exit():
	master.destroy()

for option in ["Chrome","Zip7","Daemon tools"]:
	listbox.insert(0, option)
listbox.pack()

b= Button(master, command=callback, text="Submit")
c= Button(master, command=exit, text="Exit")
b.pack()
c.pack()

mainloop()