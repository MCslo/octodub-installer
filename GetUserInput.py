from Tkinter import *


class GetUserInput(object):
    selection = None

    def __init__(self, options, multiple):
        self.master = Tk()

        self.master.title("Choose from list")

        self.listbox = Listbox(self.master, selectmode=MULTIPLE if multiple else SINGLE, width=50, height=30)
        for option in options:
            self.listbox.insert(0, option)
        self.listbox.pack()
		
        

        		

        b = Button(self.master, command=self.callback, text="Submit")
		
		
        c = Button(self.master, command=self.quit, text="Cancel")
		
        b.pack()
        c.pack()
		
        self.master.mainloop()
		

    def callback(self):
        self.selection = self.listbox.selection_get()
        self.master.destroy()
    def quit(self):
		self.master.destroy()
    def getInput(self):		
        return self.selection