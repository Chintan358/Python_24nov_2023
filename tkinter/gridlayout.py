from tkinter import *

root = Tk()
root.title("My app")
root.geometry("500x500")

l1= Label(text="Username").grid(row=0)
l2= Label(text="Email").grid(row=1)
l3= Label(text="Phone").grid(row=2)

t1 = Entry(root)
t2 = Entry(root)
t3 = Entry(root)

t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
t3.grid(row=2,column=1)

btn  = Button(root,text="Submit").grid(row=3,column=1)


root.mainloop()