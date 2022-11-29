#
# x = 10
# y = 20
# if x>y:
#     print("x is greater than y")
# elif x==y:
#     print("x is equal to y")
# else:
#     print("x is lesser than y")

# x = 10
# y = 200
# z = 30
#
# if x>y and x>z:
#     print("x is greater than y and z")
# elif y>x and y>z:
#     print("y is greater than x and z")
# elif x==y and y==z:
#     print('They are equal')
# else:
#     print("z is greater than x and y")

# x = 30
# y = 30
# z = 30
#
# if x>y and x>z:
#     print("x is greater than y and z")
# elif y>x and y>z:
#     print("y is greater than x and z")
# elif x==y and y==z:
#     print('They are equal')
# else:
#     print("z is greater than x and y")

#
# a = int(input("Enter the English marks: "))
# b = int(input("Enter the Maths marks: "))
# c = int(input("Enter the Nepali marks: "))
# d = int(input("Enter the Science marks: "))
# e = int(input("Enter the Account marks: "))
#
# total = a+b+c+d+e
# Percentage = (total/500)*100
# print(total)
# print(Percentage)
#
# print(f"The total is {total}")
# print(f"The percentage is {Percentage:.2f}")
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


# if Percentage>=80:
#     print("Your grade is A+")
# elif Percentage>=70:
#     print("Your grade is A")
# elif Percentage>=60:
#     print("Your grade is B")
# elif Percentage>=50:
#     print("Your grade is C")
# elif Percentage>=40:
#     print("Your grade is D")
# else:
#     print('Sorry!!! You failed. Work hard.')

# print('1.Python   2.Java')
# option = int(input("Enter your option: "))
# if option == 1:
#     print("You have selected python")
# elif option == 2:
#     print("You have selected Java")
# else:
#     print("Invalid option")

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if x > y and x > z:
    if y > z:
        x, y, z = x, y, z
    else:
        x, y, z = x, z, y

if y > x and y > z:
    if x > z:
        x, y, z = y, x, z
    else:
        x, y, z = y, z, x

if z > x and z > y:
    if x > y:
        x, y, z = z, x, y
    else:
        x, y , z = z, y, x

else:
    x, y, z = x, y, z

print(f"Sorted numbers : {x}, {y}, {z}")