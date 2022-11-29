# mutable = can be changed, immutable = data cant be changed
# select the syntax then press command + / ( for comment)
# command + alt + L - to arrange lines


list1 = ['ram', 'sita', 'hari', 'shyam']
print(list1[0])
print(list1[1])
print(list1[0:3])
print(list1[:4])
print(list1[2:])
print(list1[-3:])


list1 = [ "ram", 23, "hari", "34shaq", "shyam444"]
print(list1)

# append
list1.append("Sita")
print(list1)

# insert
list1.insert(2,"Sophia")
print(list1)

# pop
list1.pop()
print(list1)

list1.pop(4)
print(list1)

# remove
list1.remove("hari")
print(list1)

# update/replace
list1[0] = "Shashank"
print(list1)
list1[1] = "Sabina"
print(list1)

# len - number of elements in a list
print(len(list1))

# count repeatation of elements in a list
print(list1.count("Shashank"))

# res join

# sort

# clear
list1.clear()
print(list1)

# delete
del list1

#print(list1)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
print("======================================================")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

''' 
list is a collection of data
properties of list = mutable, ordered, indexed, iterable, sequence, dynamic
'''
#
# data = [
#     ['ram', 'sita', 'hari'],
#     ['hari', 'shyam', 'gopal']
# ]
# print(data[1][1])
#
# data = [
#     ['ram', 'sita', 'hari'],
#        ['hari', 'shyam', [[['Laxmi']]], 'gopal']
# ]
# print(data[1][2])
# print(data[1][2][0][0][0])
#
#
# data = ['ram', 'sita', 'hari']
# print(data)
# data[1] = 'sophia'
# print(data)
# print(dir(data))