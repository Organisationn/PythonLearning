# Tuple Syntax
Tup = ('Jan','feb','march')

# To write an empty tuple, you need to write as two parentheses containing nothing-
tup1 = ()
tup1 = ('Mano')
print(tup1)

# For writing tuple for a single value, you need to include a comma, even though there is a single value.
# Also at the end you need to write semicolon as shown below.

Tup1 = (50,);
# Tuple indices begin at 0, and they can be concatenated, sliced and so on.
#Exp
tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print(tup1[0])
print(tup2[1:4])

# Tuple 1 includes list of information of Robert
# Tuple 2 includes list of numbers in it
# We call the value for [0] in tuple and for tuple 2 we call the value between 1 and 4
# Run the code- It gives name Robert for first tuple while for second tuple it gives number (2,3 and 4)

# In packing, we place value into a new tuple while in unpacking we extract those values back into variables.
x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)#Guru99
print(emp)#20
print(profile)#Education

#Tuple Comparison:-
#It starts with comparing the first element from each of the tuples
a=(5,6)
b=(1,4)
if (a>b):print("a is bigger")
else: print("b is bigger")# a bigger

a=(5,6)
b=(5,4)
if (a>b):print("a is bigger")
else: print ("b is bigger") # a bigger

a=(5,6)
b=(6,4)
if (a>b):print("a is bigger")
else: print("b is bigger") # b bigger

# NB:-
# Comparison starts with 1st element of each tuple.If 1st one is greater/less
# it will execute if or else accordingly but if 1st elements are equal it will check 2nd elements and decide accordingly

#Tuples and dictionary
a = {'x':100, 'y':200}
b = a.items()
print(b)

#Slicing of Tuple
x = ("a", "b","c", "d", "e")
print(x[2:4])
del x
print(x)

# Built-in functions with Tuple
# To perform different task, tuple allows you to use many built-in functions like all(), any(), enumerate(), max(), min(), sorted(), len(), tuple(), etc.

#Advs of Tuple over List:-
# i)Iterating through tuple is faster than with list, since tuples are immutable.
# ii)Tuples that consist of immutable elements can be used as key for dictionary, which is not possible with list
# iii)If you have data that is immutable, implementing it as tuple will guarantee that it remains write-protected

# NB:-
# i)Tuples are immutable and cannot be deleted. You cannot delete or remove items from a tuple.
# But deleting tuple entirely is possible by using the keyword “del”
# To fetch specific sets of sub-elements from tuple or list, we use this unique function called slicing

