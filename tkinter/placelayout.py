from tkinter import *
import mysql.connector

root = Tk()
root.title("My app")
root.geometry("500x500")

def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="python"
    )

def insertdata(uname,email,phone):
    con = connection()
    cursor =con.cursor()
    qry = "insert into reg values(%s,%s,%s,%s)"
    val = (0,uname,email,phone)
    cursor.execute(qry,val)
    con.commit()
   
l1= Label(text="Username").place(x=100,y=100)
l2= Label(text="Email").place(x=100,y=130)
l3= Label(text="Phone").place(x=100,y=160)

t1 = Entry(root)
t2 = Entry(root)
t3 = Entry(root)

t1.place(x=170,y=100)
t2.place(x=170,y=130)
t3.place(x=170,y=160)

btn  = Button(root,text="Submit", fg="red",bg="yellow",command=lambda:insertdata(t1.get(),t2.get(),t3.get())).place(x=170,y=190)


root.mainloop()