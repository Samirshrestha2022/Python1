# print("============Computer Bazaar=============")
# print("We sell: 1. Dell : Rs 20000  2. Toshiba : Rs 30000   3. Mac : Rs 50000")
# option = int(input("Enter your choice: "))
#
# dell_price = 0
# toshiba_price = 0
# mac_price = 0
# delivery_price = 0
# plastic_price = 0
# bag_price = 0
# giftbox_price = 0
# location_price = 0
# tax_amount = 0
#
# if option == 1:
#     quantity = int(input("Enter the quantity : "))
#     dell_price = quantity * 20000
#
# elif option == 2:
#     quantity = int(input("Enter the quantity : "))
#     toshiba_price = quantity * 30000
#
# elif option == 3:
#     quantity = int(input("Enter the quantity : "))
#     mac_price = quantity * 50000
#
# else:
#     print("Invalid option")
#
# print("=======Delivery option========")
# print('1. Home: Rs 500   2. Pickup: Free')
# delivery_option = input('Choose your delivery option : ')
# if delivery_option == 1:
#     delivery_price = 1000
#
# print(" ======Packing Option=======")
# print("1. Plastic : Rs 500  2. Bag : Rs 1000  3. Gift Box : Rs 5000  4. None")
# packing_option = int(input('Enter packing option : '))
# if packing_option == 1:
#     plastic_price = 500
# elif packing_option == 2:
#     bag_price = 1000
# elif packing_option == 3:
#     giftbox_price = 5000
#
# total = dell_price + toshiba_price + mac_price
#
# print("=======Tax % =======")
# print("1. Kathmandu :13 % tax   2. BKT - free  3. LTP - free")
# location_option = int(input("Enter the location : "))
# if location_option == 1:
#     tax_amount = Total * 0.13
#
# grand_total = total + delivery_price + plastic_price + bag_price + giftbox_price + tax_amount
#
# print("===== BILL =====")
# print("Total: ", total)
# print("Tax amount: ", tax_amount)
# print("Grand total : ", grand_total)
#
# print("=========COMPUTER SHOP===========")
# print("We sell: 1. Dell : Rs 20000  2. Toshiba : Rs 30000   3. Mac : Rs 50000")
# selected_computer = int(input("Please select the computer : "))
# if selected_computer >= 4:
#     print("Enter valid number !!!")
#     exit()
# quantity = int(input("Quantity : "))
#
# if selected_computer == 1:
#     computer_price = 20000
#
# if selected_computer == 2:
#     computer_price = 30000
#
# if selected_computer == 3:
#     computer_price = 50000
#
#
# print("===========PACKING OPTION=============")
# print("1. Plastic: Rs 500      2. Bag: Rs 1000        3. Gift box: Rs 5000")
#
# selected_packing = "Enter the packing option : \n"
# packing_option = int(input(selected_packing))
#
# while packing_option >=4:
#     print("The option is invalid. Please try again !!!")
#     packing_option = int(input(selected_packing))
#
# if packing_option == 1:
#     packing_charge = 500
#
# if packing_option == 2:
#     packing_charge = 1000
#
# if packing_option == 3:
#     packing_charge = 5000
#
# print("==========DELIVERY OPTION============")
# print("1. home delivery = 500       2. Pickup = Free")
# delivery_option = int(input("Enter delivery option: "))
#
# if delivery_option >=3:
#     print("Enter the valid number !!!")
#     exit()
#
# elif delivery_option == 1:
#     delivery_charge = 500
# else:
#     delivery_charge = 0
#
#
# total = computer_price * quantity
# print('Your total is Rs ', total)
#
# print("=======Location and Tax Rates=======")
# print("1. Kathmandu: 10%  2. Bhaktapur : Free   3. Lalitpur : Free")
#
# tax_location = int(input("Enter your location: "))
# if tax_location == 1:
#     tax = 0.1
# else:
#     tax = 0
# tax_amount = tax * total
# print(f"Your total is Rs {total}")
# print("Your tax amount is Rs", tax_amount)
# print(f"Your packing charge is Rs {packing_charge}")
# print(f"Your delivery charge is Rs {delivery_charge}")
# grand_total = total + tax_amount + packing_charge + delivery_charge
# print("Your grand total is Rs ", grand_total)
#



print("=========COMPUTER SHOP===========")
print("We sell: 1. Dell : Rs 20000  2. Toshiba : Rs 30000   3. Mac : Rs 50000")

def selected_computer
    selected_computer = int(input("Please select the computer : "))
    if selected_computer >= 4:
    print("Enter valid number !!!")
    exit()
    quantity = int(input("Quantity : "))

    if selected_computer == 1:
    computer_price = 20000

    if selected_computer == 2:
    computer_price = 30000

    if selected_computer == 3:
    computer_price = 50000


print("===========PACKING OPTION=============")
print("1. Plastic: Rs 500      2. Bag: Rs 1000        3. Gift box: Rs 5000")

selected_packing = "Enter the packing option : \n"
packing_option = int(input(selected_packing))

while packing_option >=4:
    print("The option is invalid. Please try again !!!")
    packing_option = int(input(selected_packing))

if packing_option == 1:
    packing_charge = 500

if packing_option == 2:
    packing_charge = 1000

if packing_option == 3:
    packing_charge = 5000

print("==========DELIVERY OPTION============")
print("1. home delivery = 500       2. Pickup = Free")
delivery_option = int(input("Enter delivery option: "))

if delivery_option >=3:
    print("Enter the valid number !!!")
    exit()

elif delivery_option == 1:
    delivery_charge = 500
else:
    delivery_charge = 0


total = computer_price * quantity
print('Your total is Rs ', total)

print("=======Location and Tax Rates=======")
print("1. Kathmandu: 10%  2. Bhaktapur : Free   3. Lalitpur : Free")

tax_location = int(input("Enter your location: "))
if tax_location == 1:
    tax = 0.1
else:
    tax = 0
tax_amount = tax * total
print(f"Your total is Rs {total}")
print("Your tax amount is Rs", tax_amount)
print(f"Your packing charge is Rs {packing_charge}")
print(f"Your delivery charge is Rs {delivery_charge}")
grand_total = total + tax_amount + packing_charge + delivery_charge
print("Your grand total is Rs ", grand_total)

