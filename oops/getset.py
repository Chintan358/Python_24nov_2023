

class Demo:

    def __init__(self,a):
        self.a = a;

    def display(self):
        print(self.a)

    @property
    def ten_number(self):
        return self.a * 10;

    @ten_number.setter
    def ten_number(self,k):
        self.a=k;

    @property
    def sq_number(self):
        return self.a*self.a
    
    @sq_number.setter
    def sq_number(self,x):
        self.a=x

d = Demo(10)
# d.display()
d.ten_number = 45
print(d.ten_number)
d.sq_number=50
print(d.sq_number)


