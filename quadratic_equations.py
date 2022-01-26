from tkinter import *
from math import *

window = Tk()
window.title("quadratic equations")
window.geometry("500x500")

D=0
x1=0
x2=0

a=0
b=0
c=0

lbl_1=Label(window,text="quadratic equations",height=2,width=15,font="Arial 20",fg="#468499",bg="#DDDDDD",relief="solid")
lbl_2=Label(window,text="x**2+",height=1,width=5,font="Arial 12",fg="#468499",bg="#DDDDDD",relief="solid")
lbl_3=Label(window,text="x+",height=1,width=5,font="Arial 12",fg="#468499",bg="#DDDDDD",relief="solid")
lbl_4=Label(window,text="=0",height=1,width=5,font="Arial 12",fg="#468499",bg="#DDDDDD",relief="solid")
lbl_5=Label(window,text=f"D={D}\n x1={x1}\n x2={x2}",height=5,width=15,font="Arial 15",fg="#468499",bg="#DDDDDD",relief="solid")

entry_1=Entry(window, width=5)
entry_2=Entry(window, width=5)
entry_3=Entry(window, width=5)

button_1=Button(window,text="Answer",height=1,width=10,font="Arial 15",fg="#468499",bg="#DDDDDD",relief="solid")


def Answer(event):
    a = entry_1.get()
    b = entry_2.get()
    c = entry_3.get()
    global D
    global x1
    global x2
    D = int(b)**2 - 4 * int(a) * int(c)
    D2=sqrt(D)
    x1=-b+D2/2*a
    x2=-b-D2/2*a
    lbl_5.configure(text=f"D={D}\n x1={x1}\n x2={x2}")


lbl_1.pack()
lbl_5.pack()
entry_1.pack(side=LEFT)
lbl_2.pack(side=LEFT)
entry_2.pack(side=LEFT)
lbl_3.pack(side=LEFT)
entry_3.pack(side=LEFT)
lbl_4.pack(side=LEFT)
button_1.pack(side=RIGHT)
button_1.bind("<Button-1>", Answer)






window.mainloop()