# number = float(input("Enter the number with decimal places: "))
# new_number = number * 2
# print(new_number)
# print(round(new_number,2))
# print(round(new_number))

# import math
# number = int(input("Enter the number to find square root :"))
# sqrt = math.sqrt(number)
# print(f"The square root of {number} is :", round(sqrt,2))

# x = "Triangle"
# y = "Square"
# print()
# print("1) Triangle")
# print("2) Square")
# print()
# select = int(input("Please select what you want to draw : "))
# if select == 1:
#     height = int(input("Enter the height of triangle : "))
#     base = int(input("Enter the base of the triangle : "))
#     area = 1 / 2 * height * base
#     print(f"The area of {x} is", round(area))
# elif select == 2:
#     side = int(input("Enter the length of a side of a square : "))
#     area = side ** 2
#     print(f"The area of {y} is", round(area))
#
# else:
#     print("Invalid option. Try again !!!")

# # type
# print(type(5))
# print(type(5.5))
# print(type("Ram"))
# print(type(range(5)))
# print("=================================")

# list = []
# for x in range(1,10):
#     if x%2 == 0:
#         list.append(x)
#         print(x)
# count = len(list)
# print(f"There are {count} even numbers.")

count = 0
for x in range(1,10):
    if x%2 == 0:
        print(x)
        count += 1

print(f"There are {count} even numbers.")
