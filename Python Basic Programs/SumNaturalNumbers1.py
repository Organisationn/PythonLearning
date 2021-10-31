def sumOfNaturalNumbers(n):
    if(n<0):
        print('please enter a positive number')
    else:
        sum=0
        while(n>0):
            sum+=n
            n-=1
        print("sum of ",n,"th natural numbers are: ", sum)

num=int(input('enter the natural number'))
sumOfNaturalNumbers(num)