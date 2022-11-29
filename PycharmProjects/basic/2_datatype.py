# data types
# numbers: int, float, complex
# strings: str
# boolean: True, False
# lists: list
# tuples: tuple
# dictionaries: dict
# sets: set


# int: integer ( no decimals)
x = 10
print(type(x))
print(dir(x))
# dir tells the content of directory

# float has decimals
age =4.5
print(type(age))
print(dir(age))

age = 10j
print(type(age))
print(dir(age))

'''a= int(input("Enter a: "))
b= int(input("Enter b: "))
print (a+b)
print(type(a))'''

name = "ram"
print(type(name))

# mother's
# print("mother's")

# 'mother's', "mother's", mother"s

print("'mother's'")
print('\'mother\'s\'')
print('"mother\'s"')
print('mother"s')

name = 'ram'
print(name[0])

name = 'python course'
print(name[:])
print(name[3:])
print(name[3:7])
print(name[:-3])

# nepali.mp3, english.mp3
song = "nepali.mp3"
print(song)
print(song[:-4])

# boolean
print(5>7)
print(5<7)

a,b = 10, 20
print(a)
print(b)

a,*b = 10, 20, 30, 40, 50
print(a)
print(b)

*a,b = 10, 20, 30, 40, 50
print(a)
print(b)

print("hello", "ram", 20)

data = ['ram', 20, 'sita']
print(data)
print(dir(data))