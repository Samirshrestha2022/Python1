#
# data1= {
#     'name':'ram',
#     'age': 20,
#     'address': 'kathmandu'
# }
# print(type(data1))
# print(dir(data1))
# print(data1.keys())
# print(data1.values())
#
#
# data = {
#     'name':'ram',
#     'address': {'province':'kathmandu'},
#     'phone': 9872687837
# }
#
# print(data['address']['province'])
# print(data['phone'])
#
# #you can index in list but use keys in dictionary.
# data = [
#     {'name':'ram', 'age': 20},
#     {'name': 'sita', 'age': 22},
# ]
# print(data[1]['name'])
# print(data[0]['age'])

# student = {
#     "name" : ["John", "Sarah"],
#     "age" : [24, 22],
#     "address" : ["Wales", "Spain"]
# }
# print(student["name"])
# print(student["name"], student["address"])
# print(student.get("phone", "Not found"))
# student["phone"] = ["9841234232", "9862345645"]
# print(student)
# print(student["phone"])
#
# # replacing name
# student["name"] = ["Ram", "Sita"]
# print(student["name"])

# # updating dictionary
# student.update({"age" : [33, 31], "address" : ["Baluwatar", "Thimi"]})
# print(student)
#
# # deleting age of student
# del student["age"]
# print(student)
#
# student1 = student.pop("phone")
# print(student1)
# print(len(student1))
#
#
# for key in student:
#     print(key)
#
# for key, value in student.items():
#     print(key, value)


# call kamaladi, 5 and shashank
data = {
    'name' : "sophia",
    'age' : 12,
    'phone' : 9123234344,
    'address': "kathmandu",
    'town' : {
        'name' : "putalisadak",
        'tole' : {
            'name' : "kamaladi",
            'ward' : [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10
            ]
        }
    },
    "students" : [
        {
            'name' : "Shashank"
        }
    ]
}

print(data["town"]["tole"]["name"])
print(data["town"]["tole"]["ward"][4])
print(data["students"][0]['name'])