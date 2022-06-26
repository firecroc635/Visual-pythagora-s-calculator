from tkinter import *
from PIL import ImageTk, Image
from turtle import *
import math
#opening directory
import os
bik = os.path.dirname(os.path.abspath(__file__))
print(bik)
os.chdir(bik)
    #title and icon
root = Tk()
root.title('Menu')

def sous():
    top = Toplevel()
    top.title('Regular calculator')
    e = Entry(top, width=40, borderwidth=5)
    e.grid(row=1, column=1, columnspan=6)
    b = Entry(top, width= 40, borderwidth=5)
    b.grid(row=3, column=1, columnspan=6)
    global sign
    global number
    global lab
    sign = "?"
    sig = Label(top, text="operation: " + sign)
    sig.config(font=("Courier", 12))
    sig.grid(row=2, column = 1, columnspan=4)
    number = 0
    emp = Label(top, text="").grid(row=5, column=0)
    emp2 = Label(top, text="").grid(row=5, column=10)
    lab = Label(top, text= "result: " + str(number))
    lab.grid(row=4, column=3)
    lab.config(font=("Courier", 8))

    def plus():
        global j
        print("plus")
        j = 1
        sign = "+"
        sig.config(text = "operation: " + sign)

    def minus():
        global j
        print("minus")
        j = 2
        sign = "-"
        sig.config(text = "operation: " + sign)

    def multiple():
        global j
        print("multiple")
        j = 3
        sign = "*"
        sig.config(text = "operation: " + sign)

    def devide():
        global j
        print("devide")
        j = 4
        sign = "/"
        sig.config(text = "operation: " + sign)

    def calculate(number):
        global j
        global lab
        t1=int(e.get())
        t2=int(b.get())
        print(j, t1, t2)
        if j == 1:
            number = t1 + t2
        elif j == 2:
            number = t1 - t2
        elif j == 3:
            number = t1 * t2
        elif j == 4:
            number = t1 / t2
        else:
            print("cow")
        number = str(number)
        lab.config(text="result: " + number)
        #button_cal['state'] = DISABLED

    button_plus = Button(top, text = "+", padx = 10, command =lambda: plus(), borderwidth=5 ).grid(row = 4, column = 1)
    button_minus = Button(top, text = "-", padx = 10, command = lambda: minus(), borderwidth=5 ).grid(row = 4, column = 2)
    button_multiple = Button(top, text = "*", padx = 10, command = lambda: multiple(), borderwidth=5 ).grid(row = 4, column = 4,)
    button_devide = Button(top, text = "/", padx = 10, command = lambda: devide(), borderwidth=5 ).grid(row = 4, column = 5)

    button_cal = Button(top, text = "calculate", command = lambda: calculate(e.get), pady=20, borderwidth=5)
    button_cal.grid(row = 0, column = 7, rowspan=4)
