print( "    /!")
print( "   / !")
print( "  /  ! ")
print( " /   !")
print( "/____!")

print('hello world')

print("hello \"world\"")

phrase = "SAm academy"
print(phrase)

message = "Hello World"
print(message)


character_name = "SAm"
character_age = "35"
print("There was a man named "+ character_name +",")
print("he was "+ character_age + " years old.")
print("he really liked the name "+character_name +",")
print("but didn't like being "+ character_age +".")




character_name = "sam   "
character_age = "35"

print("There was a man named "+ character_name +",")
print("he was "+ character_age + " years old.")
character_name = "Hari"
print("he really liked the name "+character_name +",")
print("but didn't like being "+ character_age +".")



character_name = "John"
character_age = 44.55
is_male = False


print ("Samir \nShrestha")
print ("\"Samir\" is cool")

character_name = "John"

phrase = "is cool"
print (""+ character_name +" "+phrase+"")
print (phrase.upper())
print (phrase.upper().isupper())


print (phrase.upper().islower())

print (len(phrase))


print (character_name[0])
print (character_name[1])
print (character_name[2])
print (character_name[3])

print (phrase.index("l"))

print (phrase.replace("cool","smart"))

str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

a = [5,10,15,20,25,30,35,40]
print(a[2])
print("a[2] = ", a[2])
# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

a = [1, 2, 3]
a[2] = 4
print(a)

t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])




s = "This is a string"
print(s)
s = '''A multiline
string'''
print(s)

s = 'Hello world!'

# s[4] = 'o'
print("s[5] = ", s[5])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])


# Python String Operations
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)


# Iterating through a string
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')


# Iterating through a string
count = 0
for letter in 'Hello World':
    if(letter == 'o'):
        count += 1
print(count,'letters found')


str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))




# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")
