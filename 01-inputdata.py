from tkinter import *

nama = []
umur = []
alamat = []
root = Tk()
root.geometry("450x450")

frameInput = Frame(root)
frameInput.grid(row=0, column=0)

frameList = Frame(root)
frameList.grid(row=1, column=0)


lbl1 = Label(frameInput, text="Masukkan Nama: ")
lbl1.grid(row= 0, column=0)

etr1 = Entry(frameInput)
etr1.grid(row=0, column=1)


def tmbhnama():
    getNama = etr1.get()
    nama.append(getNama)
    nma = Listbox(frameList)

    for i in range(len(nama)):
        nma.insert(i+1, nama[i])

    nma.grid(row=0, column=0)


btn1 = Button(frameInput, text=" + ", command = tmbhnama)
btn1.grid(row=0, column=2)



lbl2 = Label(frameInput, text="Masukkan Umur: ")
lbl2.grid(row= 1, column=0)

etr2 = Spinbox(frameInput, from_=1, to=50, width=19)
etr2.grid(row=1, column=1)


def tmbhumur():
    getUmur = etr2.get()
    umur.append(getUmur)
    umr = Listbox(frameList)

    for i in range(len(umur)):
        umr.insert(i+1, umur[i])

    umr.grid(row=0, column=1)


btn2 = Button(frameInput, text=" + ", command = tmbhumur)
btn2.grid(row=1, column=2)


lbl3 = Label(frameInput, text="Masukkan Nama: ")
lbl3.grid(row= 2, column=0)

etr3 = Entry(frameInput)
etr3.grid(row=2, column=1)


def tmbhalamat():
    getAlamat = etr3.get()
    alamat.append(getAlamat)
    almat = Listbox(frameList)

    for i in range(len(alamat)):
        almat.insert(i+1, alamat[i])

    almat.grid(row=0, column=2)


btn3 = Button(frameInput, text=" + ", command = tmbhalamat)
btn3.grid(row=2, column=2)




root.mainloop()
