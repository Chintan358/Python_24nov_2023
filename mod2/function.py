
# a=10;
# b = 20;
# c= a+b
# print(c)

# x=100
# y =600
# z=x+y
# print(z)

# def getMsg():
#     print("Hello")

# def square(x):
#     return x*x

# def add(a=0,b=0):
#     print(a+b)
  
# def info(fname,lname):
#     print(fname,lname)

# add()

# getMsg()
# n = square(8)
# print(n)
# add(10,20)
# print(square(50))

# info(lname="tech",fname="tops")

# add = lambda a,b:print(a+b)
# sq= lambda a: print(a*a)

# add(10,20)
# sq(10)
    

def test(fx):
    def vfx(*a,**b):
        print("method start")
        fx(*a,**b)
        print("program end")
    return vfx

@test
def hello():
    print("Hello")

@test
def add(a,b):
    print(a+b)


hello()
add(10,20)