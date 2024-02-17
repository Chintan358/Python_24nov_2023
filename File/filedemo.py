

f = open("myfile.txt",'w')
f.write("Hello python")
f.truncate(7)

# f = open("myfile.txt",'r')
# text = f.read()
# print(text)

# f = open("myfile.txt",'a')
# f.write("Hello0 hello python")
# f.close()

# with open("myfile.txt") as f:
#     text  =f.read()
#     print(text)

# with open("myfile.txt") as f:
#     while True:
#         text = f.readline()
#         if not text:
#          break
#         print(text)

# with open("myfile.txt") as f:
#     # f.seek(10)
#     print(f.tell())
#     text  =f.read()
#     print(text)
    
import os

# os.makedirs("newfolder")
os.rmdir("newfolder")


