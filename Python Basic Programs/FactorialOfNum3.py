def fact(n):
    factorial=1
    if(n<0):
        print('factorial of negative number doesn"t exist')
    elif(n==0 or n==1):
        print('factorial is 1')
    else:
        for i in range(1,n+1):
            factorial=factorial*i
        print('factorial is: ',factorial)
n=int(input('enter number'))
fact(n)
