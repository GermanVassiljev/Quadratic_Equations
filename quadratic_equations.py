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
def pictureW():
    x1 = np.arange(0,9.5,0.5)
    y1 = (2/27)*x1*x1-3
    x2 = np.arange(-10,0.5,0.5)
    y2 = 0.04*x2*x2-3
    x3 = np.arange(-9,-2.5,0.5)
    y3 = (2/9)*(x3+6)**2+1
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
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def pictureG():
    x1 = np.arange(-9,-0.5,0.5)
    y1 = -1*(1/16)*(x1+5)**2+2
    x2 = np.arange(1,9.5,0.5)
    y2 = -1*(1/16)*(x2-5)**2+2
    x3 = np.arange(-9,-0.5,0.5)
    y3 = (1/4)*(x3+5)**2-3
    x4 = np.arange(1,9.5,0.5)
    y4 = (1/4)*(x4-5)**2-3
    x5= np.arange(-9,-5.5,0.5)
    y5 = -1*(x5+7)**2+5
    x6 = np.arange(6,9.5,0.5)
    y6 = -1*(x6-7)**2+5
    x7 = np.arange(-1,1.5,0.5)
    y7 = -1*0.5*(x7*x7)+1.5
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title("Glasses")
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def pictureF():
    x1 = np.arange(-7,7.5,0.5)
    y1 = -1*(3/49)*(x1*x1)+1
    x2 = np.arange(-7,7.5,0.5)
    y2 = (4/49)*(x2*x2)+1
    x3 = np.arange(-6.8,-1.5,0.5)
    y3 = -0.75*(x3+4)**2+11
    x4 = np.arange(2,7.3,0.5)
    y4 = -0.75*(x4-4)**2+11
    x5 = np.arange(-5.8,-2.3,0.5)
    y5 = -1*(x5+4)**2+9
    x6 = np.arange(2.8,6.3,0.5)
    y6 = -1*(x6-4)**2+9
    x7 = np.arange(-4,4.5,0.5)
    y7 = (4/9)*(x7*x7)-5
    x8 = np.arange(-5.2,5.7,0.5)
    y8 = (4/9)*(x8*x8)-9
    x9 = np.arange(-7,2.3,0.5)
    y9 = -1*(1/16)*(x9+3)**2-6
    x10 = np.arange(2.8,7.5,0.5)
    y10 = -1*(1/16)*(x10-3)**2-6
    x11 = np.arange(-7,0.5,0.5)
    y11 = (1/9)*(x11+4)**2-11
    x12 = np.arange(0,7.5,0.5)
    y12 = (1/9)*(x12-4)**2-11
    x13 = np.arange(4.5,7.7,0.5)
    y13 = -1*(x13-5)**2
    x14 = np.arange(-7.-4,0.5)
    y14 = -1*(x13+5)**2
    x15 = np.arange(-3,3.5,0.5)
    y15 = (2/9)*(x15*x15)+2
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15)
    plt.title("Glasses")
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

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
        t=0

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
r1 = Radiobutton(f2,text="Whale",variable=var,var=1,font="Arial 15",command=pictureW)
r2 = Radiobutton(f2,text="Glasses",variable=var,var=1,font="Arial 15",command=pictureG)
r3 = Radiobutton(f2,text="Frog",variable=var,var=1,font="Arial 15",command=pictureF)

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
