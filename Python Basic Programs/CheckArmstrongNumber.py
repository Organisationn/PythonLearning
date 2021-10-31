def armstrongNumber(num):
    temp=num
    sum=0
    r=0
    order = len(str(num))
    while(num>0):
        r=num%10
        sum = sum + r ** order
        num=num//10

    if(sum==temp):
        print(temp,' is an armstrong number')
    else:
        print(temp,' is not an armstrong number')

n=int(input('enter a number'))
armstrongNumber(n)