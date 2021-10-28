# Properties of Dictionary Keys
# 1)no duplicate key is allowed
# 2)The values in the dictionary can be of any type, while the keys must be immutable
# 3)Dictionary keys are case sensitive- Same key name but with the different cases are treated as
# different keys in Python dictionaries.

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print(Dict['Tiffany'])

# We can copy the entire dictionary to another using copy() method as below
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
studentX=Boys.copy()
studentY=Girls.copy()
print(studentX)
print(studentY)

# Update a dictionary:-
# we can update a dictionary by adding a new key-value pair to the existing dictionary
# or by deleting an existing entry as below
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Dict.update({"Sarah":9})
print(Dict)#{'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25, 'Sarah': 9}

Dict1 = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
del Dict1['Charlie']
print(Dict1)
Dict2 = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("printable string:%s" % str (Dict2))
print(Dict2)

