import tkinter as tk
from ctypes import c_char
from tkinter import messagebox
Eingabe_liste = []
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
def clear():
    Eingabe_liste.clear()
def auf():
    Eingabe_liste.append("(")
def zu():
    Eingabe_liste.append(")")
def komma():
    Eingabe_liste.append(".")
def wurzel():
    Eingabe_liste.append("** 0.5")

### Die Idee ist das die Liste alle Elemente in ein print Befehl überführen für die ausgabe
### Die Herausforderung besteht unter ander m da rin das der pop befehl null immer überschriben wird.



def ist_gleich():
    rechnung= "".join(map(str, Eingabe_liste))
    ergebnis = eval(rechnung)
    ergebnis = round(float(ergebnis), 2)
    messagebox.showinfo("Dein Ergebnis ist",f"{ergebnis}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hallo Tkinter!")
    root.geometry("450x700")
    root.configure(bg="lightblue", highlightbackground="black", highlightthickness=5)


    button1 = tk.Button(

    root,
    text="1",
    command=eins_sagen,
    width=10,
    height=4,
    )
    button2 = tk.Button(
    root,
    text="2",
    command=zwei_sagen,
    width=10,
    height=4,
    )
    button3 = tk.Button(
    root,
    text="3",
    command=drei_sagen,
    width=10,
    height=4,
    )
    button4 = tk.Button(
    root,
    text="4",
    command=vier_sagen,
    width=10,
    height=4,
    )
    button5 = tk.Button(
    root,
    text="5",
    command=fuenf_sagen,
    width=10,
    height=4,
    )
    button6 = tk.Button(
    root,
    text="6",
    command=sechs_sagen,
    width=10,
    height=4,
    )
    button7 = tk.Button(
    root,
    text="7",
    command=sieben_sagen,
    width=10,
    height=4,
    )
    button8 = tk.Button(
    root,
    text="8",
    command=acht_sagen,
    width=10,
    height=4,
    )
    button9 = tk.Button(
    root,
    text="9",
    command=neun_sagen,
    width=10,
    height=4,
    )
    button0 = tk.Button(
    root,
    text="0",
    command=null_sagen,
    width=10,
    height=4,
    )
    button11 = tk.Button(
    root,
    text="=",
    command=ist_gleich,
    width=10,
    height=4,
    )
    button12 = tk.Button(
    root,
    text="+",
    command=plus,
    width=10,
    height=4,
    )
    button13 = tk.Button(
    root,
    text="-",
    command=minus,
    width=10,
    height=4,
    )
    button14 = tk.Button(
    root,
    text="/",
    command=teilen,
    width=10,
    height=4,
    )
    button15 = tk.Button(
    root,
    text="*",
    command=mal,
    width=10,
    height=4,
    )
    button16 = tk.Button(
    root,
    text="**",
    command=quadrat,
    width=10,
    height=4,
    )
    button17 = tk.Button(
    root,
    text="clear",
    command=clear,
    width=10,
    height=4,
    )
    button18 = tk.Button(
    root,
    text="(",
    command=auf,
    width=10,
    height=4,
    )
    button19 = tk.Button(
    root,
    text=")",
    command=zu,
    width=10,
    height=4,
    )
    button20 = tk.Button(
    root,
    text=",",
    command=komma,
    width=10,
    height=4,
    )
    button21 = tk.Button(
    root,
    text="√",
    command=wurzel,
    width=10,
    height=4,
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
    button17.pack()
    button17.place(x=200,y=500)
    button18.pack()
    button18.place(x=300,y=500)
    button19.pack()
    button19.place(x=100,y=600)
    button20.pack()
    button20.place(x=200,y=600)
    button21.pack()
    button21.place(x=300,y=600)

    label = tk.Label(root, text="", font=("Arial", 14))         #Leeres Label
    label.pack(pady=20)

root.mainloop()







