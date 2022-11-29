
# data =[
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]
# for d in data:
#     for b in d:
#         print(b)
#     print("====================")
#

#
# increment = 0
# list = []
# input_times = int(input("Enter the number of inputs to be taken : "))
# while increment < input_times:
#     num_entered = int(input("Enter the number :"))
#     list.append(num_entered)
#     increment += 1
#
# print(list)
#
# rep_num = []
#
# for x in list:
#     if list.count(x) > 1 and x not in rep_num:
#         rep_num.append(x)
# print(rep_num)
# for y in rep_num:
#     print(f"{y} is repeated {list.count(y)} times")




# data = [5, 9, 6, 9, 8, 9, 3, 7, 9, 8, 4]
# sum = data[0] + data[-1]
# print("The sum is", sum)
# rep_num = []
# for x in data:
#     if x == sum and data.count(x) >= 1:
#         rep_num.append(x)
# print(rep_num)
#
# for y in rep_num:
#     print(f"{y} is repeated {data.count(y)} times")
#     break
# else:
#     print(f"{sum} is not in the list")



# while True:
#     city = input("Enter the name of the city / \"quit\" when finished :")
#     if city == 'quit':
#         print("Thank you for playing.")
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")


# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 1:
#         continue
#     print(current_number)



# names = ["ram", "sita", "hari", "gita", "ram", "hari"]
# input = ram
# output = ram, ram

# names = ["ram", "sita", "hari", "gita", "hari"]
# search_name = input("Enter the name to be searched: ")
# repeated_name = []
# for name in names:
#     if name == search_name:
#         repeated_name.append(name)
# print(repeated_name)
# for y in repeated_name:
#     print(y)

#
# # This loop runs forever!
# x = 1
# while x <= 5:
#     print(x)
#
# # solution
# x = 1
# while x <= 5:
#     x += 1
#     print(x)