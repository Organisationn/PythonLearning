a=float(input("enter 1st side"))
b=float(input("enter 2nd side"))
c=float(input("enter 3rd side"))

# semi peri-meter
s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5

print(area)