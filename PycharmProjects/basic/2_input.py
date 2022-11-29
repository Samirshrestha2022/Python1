# '''name = input("Enter name: ")
# age = input("Enter age:")
# phone = input("Enter phone no.:")
# address = input("Enter address:")
#
# print(f"My name is {name}")
# print(f"My age is {age}")
# print(f"My phone is {phone}")
# print(f"My address is {address}")'''
#
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# z = int(input("Enter z: "))
# total = x+y+z
# sub = x-y-z
# multi = x*y*z
# div = x/y
# div2 = x/z
# div3 = y/z
# div4 = z/x
# mod = x%y
# print(f"Total is {total}")
# print(f"Sub is {sub}")
# print(f"Multiplication is {multi}")
# print(f"Division is {div}")
# print(f"Division is {div2}")
# print(f"Division is {div3}")
# print(f"Division is {div4}")
# print(f"Modulus is {mod}")


a = int(input("Enter the English marks: "))
b = int(input("Enter the Maths marks: "))
c = int(input("Enter the Nepali marks: "))
d = int(input("Enter the Science marks: "))
e = int(input("Enter the Account marks: "))

total = a+b+c+d+e
Percentage = (total/500)*100
print(total)
print(Percentage)

print(f"The total is {total}")
print(f"The percentage is {Percentage:.2f}")
#
# if Percentage>=80:
#     print("A+")
# elif Percentage>=70:
#     print("A")
# elif Percentage>=60:
#     print("B")
# elif Percentage>=50:
#     print("C")
# elif Percentage>=40:
#     print("D")
# else:
#     print('fail')


if Percentage>=80:
    print("Your grade is A+")
elif Percentage>=70:
    print("Your grade is A")
elif Percentage>=60:
    print("Your grade is B")
elif Percentage>=50:
    print("Your grade is C")
elif Percentage>=40:
    print("Your grade is D")
else:
    print('Sorry!!! You failed. Work hard')