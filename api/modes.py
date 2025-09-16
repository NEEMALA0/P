from tkinter import *

window = Tk()
window.title("Toggle Switch")
window.geometry("400x600")
window.config(bg="white")

button_mode = True

def customize():
    global button_mode

    if button_mode:
        button.config(image=dark_mode,bg="#26242f",activebackground="#26242f")
        window.config(bg="#26242f")
        button_mode = False
    else:
        button.config(image=light_mode,bg="white",activebackground="white")
        window.config(bg="white")
        button_mode = True

light_mode = PhotoImage(file="C:/Users/Hp/Pictures/WEB/light_mode.png")
dark_mode = PhotoImage(file="C:/Users/Hp/Pictures/WEB/dark_mode.png")

button = Button(window,image=light_mode,bd=0,bg="white",activebackground="white",command=customize)
button.pack(padx=50,pady=50)

window.mainloop()