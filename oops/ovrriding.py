
class A:

    def sample(self):
        print("Class A sample calling")
    
class B(A):

    def __init__(self) -> None:
        pass

    def sample(self):
        print("class  B sample")

b = B()
b.sample()