num1=input("enter first number")
num2=input("enter second number")

#Add
sum=int(num1)+int(num2)
print("sum of {0} and {1} is {2}".format(num1,num2,sum))

#Sub
min=int(num1)-int(num2)
print("subtraction of {0} and {1} is {2}".format(num1,num2,min))

#multiply
mul=int(num1)*int(num2)
print("multiplication of {} and {} is {}".format(num1,num2,mul))

#divide
div=int(num1)/int(num2)
print("division of {a} and {c} is {b}".format(c=num1,a=num2,b=div))

#modulus
mod=int(num1)%int(num2)
print("mod of {} and {} is {}".format(num1,num2,mod))

#Exponential:- In Python, ** is the exponentiation operator.
# It is used to raise the first operand to power of second.
exp=int(num1)**int(num2)
print("exponent of num1 and num2 is "+str(exp))

# Floor division : In Python, // is used to conduct the floor division.
# It is used to find the floor 1of the quotient when first operand is divided by the second.
res=int(num1)//int(num2)
print(res)
