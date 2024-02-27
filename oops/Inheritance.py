
class Pen:

    price=10
    color="Red"
    company="cello"

    def show(self):
        print(f" price: {self.price} , color : {self.color} , company : {self.company}")

class NoteBook(Pen):

    def __init__(self) -> None:
        pass
    def display(self):
        print(f" price: {self.price} , color : {self.color} , company : {self.company}")

p= Pen()
p.show()
n = NoteBook()
n.display()