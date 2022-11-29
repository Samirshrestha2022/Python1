## Fuction type: 1. Inbuilt function      2. User defined function
## Inbuilt function: e.g. print,len, type, dir
## User defined function: eg


# def welcome():
#     print("Welcome to Python")
# welcome()


# def welcome(name):
#     print("Welcome", name.title(),"!!!")
# welcome("ram")


# def welcome(name, age):
#     print("Welcome",name.title(),"!!!"" Your age is", age,".")
# name = input("Enter the name: ")
# age = input("Enter the age: ")
# welcome(name, age)


# def welcome(name = 'Samir'):
#     print("Welcome", name,".")
# welcome()
# welcome("Sabina")


# def welcome(name = 'Samir', age = 33):
#     print(f"Welcome {name}. You are {age} years old.")
# welcome()
# welcome("Sabina", 31)


# def welcome(name, phone, age = 0, address = ''):
#     print(f"Welcome {name.title()}!!! \n Age: {age} yrs \n Contact no: {phone} \n Address: {address.title()}")
#
# welcome('ram', 9841276552, 23, 'anamnagar')


# def welcome(name = 'Samir', phone = 9828061522, age = 33, address = 'Anamnagar'):
#     print(f"Welcome {name.title()}!!! \n Age: {age} yrs \n Contact no: {phone} \n Address: {address.title()}")
# welcome()
# welcome('ram', 9841276552, 23, 'dillibazaar')


# def greet():
#     print("Hello !!!")
#     print("Good morning.")
# greet()
# print("========================================")


# def add(x, y):
#     c = x + y
#     return c
# print(add(5,4))
# print("========================================")
#
#
# def add_sub(x, y):
#     c = x + y
#     d = x - y
#     return c, d
# result1, result2 = add_sub(5,4)
# print(result1, result2)
# print("========================================")

#
# def add_sub(x, y):
#     c = x + y
#     d = x - y
#     return [c, d]
# result= add_sub(5,4)
# print(result)
# print(result[0])
# print(result[1])
# # print(result1, result2)
# print("========================================")


# def user():
#     print("Hello form the user function.")
#
# def result():
#     user()
#
# result()


# def take_value():
#     p = int(input("Enter the principal: "))
#     t = int(input("Enter the time: "))
#     r = int(input("Enter the rate: "))
#     return [p, t, r]
#
#
# def calculator():
#     sp = take_value()
#     return sp[0] * sp[1] * sp[2] / 100
#
# def display():
#     print(f"Simple interest is: {calculator()}")
#
# display()
# print("========================================")


# def take_value():
#     p = int(input("Enter the principal: "))
#     t = int(input("Enter the time: "))
#     r = int(input("Enter the rate: "))
#     return p, t, r
#
# def calculator():
#     i = take_value()
#     return i[0] * i[1] * i[2] / 100
#
# def display():
#     print(f"Simple interest is: {calculator()}")
#
# display()
# print("========================================")


# nested function, lambda function, recursion function
# module
#(*args)(*kwargs)
# except finally
# file handling
# oop (object oriented programming)

#
# def square(a):
#     return a * a
#
# result = square(5)
# print(result)
#
# data = []
# x = input("Enter the name: ")
# for x in data:
#     if x != data:
#         data.append(x)
#         print(data)
#         continue
#     else:
#         print("The name is already in the list")
#         break
# print(data)


data = []
x = int(input("Enter the times: "))
y = 0
while y <=x:
    name = input("Enter the name: ")
    if name not in data:
        data.append(name)
    else:
        print("The name is already in the list")
    y += 1

print(data)