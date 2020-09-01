from tkinter import *

window = Tk()
text = Text(window)
window.title("Python GUI App")
window.configure(width=500, height=300)
window.configure(bg='lightgray')

# move window center
winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

text = Text(window)
text.insert(INSERT, "Hei jeg heter Mikkel.")
text.insert(END, " Hva heter du?")


text.pack()
text.tag_add("Hei","1.0","100.0")

text.tag_config("Hei", background="yellow", foreground="black")

window.mainloop()