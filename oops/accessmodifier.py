class Sample:

    #  id=20;
    __id= 10

    def __init__(self) -> None:
        pass

class Demo(Sample):

    def show(self):
        print(self.__id)

# s =Sample()
# s.__id=50
# print(s.__id)


# d = Demo()
# d.show()