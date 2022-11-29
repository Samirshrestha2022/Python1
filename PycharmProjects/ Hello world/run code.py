# upper or lower case
phrase = "Giraffe Academy"
print (phrase.upper())
print (phrase.lower())
print (phrase.isupper())
print (phrase.upper().isupper())

print (len(phrase))

print (phrase[0])
print (phrase[4])
# index
print (phrase.index("G"))
print (phrase.index("a"))
print (phrase.index("Acad"))

# replace
print (phrase.replace("Academy", "School"))
print (phrase.replace ("Giraffe", "Camel")) 
## working with NUMBERS

print (2)
print (2.877877)
print (5+2)
print (3*4+5)
print (3*(4+5))
print (10%3)
print(13%5)
my_num = 33
print (str(my_num) + " is a lucky number")
print (my_num, " is a lucky number")
print ("lucky number is ", my_num )

# Absolute Number
my_num = -33
print (abs(my_num))

#power function
print (pow(2,6))
print (pow(3,4))
print (max(2,6))
print (min(2,6))

from math import *

print (round(3.59))
print(floor(3.7))
print (ceil(3.59))
print (sqrt(36))


print (list(range(0,100,9)))