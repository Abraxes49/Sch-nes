import tkinter as tk
from ctypes import c_char
from tkinter import messagebox  #jo für die messagbox
Eingabe_liste = []
count = 0
def eins_sagen():
    Eingabe_liste.append(1)
def zwei_sagen():
    Eingabe_liste.append(2)
def drei_sagen():
    Eingabe_liste.append(3)
def vier_sagen():
    Eingabe_liste.append(4)
def fuenf_sagen():
    Eingabe_liste.append(5)
def sechs_sagen():
    Eingabe_liste.append(6)
def sieben_sagen():
    Eingabe_liste.append(7)
def acht_sagen():
    Eingabe_liste.append(8)
def neun_sagen():
    Eingabe_liste.append(9)
def null_sagen():
    Eingabe_liste.append(0)

def teilen():
    Eingabe_liste.append("/")
def mal():
    Eingabe_liste.append("*")
def plus():
    Eingabe_liste.append("+")
def minus():
    Eingabe_liste.append("-")
def quadrat():
    Eingabe_liste.append("**")

def ist_gleich():
    print(Eingabe_liste)  # Platzhalter

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hallo Tkinter!")
    root.geometry("400x600")

    button1 = tk.Button(

    root,
    text="1",
    command=eins_sagen,
    width=5,
    height=2,
    )
    button2 = tk.Button(
    root,
    text="2",
    command=zwei_sagen,
    width=5,
    height=2,
    )
    button3 = tk.Button(
    root,
    text="3",
    command=drei_sagen,
    width=5,
    height=2,
    )
    button4 = tk.Button(
    root,
    text="4",
    command=vier_sagen,
    width=5,
    height=2,
    )
    button5 = tk.Button(
    root,
    text="5",
    command=fuenf_sagen,
    width=5,
    height=2,
    )
    button6 = tk.Button(
    root,
    text="6",
    command=sechs_sagen,
    width=5,
    height=2,
    )
    button7 = tk.Button(
    root,
    text="7",
    command=sieben_sagen,
    width=5,
    height=2,
    )
    button8 = tk.Button(
    root,
    text="8",
    command=acht_sagen,
    width=5,
    height=2,
    )
    button9 = tk.Button(
    root,
    text="9",
    command=neun_sagen,
    width=5,
    height=2,
    )
    button0 = tk.Button(
    root,
    text="0",
    command=null_sagen,
    width=5,
    height=2,
    )
    button11 = tk.Button(
    root,
    text="=",
    command=ist_gleich,
    width=5,
    height=2,
    )
    button12 = tk.Button(
    root,
    text="+",
    command=plus,
    width=5,
    height=2,
    )
    button13 = tk.Button(
    root,
    text="-",
    command=minus,
    width=5,
    height=2,
    )
    button14 = tk.Button(
    root,
    text="/",
    command=teilen,
    width=5,
    height=2,
    )
    button15 = tk.Button(
    root,
    text="*",
    command=mal,
    width=5,
    height=2,
    )
    button16 = tk.Button(
    root,
    text="**",
    command=quadrat,
    width=5,
    height=2,
    )

    button1.pack()
    button1.place(x=100,y=0)
    button2.pack()
    button2.place(x=200,y=0)
    button3.pack()
    button3.place(x=300,y=0)
    button4.pack()
    button4.place(x=100,y=100)
    button5.pack()
    button5.place(x=200,y=100)
    button6.pack()
    button6.place(x=300,y=100)
    button7.pack()
    button7.place(x=100,y=200)
    button8.pack()
    button8.place(x=200,y=200)
    button9.pack()
    button9.place(x=300,y=200)
    button11.pack()
    button11.place(x=100,y=300)
    button0.pack()
    button0.place(x=200,y=300)
    button12.pack()
    button12.place(x=300,y=300)
    button13.pack()
    button13.place(x=100,y=400)
    button14.pack()
    button14.place(x=200,y=400)
    button15.pack()
    button15.place(x=300,y=400)
    button16.pack()
    button16.place(x=100,y=500)
    root.mainloop()



