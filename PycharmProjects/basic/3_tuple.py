data = ('ram', 'sita', 'hari')
print(type(data))

data = {'ram', 'sita', 'hari'}
print(type(data))

data = {'ram', 'sita', 'hari', 'ram', 'sita'}
print(data)

data = {
    'name': 'ram',
    'age': 20,
    'address': [{'location': 'kathmandu'},
                {'location 2' : 'thamel'}]
}
print(data['address'][0]['location'])
print(data['address'][1]['location 2'])
data = ['ram']
print(data[0][0])

data = ['ram', 'sita', 'hari', 'ram', 'ram', 'sita']
print(data[0])

print(dir(data))
print(data.count('ram'))

print(len(data))

list = [1, 1, 2, 5, 6, 3, 5, 6, 7, 8, 8, 9, 7, 6, 5, 5, 5, 7, 7, 8, 8, 6, 4, 5, 5, 6, 7, 5, 3, 3, 3, 5, 2]
x = list.count(1)
print(x)
print(list.count(5))
print(list.count(6))

