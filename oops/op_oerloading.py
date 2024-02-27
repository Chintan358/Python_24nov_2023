
# print(10+20)
# print("hello"+"python")

# 2 + 3i
# 5 + 7i
# 7 + 10i

class Calc:

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __str__(self):
        x =str(self.a)
        y =str(self.b)
        return x +","+ y

    def __mul__(self,u):
        return self.a*u.a,self.b*u.b

c1 = Calc(2,3)
c2 = Calc(5,7)

print(c1)
print(c2)
k = c1 * c2
print(k)