def tri():
    gop = Toplevel()

    def hypo():
        top = Toplevel()
        top.title("hypotenus")
        a = Entry(top, width = 40, borderwidth=5)
        labe_1=Label(top, text="A:")
        labe_1.grid(row=0, column=0)
        labe_1.config(font=("Arial, 15"))
        a.grid(row=1, column=1, columnspan=5)
        b = Entry(top, width = 40, borderwidth=5)
        labe=Label(top, text="B:")
        labe.grid(row=2, column=0)
        labe.config(font=("Arial, 15"))
        b.grid(row=3, column=1, columnspan=5)

        img = ImageTk.PhotoImage(Image.open("rat_regular.png"))
        imagae = Label(top, image=img)
        imagae.image = img
        imagae.grid(row=4, column=0, columnspan=10)
        def dig():
            t1 = int(b.get())
            t2 = int(a.get())
            if t1 and t2:
                #calculation end
                I_hate_this = round(math.sqrt((t1 ** 2)+(t2 ** 2)), 2)
                #drawing time YAY!!!! DRAWING!!!
                drwa = Screen()
                y1 = t1
                y2 = t2
                drwa.setup(width=500, height=250)
                word="Result = " + str(I_hate_this)
                forum = "Formula: sqrt(a^2 + b^2)"
                penup()
                goto(-240,75)
                pendown()
                write(word, move=False, font=('Arial', 30, 'normal'))
                penup()
                goto(-235,50)
                pendown()
                write(forum, move=False, font=('Arial', 18, 'normal'))
                width(3)
                penup()
                goto(-175,-80 + 25)
                if y1 == y2:
                    pendown()
                    goto(-175, 20 + 25)
                    goto(-75, -80 + 25)
                    goto(-175, -80 + 25)
                    goto(-175, -30 +25)
                    goto(-186, -30 + 25)
                    penup()
                    goto(-205, -35 + 25)
                    ko = t2
                    if t2 > 100:
                        goto(-218, -35 +25)
                    write(ko, move=False, font=('Arial', 10, 'normal'))
                    goto(-125, -80 + 25)
                    pendown()
                    goto(-125, -99 + 25)
                    penup()
                    goto(-125, -114 + 25)
                    write(ko, move=False, font=('Arial', 10, 'normal'), align="center")
                    goto(0,0)
                elif y1 < y2:
                    goto(-175, 20 + 8)
                    pendown()
                    goto(-25, -50 + 8)
                    goto(-175, -50 + 8)
                    goto(-175, 20 +8)
                    goto(-175, 8)
                    goto(-186, 0 + 8)
                    penup()
                    goto(-205, 5 + 8)
                    ko = t2
                    if t2 > 100:
                        goto(-218, 5 +8)
                    write(po, move=False, font=('Arial', 10, 'normal'))
                    goto(-100, -50 + 8)
                    pendown()
                    goto(-100, -69 + 8)
                    penup()
                    goto(-100, -84 + 8)
                    po = t1
                    write(ko, move=False, font=('Arial', 10, 'normal'), align="center")
                    goto(0,0)
                else:
                    goto(50, -80 + 25)
                    pendown()
                    goto(50, 20 + 25)
                    goto(80, -80 + 25)
                    goto(50, -80 + 25)
                    goto(50, -30 +25)
                    goto(39, -30 + 25)
                    penup()
                    goto(20, -35 + 25)
                    ko = t2
                    po = t1
                    if t2 > 100:
                        goto(7, -35 +25)
                    write(ko, move=False, font=('Arial', 10, 'normal'))
                    goto(65, -80 + 25)
                    pendown()
                    goto(65, -99 + 25)
                    penup()
                    goto(65, -114 + 25)
                    write(po, move=False, font=('Arial', 10, 'normal'), align="center")
                    goto(0,0)
            else:
                print("hah")

        botan = Button(top, text='calculate', borderwidth=5, padx=10, command=dig).grid(row=5,column=0,columnspan=20)
    def leg():
        top = Toplevel()
        top.title("Leg finder")
        a = Entry(top, width = 40, borderwidth=5)
        labe_1=Label(top, text="A:")
        labe_1.grid(row=0, column=0)
        labe_1.config(font=("Arial, 15"))
        a.grid(row=1, column=1, columnspan=5)
        b = Entry(top, width = 40, borderwidth=5)
        labe=Label(top, text="C:")
        labe.grid(row=2, column=0)
        labe.config(font=("Arial, 15"))
        b.grid(row=3, column=1, columnspan=5)

        img = ImageTk.PhotoImage(Image.open("fe.png"))
        imagae = Label(top, image=img)
        imagae.image = img
        imagae.grid(row=4, column=0, columnspan=10)
        def dig():
            t1 = int(b.get())
            t2 = int(a.get())
            if t1 and t2:
                #calculation end
                I_hate_this = round(math.sqrt((t1 ** 2)-(t2 ** 2)), 2)
                #drawing time YAY!!!! DRAWING!!!
                drwa = Screen()
                y1 = I_hate_this
                y2 = t2
                drwa.setup(width=500, height=250)
                word="Result = " + str(I_hate_this)
                forum = "Formula: sqrt(C^2 - b^2)"
                penup()
                goto(-240,75)
                pendown()
                write(word, move=False, font=('Arial', 30, 'normal'))
                penup()
                goto(-235,50)
                pendown()
                write(forum, move=False, font=('Arial', 18, 'normal'))
                width(3)
                penup()
                goto(-175,-80 + 25)
                if y1 == y2:
                    pendown()
                    goto(-175, 20 + 25)
                    goto(-75, -80 + 25)
                    goto(-175, -80 + 25)
                    goto(-175, -30 +25)
                    goto(-186, -30 + 25)
                    penup()
                    goto(-205, -35 + 25)
                    ko = y2
                    if y2 > 100:
                        goto(-218, -35 +25)
                    write(ko, move=False, font=('Arial', 10, 'normal'))
                    goto(-125, -80 + 25)
                    pendown()
                    goto(-125, -99 + 25)
                    penup()
                    goto(-125, -114 + 25)
                    write(ko, move=False, font=('Arial', 10, 'normal'), align="center")
                    goto(0,0)
                elif y1 < y2:
                    goto(-175, 20 + 8)
                    pendown()
                    goto(-25, -50 + 8)
                    goto(-175, -50 + 8)
                    goto(-175, 20 +8)
                    goto(-175, 8)
                    goto(-186, 0 + 8)
                    penup()
                    goto(-205, 5 + 8)
                    ko = y2
                    if t2 > 100:
                        goto(-218, 5 +8)
                    write(ko, move=False, font=('Arial', 10, 'normal'))
                    goto(-100, -50 + 8)
                    pendown()
                    goto(-100, -69 + 8)
                    penup()
                    goto(-100, -84 + 8)
                    po = y1
                    write(po, move=False, font=('Arial', 10, 'normal'), align="center")
                    goto(0,0)
                else:
                    goto(50, -80 + 25)
                    pendown()
                    goto(50, 20 + 25)
                    goto(80, -80 + 25)
                    goto(50, -80 + 25)
                    goto(50, -30 +25)
                    goto(39, -30 + 25)
                    penup()
                    goto(20, -35 + 25)
                    ko = y2
                    po = y1
                    if t2 > 100:
                        goto(7, -35 +25)
                    write(ko, move=False, font=('Arial', 10, 'normal'))
                    goto(65, -80 + 25)
                    pendown()
                    goto(65, -99 + 25)
                    penup()
                    goto(65, -114 + 25)
                    write(po, move=False, font=('Arial', 10, 'normal'), align="center")
                    goto(0,0)
            else:
                print("hah")

        botan = Button(top, text='calculate', borderwidth=5, padx=10, command=dig).grid(row=5,column=0,columnspan=20)
    def area():
        top = Toplevel()
        top.title("Area")
        a = Entry(top, width = 40, borderwidth=5)
        labe_1=Label(top, text="A:")
        labe_1.grid(row=0, column=0)
        labe_1.config(font=("Arial, 15"))
        a.grid(row=1, column=1, columnspan=5)
        b = Entry(top, width = 40, borderwidth=5)
        labe=Label(top, text="B:")
        labe.grid(row=2, column=0)
        labe.config(font=("Arial, 15"))
        b.grid(row=3, column=1, columnspan=5)

        img = ImageTk.PhotoImage(Image.open("was.png"))
        imagae = Label(top, image=img)
        imagae.image = img
        imagae.grid(row=4, column=0, columnspan=10)
        def dig():
            t1 = float(b.get())
            t2 = float(a.get())
            if t1 and t2:
                #calculation end
                I_hate_this = round((t1 * t2) / 2, 2)
                #drawing time YAY!!!! DRAWING!!!
                drwa = Screen()
                y1 = t1
                y2 = t2
                drwa.setup(width=500, height=250)
                word="Result = " + str(I_hate_this)
                forum = "Formula: a * b / 2"
                penup()
                goto(-240,75)
                pendown()
                write(word, move=False, font=('Arial', 30, 'normal'))
                penup()
                goto(-235,50)
                pendown()
                write(forum, move=False, font=('Arial', 18, 'normal'))
                width(3)
                penup()
                goto(-175,-80 + 25)
                if y1 == y2:
                    pendown()
                    goto(-175, 20 + 25)
                    goto(-75, -80 + 25)
                    goto(-175, -80 + 25)
                    goto(-175, -30 +25)
                    goto(-186, -30 + 25)
                    penup()
                    goto(-205, -35 + 25)
                    ko = t2
                    if t2 > 100:
                        goto(-218, -35 +25)
                    write(ko, move=False, font=('Arial', 10, 'normal'))
                    goto(-125, -80 + 25)
                    pendown()
                    goto(-125, -99 + 25)
                    penup()
                    goto(-125, -114 + 25)
                    write(ko, move=False, font=('Arial', 10, 'normal'), align="center")
                    goto(0,0)
                elif y1 < y2:
                    goto(-175, 20 + 8)
                    pendown()
                    goto(-25, -50 + 8)
                    goto(-175, -50 + 8)
                    goto(-175, 20 +8)
                    goto(-175, 8)
                    goto(-186, 0 + 8)
                    penup()
                    goto(-205, 5 + 8)
                    ko = t2
                    if t2 > 100:
                        goto(-218, 5 +8)
                    write(ko, move=False, font=('Arial', 10, 'normal'))
                    goto(-100, -50 + 8)
                    pendown()
                    goto(-100, -69 + 8)
                    penup()
                    goto(-100, -84 + 8)
                    po = t1
                    write(po, move=False, font=('Arial', 10, 'normal'), align="center")
                    goto(0,0)
                else:
                    goto(50, -80 + 25)
                    pendown()
                    goto(50, 20 + 25)
                    goto(80, -80 + 25)
                    goto(50, -80 + 25)
                    goto(50, -30 +25)
                    goto(39, -30 + 25)
                    penup()
                    goto(20, -35 + 25)
                    ko = t2
                    if t2 > 100:
                        goto(7, -35 +25)
                    write(ko, move=False, font=('Arial', 10, 'normal'))
                    goto(65, -80 + 25)
                    pendown()
                    goto(65, -99 + 25)
                    penup()
                    goto(65, -114 + 25)
                    write(ko, move=False, font=('Arial', 10, 'normal'), align="center")
                    goto(0,0)
            else:
                print("hah")

        botan = Button(top, text='calculate', borderwidth=5, padx=10, command=dig).grid(row=5,column=0,columnspan=20)
    def peri():
        top = Toplevel()
        top.title("perimeter")
        a = Entry(top, width = 40, borderwidth=5)
        labe_1=Label(top, text="A:")
        labe_1.grid(row=0, column=0)
        labe_1.config(font=("Arial, 15"))
        a.grid(row=1, column=1, columnspan=5)
        b = Entry(top, width = 40, borderwidth=5)
        labe=Label(top, text="B:")
        labe.grid(row=2, column=0)
        labe.config(font=("Arial, 15"))
        b.grid(row=3, column=1, columnspan=5)

        img = ImageTk.PhotoImage(Image.open("kool.png"))
        imagae = Label(top, image=img)
        imagae.image = img
        imagae.grid(row=4, column=0, columnspan=10)
        def dig():
            t1 = int(b.get())
            t2 = int(a.get())
            if t1 and t2:
                #calculation end
                ber = round(math.sqrt((t1 ** 2)+(t2 ** 2)), 2)
                I_hate_this = ber + t1 + t2
                #drawing time YAY!!!! DRAWING!!!
                drwa = Screen()
                y1 = t1
                y2 = t2
                drwa.setup(width=500, height=250)
                word="Result = " + str(I_hate_this)
                forum = "Formula: sqrt(a^2 + b^2) = c + b + a"
                penup()
                goto(-240,75)
                pendown()
                write(word, move=False, font=('Arial', 30, 'normal'))
                penup()
                goto(-235,50)
                pendown()
                write(forum, move=False, font=('Arial', 18, 'normal'))
                width(3)
                penup()
                goto(-175,-80 + 25)
                if y1 == y2:
                    pendown()
                    goto(-175, 20 + 25)
                    goto(-75, -80 + 25)
                    goto(-175, -80 + 25)
                    goto(-175, -30 +25)
                    goto(-186, -30 + 25)
                    penup()
                    goto(-205, -35 + 25)
                    ko = t2
                    if t2 > 100:
                        goto(-218, -35 +25)
                    write(ko, move=False, font=('Arial', 10, 'normal'))
                    goto(-125, -80 + 25)
                    pendown()
                    goto(-125, -99 + 25)
                    penup()
                    goto(-125, -114 + 25)
                    write(ko, move=False, font=('Arial', 10, 'normal'), align="center")
                    goto(0,0)
                elif y1 < y2:
                    goto(-175, 20 + 8)
                    pendown()
                    goto(-25, -50 + 8)
                    goto(-175, -50 + 8)
                    goto(-175, 20 +8)
                    goto(-175, 8)
                    goto(-186, 0 + 8)
                    penup()
                    goto(-205, 5 + 8)
                    ko = t2
                    if t2 > 100:
                        goto(-218, 5 +8)
                    write(po, move=False, font=('Arial', 10, 'normal'))
                    goto(-100, -50 + 8)
                    pendown()
                    goto(-100, -69 + 8)
                    penup()
                    goto(-100, -84 + 8)
                    po = t1
                    write(ko, move=False, font=('Arial', 10, 'normal'), align="center")
                    goto(0,0)
                else:
                    goto(50, -80 + 25)
                    pendown()
                    goto(50, 20 + 25)
                    goto(80, -80 + 25)
                    goto(50, -80 + 25)
                    goto(50, -30 +25)
                    goto(39, -30 + 25)
                    penup()
                    goto(20, -35 + 25)
                    ko = t2
                    po = t1
                    if t2 > 100:
                        goto(7, -35 +25)
                    write(ko, move=False, font=('Arial', 10, 'normal'))
                    goto(65, -80 + 25)
                    pendown()
                    goto(65, -99 + 25)
                    penup()
                    goto(65, -114 + 25)
                    write(po, move=False, font=('Arial', 10, 'normal'), align="center")
                    goto(0,0)
            else:
                print("hah")

        botan = Button(top, text='calculate', borderwidth=5, padx=10, command=dig).grid(row=5,column=0,columnspan=20)
    leb = Label(gop, text=" ").grid(row=0, column=1)
    leb = Label(gop, text=" ").grid(row=0, column=3)
    bu = Button(gop, text="Hypotenus", command= lambda: hypo())
    bu.grid(row=0, column=0)
    gu = Button(gop, text="Legs finder", command= lambda: leg())
    gu.grid(row=0, column=2)
    tu = Button(gop, text="Area", command=lambda: area())
    tu.grid(row=0, column=4)
    du = Button(gop, text="perimeter", command=lambda: peri())
    du.grid(row=1, column=2)
def poli():
    print("poly")
def circle():
    print("roundi")

root.geometry("150x100")
lab = Label(root, text="     ").grid(row=0, column=0)
button_1 = Button(root, text="simple calculator", command= sous).grid(row=0, column=0)
button_2 = Button(root, text="right angle", command= tri).grid(row=1, column=0)

root.mainloop()
