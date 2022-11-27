from tkinter import *

root = Tk()
root.geometry("400x300")

lbl = Label(root, text="Masukkan Nama: ")
lbl.grid(column=0)

etr = Entry(root)
etr.grid(row=0, column=1)

def cmd():
    t = StringVar()
    t.set(etr.get())
    Entry(root, textvariable=t).grid(row=3, column=1)

btn = Button(root, text="Tambah", command=cmd)
btn.grid(row=1, column=0)

lbl2 = Label(root, text="Masukkan Nama Kedua: ")
lbl2.grid(row=3, column=0)

etr2 = Entry(root)
etr2.grid(row=3, column=1)



root.mainloop()
