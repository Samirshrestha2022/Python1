

print("Bus stops: 1.Gongabu  2.Maharajgunj  3. Chabahil  4. Satdobato  5. Kalanki")
start_point = int(input("Start point : "))
end_point = int(input("End point : "))

student_discount = 0
bus_fare = 0
base_fare = 15
discount = 0.10


if start_point == 1 and end_point == 2:
    stops = 1
elif start_point == 1 and end_point == 3:
    stops = 2
elif start_point == 1 and end_point == 4:
    stops = 3
elif start_point == 1 and end_point == 5:
    stops = 4
elif start_point == 1 and end_point == 1:
    stops = 5

elif start_point == 2 and end_point == 3:
    stops = 1
elif start_point == 2 and end_point == 4:
    stops = 2
elif start_point == 2 and end_point == 5:
    stops = 3
elif start_point == 2 and end_point == 1:
    stops = 4
elif start_point == 2 and end_point == 2:
    stops = 5

elif start_point == 3 and end_point == 4:
    stops = 1
elif start_point == 3 and end_point == 5:
    stops = 2
elif start_point == 3 and end_point == 1:
    stops = 3
elif start_point == 3 and end_point == 2:
    stops = 4
elif start_point == 3 and end_point == 3:
    stops = 5

elif start_point == 4 and end_point == 5:
    stops = 1
elif start_point == 4 and end_point == 1:
    stops = 2
elif start_point == 4 and end_point == 2:
    stops = 3
elif start_point == 4 and end_point == 3:
    stops = 4
elif start_point == 4 and end_point == 4:
    stops = 5

elif start_point == 5 and end_point == 1:
    stops = 1
elif start_point == 5 and end_point == 2:
    stops = 2
elif start_point == 5 and end_point == 3:
    stops = 3
elif start_point == 5 and end_point == 4:
    stops = 4
elif start_point == 5 and end_point == 5:
    stops = 5

option = input('Are you a student ? y/n :')
if option == "y":
    bus_fare = stops * base_fare
    student_discount = discount * bus_fare
    student_fare = bus_fare - student_discount
    print("====== BUS FARE DETAILS ===================")
    print('Number of stops = ', stops)
    print('Student discount = Rs',student_discount)
    print('Your bus fare = Rs', student_fare)

else:
    bus_fare = stops * base_fare
    print('Your bus fare is Rs ', bus_fare)