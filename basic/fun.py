class Demo:
    print("Hello")

    def __str__(self) -> str:
        return "Hello"

d = Demo()
print(d)