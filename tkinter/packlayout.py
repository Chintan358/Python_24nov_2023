from tkinter import *

root = Tk()
root.title("My app")
root.geometry("500x500")

btn1= Button(text="Button1").pack(side=LEFT)

btn2= Button(text="Button2").pack(side=RIGHT)

btn3= Button(text="Button3").pack(side=TOP)

btn4= Button(text="Button4").pack(side=BOTTOM)

root.mainloop()




