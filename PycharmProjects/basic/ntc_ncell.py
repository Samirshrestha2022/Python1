print('======= CHECK YOUR BONUS ========')
print("Service provider: 1. ntc     2. ncell")
call_from = int(input("Calling from: "))
call_to = int(input("Calling to: "))
if call_from == 1 and call_to == 1:
    base_bonus = 2.5
elif call_from == 1 and call_to == 2:
    base_bonus = 5
elif call_from == 2 and call_to == 1:
    base_bonus = 7.5
elif call_from == 2 and call_to == 2:
    base_bonus = 10
else:
    print("Not a valid code!!!")
    exit()
call_duration = int(input("Call duration : "))
count = call_duration // 10 + 1
print("Your base bonus = ", base_bonus,"per 10 mins")
total_bonus = count * base_bonus
print("Your total bonus is",  total_bonus)
