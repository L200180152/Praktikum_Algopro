from Tkinter import *
bgeo = Tk(className="Bangun Geometri")

judul = Label(bgeo, text="Bangun Geometri, Segi empat/ persegi panjang", font="Times, 24", padx=10, pady=10)
judul.grid(row=0)

des = Label(bgeo, font="Times, 12", justify=CENTER
, padx=10)
des.grid(row=1)

L1 = Label(bgeo, font="Times, 12", text="panjang :", padx=10)
L1.place(x=85, y=170)

L2 = Label(bgeo, font="Times, 12", text="lebar :", padx=10)
L2.place(x=85, y=200)

E1 = Entry(bgeo, font="Times, 12")
E1.place(x=175, y=170, height=30)

E2 = Entry(bgeo, font="Times, 12")
E2.place(x=175, y=200, height=30)

def hitung():
    panjang = float(E1.get())
    lebar = float (E2.get())
    hasil = panjang * lebar
    luas.config(text=hasil)
    
B = Button(bgeo, text="Hitung Luas", command=hitung, font="Times 14", justify=CENTER)
B.place(x=85, y=230)

L2 = Label(bgeo, text="Luas = ", font="Times 14 bold")
L2.place(x=200, y=235)

luas = Label(bgeo, font="Times 14 bold")
luas.place(x=265, y=235)

bgeo.mainloop()
