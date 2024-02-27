
class Calc:

    # def add(self,a,b,c):
    #     print(a+b+c)
    
    # def add(self,a,b):
    #     print(a+b)

    def add(self,*a):
        # sum= 0
        # for i in a:
        #     sum +=i
        # print(sum)
        print("calling")

c= Calc()
c.add(10,20)
c.add(10,2,9)
c.add(10,50,62,89,10)
c.add(10,"Hello")
c.add(50.23)
