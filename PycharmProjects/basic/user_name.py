#
# username = input("Enter the username :")
# password = input("Enter the password: ")
# if username == "admin" and password == "admin123" or username == "ram" and password == "ram002":
#     print(f"Welcome {username}")
# else:
#     print("Incorrect username or password !!!")

# x = 16
# y = 15
# z = 11
#
# if x > y :
#     if x > z:
#         print('X is greater')
#     else:
#         print('Z is greater')
# else:
#     if y > z:
#         print('Y is greater')
#     else:
#         print('Z is greater')



username = input("Enter the username :")
password = input("Enter the password: ")
if username == "admin":
    if password == "admin123":
        print(f"Welcome {username}")
    else:
        print('Incorrect password')
elif password == "admin123":
    print("Incorrect username !!!")
else:
    print("Invalid both username and password !!!")