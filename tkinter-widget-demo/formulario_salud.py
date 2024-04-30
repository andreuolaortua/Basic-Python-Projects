from tkinter import *

window = Tk()
window.title("FORMULARIO")
window.minsize(width=500, height=500)
window.config(bg="white")

name = Label(text="Name")
name.config(text="New")
name.pack()

entry_name = Entry()
entry_name.insert(END, string="Some text")
print(entry_name.get())
entry_name.pack()
#edat, pes, dies de execici,








window.mainloop()


