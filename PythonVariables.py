#Definition:- A Python variable is a reserved memory location to store values.
# In other words, a variable in a python program gives data to the computer for processing.
#Types:-
# Python has five standard Data Types:
# i)Numbers
# ii)String
# iii)List
# iv)Tuple
# v)Dictionary
# How to Declare and use a Variable
# from bson import Int64
a=3.14J
print(a)
print(type(a))
a='Faith'
print(a)
a=10.001000000000000
print(a)
a=45.67
print(a)
a=100
print(a)
print(type(a))
a=True
print(a)
x=type(a)
print(x)
y="hello"
print(type(y))
pi = 3.14159
print(type(pi))
# x=Int64(7)
# exp-2
# Strings can be accessed as a whole string, or a substring of the complete variable using brackets ‘[]’.
# Here are a couple examples:
# var1 = 'Hello World!'
# var2 = 'RhinoPython'
# print(var1[0])
# print(var2[1:5])
#
# # List
# # Lists are a very useful variable type in Python.
# # A list can contain a series of values separated by comma
# # List variables are declared by using brackets [ ]
# A = [ ] # This is a blank list variable
# B = [1, 23, 45, 67] # this list creates an initial list of 4 numbers.
# C = [2, 4, 'john'] # lists can contain different variable types.
#
# mylist = ['Rhino', 'Grasshopper', 'Flamingo', 'Bongo']
# print(len(mylist))#length is 4 and index is from 0 to 3
# print(mylist[1]) #This will return the value at index 1, which is 'Grasshopper'
# print(mylist[0:2])#return 0th and 1 st index elements... include 0th but exclude 2nd element

# following example, the MyTable variable is a two-dimensional array :
# MyTable = [[], []]
# squares = [1, 4, 9, 16]
# sum = 0
# for num in squares:
#     sum += num
# print("sum ="+str(sum))
#   # print sum  ## 30
#
# list = ['larry', 'curly', 'moe']
# if 'curly' in list:
#     print('yay')

# Tuple
# Tuples are a group of values like a list and are manipulated in similar ways.
# But, tuples are fixed in size once they are assigned.
# In Python the fixed size is considered immutable as compared to a list that is dynamic and mutable.
# Tuples are defined by parenthesis ().
myGroup = ('Rhino', 'Grasshopper', 'Flamingo', 'Bongo')

# Here are some advantages of tuples over lists:
# Elements to a tuple. Tuples have no append or extend method.
# Elements cannot be removed from a tuple.
# You can find elements in a tuple, since this doesn’t change the tuple.
# You can also use the in operator to check if an element exists in the tuple.
# Tuples are faster than lists. If you’re defining a constant set of values and all you’re ever going to do with it is iterate through it, use a tuple instead of a list.
# It makes your code safer if you “write-protect” data that does not need to be changed.
# It seems tuples are very restrictive, so why are they useful? There are many datastructures in Rhino that require a fixed set of values. For instance a Rhino point is a list of 3 numbers [34.5, 45.7, 0]. If this is set as tuple, then you can be assured the original 3 number structure stays as a point (34.5, 45.7, 0). There are other datastructures such as lines, vectors, domains and other data in Rhino that also require a certain set of values that do not change. Tuples are great for this.

# Dictionary
# Dictionaries in Python are lists of Key:Value pairs
# dictionary is used to extract a value based on the key name
# Dictionaries can also be used to sort, iterate and compare data.

# Dictionaries are created by using braces ({}) with pairs separated by a comma (,)
# and the key values associated with a colon(:).
# In Dictionaries the Key must be unique.
# Here is a quick example on how dictionaries might be used:
room_num = {'john': 425, 'tom': 212}

room_num['john'] = 645  # set the value associated with the key 'john'  to 645
print (room_num['tom']) # print the value of the 'tom' key i.e.212
room_num['isaac'] = 345 # Add a new key 'isaac' with the associated value
print (room_num.keys()) # print out a list of keys in the dictionary
print ('isaac' in room_num) # test to see if 'issac' is in the dictionary.  This returns true.
del room_num['isaac']
print(room_num)
print(len(room_num))

# Sorting Dictionaries:-
# Dictionaries and be sorted by key name or by values
# To sort a dictionary by key using the following sorted() function:

print (sorted(room_num))
print (sorted(room_num.values()))

# NB:
# concatenation of String and number:-
# In Python we cant concatenate string and a number else it will throw TypeError

a="Guru"
b = 99
print(a+str(b))

# Local and Global variables:-
# There are two types of variables in Python, Global variable and Local variable.
#when a variable has to be used through out the program or module then mark the variable as Global
#when a variable has to be used in a specific function or method, you use a local variable
f=100

def expGlobalVar():
    f='Python Basics'
    print(f)

print(f)
expGlobalVar()

#Deleting a variable:-
f=11
print(f)#11
del f
print(f) #NameError: name 'f' is not defined



