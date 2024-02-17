
def test():
    try:
        num = int(input("enter number : "))
        print(num)
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
        print("always execute")

a = test()
print(a)