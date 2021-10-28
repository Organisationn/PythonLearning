#1st approach
a=int(input("enter 1st variable"))
b=int(input("enter 2nd varibale"))

temp=a
a=b
b=temp

print("after swap: ",a)
print("after swap: ",b)

# or

print("after swap: "+str(a))
print("after swap: "+str(b))

#2nd approach
#now a and b holds 3 and 2 ..so after swap it should be 2 and 3
a,b=b,a
print("after swap: "+str(a))
print("after swap: "+str(b))

#2nd approach
#now a and b holds 2 and 3 ..so after swap it should be 3 and 2

a=a+b
b=a-b
a=a-b
print("after swap: ",a)
print("after swap: ",b)