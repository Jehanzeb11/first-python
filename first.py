# import os
# import pyttsx3
# import math
# engine = pyttsx3.init()
# engine.say("Hello World!")
# engine.runAndWait()

# print(math.pi)

# dir_path = 'E:\my-learn\python'

# os.mkdir("E:\my-learn\python\hew")

# contents = os.listdir(dir_path)

# print(contents)

# abc = "hello!"

# v = len(abc)
# print(v)

# for i in range(v):
#     print(abc[i])

# for i in abc:
#     print(i)

# first = "Jehanzeb"
# last = "Siddiqui"

# name = f"{first} {last} {2+2}"

# print(name)

# reverse
# print(abc[::-1])


# print(abc.upper())
# print(abc.lower())
# print(abc.capitalize())
# print(abc.title())
# print(abc.strip()) remove space from start and end of string
# print(abc.split())
# print(abc.split('l'))
# print(abc.replace('l', 'L'))
# print(abc.find('l'))
# print(abc.startswith('h'))
# print(abc.endswith('o'))
# print(abc.isalpha())
# print(abc.isalnum())
# print(abc.isnumeric())
# print(abc.islower())
# print(abc.isupper())
# print(abc.isspace())
# print(abc.count('l'))

# a = input("Enter your age: ")
# print(type(a))
# print(int(a))

# if abc == 'hello!':
#     print("True")

# elif abc == 'hello':
#     print("True Maybe")

# else:
#     print("False")

# print("HEHE")


# print("Hello") if abc == "hello!" else print("False")

# a = 6
# b = False
# c = True

# print(a, b, c)
# print(a and b and c)

# if a and b and c:
#     print("True")
# else:
#     print("False")

# if a or b or c:
#     print("True")
# else:
#     print("False")

# if not a:
#     print("True")
# else:
#     print("False")

# if not a and (not b or not c):
#     print("True")
# else:
#     print("False")

# if a >= 18 < 65:
#     print("True")
# else:
#     print("False")

# for num in range(1, 40, 2):
#     print(num)


# for num in range(5):
#     for num2 in range(3):
#         print(f"({num} {num2})")

# for x in "Jehanzeb":
#     print(x)

# for x in [1,2,3]:
#     print(x)

# number = 100
# while number > 0:
#     number //= 2
#     print(number)

# command = ""

# while command.lower() != "quit":
#     command = input(">")
#     print(command)


# nums = 0

# for i in range(1,10):
#     if i % 2 == 0:
#         print(f"We have {i} even numbers")
#         nums += 1
# print(f"We have total {nums} even numbers")


# def myFun (name):
#     return f"Hello {name}"


# nn =  myFun("Jehanzeb")
# print(nn)

# num = 0

# def inc(incBy = 5):

#     return num + incBy

# nn = inc(10)

# print(nn)


# def multiply(*numbers):
#     total = 1
#     for i in numbers:
#         print(i)
#         total = total * i

#     return total


# print(multiply(2, 3,4))
