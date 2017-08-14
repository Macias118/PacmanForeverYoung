from tkinter import *

class World(Frame):

	def __init__(self, master=None):
		self.master = master
		Frame.__init__(self, self.master)
		self.pack()
		self.master.title("PACMAN FOREVER YOUNG")
		self.master.minsize(800, 600)

		self.create_button()
		self.create_label()

	def create_button(self):
		self.Quit = Button(self)
		self.Quit["text"] = "QUIT"
		self.Quit["fg"] = "red"
		self.Quit["command"] = self.quit
		self.Quit.pack({"side": "left"})

	def create_label(self):
		self.Label = Label(self.master, text="Jo żem wykonał te gre. Jo!", bd=15, highlightbackground="blue", highlightthickness=20, state=ACTIVE, activebackground="green", width=700, font=("Lato", 40))
		self.Label.pack(side="bottom")

root = Tk()
game = World(master=root)
game.mainloop()
