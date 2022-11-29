#
# data = ['ram', 'sita', 'gita']
# total = len(data)
# print(total)
#
# data.append('hari')
# print(data)
#
# print(len(data))
#
# data =['ram']
# data[0] = 'hari'
#
# print(data)
#
# # data= []
# # data[0] = 'hari'
# # cannot work in empty list. so use append.
# data= []
# data.append('hari')
# data.append('ram')
# print(data)
#
# data = ['sophia', 'ram', 'sita']
# data1 = ['hari', 'gita']
# data.append(data1)
# print(data)
#
# data = ['sophia', 'ram', 'sita']
# data1 = ['hari', 'gita']
# data.extend(data1)
# print(data)

data = ['sophia', 'ram', 'sita']
data1 = ['hari', 'gita']
data.insert(1,data1)
print(data)
#
# data.pop()
# print(data)
#
# data.pop(1)
# print(data)
#
# # clears all the elements in the list.
# data.clear()
# print(data)
#
# # remove needs the value rather than index to work.
# data = ['sophia', 'ram', 'sita']
# data.remove('ram')
# print(data)
#
# # # copy
# # a = 10
# # b = 20
# # c = a
# # print(id(a))
# # print(id(b))
# # print(id(c))
#
# data = ['sophia', 'ram', 'sita']
# new_data = data.copy()
# print(new_data)
#
# print(id(data))
# print(id(new_data))
#
# # sort should have similiar data type.
#
# data = ['sophia', 'ram', 'sita', 'hari']
# data.sort()
# print(data)
#
# data = ['sophia', 'ram', 'sita', 'hari']
# data.reverse()
# print(data)
#
# data = [
#     ['ram','sita','gita'],
#     ['hari','shyam','gopal'],
# ]
# data1 = ['laxmi','rita']
# data[1][1] = data1
# print(data)
#
#
# data = [
#     ['ram','sita','gita'],
#     ['hari','shyam','gopal'],
# ]
# data1 = ['laxmi','rita']
# data[1].insert(1,data1)
# print(data)