from tkinter import *

def button_pressed(num):

    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def button_equals():
    try:
        global equation_text

        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Math Error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""
    except Exception:
        equation_label.set("Error")
        equation_text = ""


def button_clear():

    global equation_text

    equation_text = ""
    equation_label.set(equation_text)

window = Tk()
window.title("Calculator")
window.geometry("500x500+0+0")
window.config(bg="#26242f")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label,font=('Consolas',20),bg="#202020",fg="white",width=23,height=2,anchor="e")
label.pack()

frame = Frame(window,bg="#202020")
frame.pack()

button1 = (Button(frame,text=1,height=3,width=7,font=35,activebackground="#26242f",bg="#202020",fg="white",command=lambda: button_pressed(1))
           .grid(row=0,column=0))
button2 = (Button(frame,text=2,height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed(2)).
           grid(row=0,column=1))
button3 = (Button(frame,text=3,height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed(3)).
           grid(row=0,column=2))
button4 = (Button(frame,text=4,height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed(4)).
           grid(row=1,column=0))
button5 = (Button(frame,text=5,height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed(5)).
           grid(row=1,column=1))
button6 = (Button(frame,text=6,height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed(6)).
           grid(row=1,column=2))
button7 = (Button(frame,text=7,height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed(7)).
           grid(row=2,column=0))
button8 = (Button(frame,text=8,height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed(8)).
           grid(row=2,column=1))
button9 = (Button(frame,text=9,height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed(9)).
           grid(row=2,column=2))
button0 = (Button(frame,text=0,height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed(0)).
           grid(row=3,column=0))
decimal = (Button(frame,text=".",height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed(".")).
           grid(row=3,column=1))
equalsto = (Button(frame,text="=",height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=button_equals).
            grid(row=3,column=2))
plus = (Button(frame,text="+",height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed("+")).
        grid(row=0,column=3))
minus = (Button(frame,text="-",height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed("-")).
         grid(row=1,column=3))
multiply = (Button(frame,text="*",height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed("*")).
            grid(row=2,column=3))
divide = (Button(frame,text="/",height=3,width=7,font=35,bg="#202020",fg="white",activebackground="#26242f",command=lambda: button_pressed("/")).
          grid(row=3,column=3))
clear = (Button(frame,text="C",height=3,width=10,font=35,bg="#202020",fg="white",activebackground="#26242f",command=button_clear).
         grid(row=4,column=1,columnspan=2))


window.mainloop()