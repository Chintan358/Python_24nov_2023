
class Student:


    def __init__(self,id,name,email):
        self.id= id
        self.name=name
        self.email=email

    def display(self):
        print(f"id: {self.id} , name: {self.name} , Email: {self.email}")


s = Student(10,"test","test@gmail.com")
s.display()

s1= Student(20,"tech","tech@gmail.com")
s1.display()



