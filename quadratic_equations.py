from tkinter import *
from math import *
import numpy as np
import matplotlib.pyplot as plt

D=0
x1=0
x2=0
flag=False
t=0
a=0
b=0
c=0
def picture():
    x4 = np.arange(-3,9.5,0.5)
    y4 = (-1/12)*(x4-3)**2+6
    x5= np.arange(5,9,0.5)
    y5 = (1/9)*(x5-5)**2+2
    x6 = np.arange(5,8.5,0.5)
    y6 = (1/8)*(x6-7)**2+1.5
    x7 = np.arange(-13,-8.5,0.5)
    y7 = (-0.75)*(x7+11)**2+6
    x8 = np.arange(-15,-12.5,0.5)
    y8 = (-0.5)*(x8+13)**2+3
    x9 = np.arange(-15,-10,0.5)
    y9 = [1]*len(x9)
    x10 = np.arange(3,4,0.5)
    y10 = [3]*len(x10)
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title("Whale")

def graphics_table():
    flag,D,t=Answer()
    if flag==True:
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x = np.arange(x0-10, x0+10, 0.5)
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'g-d')
        plt.title('quadratic equations')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Top of the parabola ({x0},{y0})"
    else:
        text=f"Unable to plot"
    lbl_5.configure(text=f"D={D}\n{t}\n{text}")
def Answer(event):
    global D
    global x1
    global x2
    if (entry_1.get()!="" and entry_2.get()!="" and entry_3.get()!=""):
        a = entry_1.get()
        b = entry_2.get()
        c = entry_3.get()
        D = int(b)**2 - 4 * int(a) * int(c)
        if D>0:
            x1_=round((-1*b+sqrt(D))/(2*a),2)
            x2_=round((-1*b-sqrt(D))/(2*a),2)
            flag=True
            lbl_5.configure(text=f"D={D}\n x1={x1}\n x2={x2}")
        elif D==0:
            x1_=round((-1*b)/(2*a),2)
            lbl_5.configure(text=f"D={D}\n x1={x1}\n x2={x2}")
            flag=True
        else:
            t="Корней нет"
            flag=False
            lbl_5.configure(text=t)
    return D,flag,t
def graphics():
    t=0
def yet():
    global t
    if t==0:
        window.geometry(str(window.winfo_width())+"x"+str(window.winfo_height()+200))
        button_2.config(text="Reduce the window")
        t=1
    else:
        window.geometry(str(window.winfo_width())+"x"+str(window.winfo_height()-200))
        button_2.config(text="Enlarge window")

window = Tk()
window.title("quadratic equations")
window.geometry("500x500")
f1 = Frame(window,width=500,height=450)
f1.pack(side=TOP)
f2 = Frame(window,width=500,height=450)
f2.pack(side=BOTTOM)

lbl_1=Label(f1,text="quadratic equations",height=2,width=15,font="Arial 20",fg="#468499",bg="#DDDDDD",relief="solid")
lbl_2=Label(f1,text="x**2+",height=1,width=5,font="Arial 12",fg="#468499",bg="#DDDDDD",relief="solid")
lbl_3=Label(f1,text="x+",height=1,width=5,font="Arial 12",fg="#468499",bg="#DDDDDD",relief="solid")
lbl_4=Label(f1,text="=0",height=1,width=5,font="Arial 12",fg="#468499",bg="#DDDDDD",relief="solid")
lbl_5=Label(f1,text=f"D={D}\n x1={x1}\n x2={x2}",height=5,width=15,font="Arial 15",fg="#468499",bg="#DDDDDD",relief="solid")

entry_1=Entry(f1, width=5)
entry_2=Entry(f1, width=5)
entry_3=Entry(f1, width=5)

button_1=Button(f1,text="Answer",height=1,width=10,font="Arial 15",fg="#468499",bg="#DDDDDD",relief="solid")
button_2=Button(f2,text="Enlarge window",height=1,width=10,font="Arial 15",fg="#468499",bg="#DDDDDD", command=yet)

var = IntVar()
r1 = Radiobutton(f2,text="Whale",variable=var,var=1,font="Arial 15")
r2 = Radiobutton(f2,text="Glasses",variable=var,var=1,font="Arial 15")
r3 = Radiobutton(f2,text="Frog",variable=var,var=1,font="Arial 15")

lbl_1.pack()
lbl_5.pack()
entry_1.pack(side=LEFT)
lbl_2.pack(side=LEFT)
entry_2.pack(side=LEFT)
lbl_3.pack(side=LEFT)
entry_3.pack(side=LEFT)
lbl_4.pack(side=LEFT)
button_1.pack(side=RIGHT)
button_2.pack(side=TOP)
r1.pack()
r2.pack()
r3.pack()
button_1.bind("<Button-1>", Answer)






window.mainloop()
