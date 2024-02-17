
print("program started")

try:
    # num = 10
    # result = num/0
    # print(result)
   l = [10,20,30,40,50]
   print(l[13])

except ValueError as e:
    print(e)
except IndexError as e:
    print(e)

    print("always execute")

print("program ended")