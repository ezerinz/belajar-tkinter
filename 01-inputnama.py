from tkinter import *

nama = []
root = Tk()
root.geometry("290x300")

lbl = Label(root, text="Masukkan Nama: ")
lbl.grid(column=0)

etr = Entry(root)
etr.grid(row=0, column=1)

def cmd():
    getEntry = etr.get()
    nama.append(getEntry)
    nma = Listbox(root, width=35)

    for i in range(len(nama)):
        nma.insert(i+1, nama[i])

    nma.grid(row=2, columnspan=2)


btn = Button(root, text="Tambah", command=cmd)
btn.grid(row=1, column=0)

root.mainloop()
