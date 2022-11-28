from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("400x400")

opt = ["1", "2"]

frameA = Frame(window, highlightbackground="blue", highlightthickness=2, borderwidth=40)
frameA.pack()

value = StringVar()
value.set("...")

teks1 = Label(frameA, text = "Mode: ")
teks1.grid(row=0, column=0)
optmenu = ttk.Combobox(frameA, width=5, textvariable= value)
optmenu.grid(row=0, column=1)



teks2 = Label(frameA, text = "Connection: ")
teks2.grid(row=0, column=2)
optmenu2 = ttk.Combobox(frameA, width=5, textvariable= value)
optmenu2.grid(row=0, column=3)

teks3 = Label(frameA, text = "Subject: ")
teks3.grid(row=1, column=0)
optmenu3 = ttk.Combobox(frameA, width=5, textvariable= value)
optmenu3.grid(row=1, column=1)

teks4 = Label(frameA, text = "Remote IP: ")
teks4.grid(row=1, column=2)
optmenu4 = Entry(frameA, width=6)
optmenu4.grid(row=1, column=3)






window.mainloop()
