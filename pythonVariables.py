#Print command
x = 5
y = "John"
print(x)
print(y)
# words in programming are called strings
# 5 = integer => int
#"hello"= word => string
# booleans = 0,1 example true/false

# variables are case sensitive
a = 4
A = "Bob"
print (a,A)
# A WILL NOT OVERWRITE a
# = in programming means "Assigned to" Exple 5 is assigned to variable x

# LEGAL VARIABLE NAMES
# A variable name must start or underscore character
# IT CANNOT START WITH A NUMBER
# IS CASE SENSITIVE AND CANNOT CONTAIN ALPHA-NUMERIC CHARACTERS (a-z, 0-9)
# CAN ALSO MEAN "NOT EQUAL TO"(AGE IS # age)
# python allow you to assign many values to multiple variable in 1 line
X,Y,Z= "Orange", "Banana", "Cherry"
print(X)
print(Y)
print(Z)

# python allows you to assign 1 value to multiple variables
X = Y = Z = "Orange"
print(X)
print(Y)
print(Z)

#RANDOM NUMBER
import random
print(random.randrange(1,10))

#concatenation
#concatenation is to combine two strings, you can use te + operator
a="hello"
B="Patricia"
c=a+B
print(c)
#add space between variables
c = a + " " + B
#string format
age = "36"
text = "My name is Patricia, I am "+ age
print (text)
