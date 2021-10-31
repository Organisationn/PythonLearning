def fibonacci(count):
    n1=0
    n2=1
    if(count<=0):
        print('Please enter a positive integer, the given number is not valid')
        # exit(1)
    elif(count==1):
        print("The Fibonacci sequence of the numbers up to", count, ": ")
        print(n1)
    else:
        print(n1, n2)
        i=2
        while(i<count): # in range(2,count+1):
            n3 = n1 + n2
            print(" ",n3)
            n1=n2
            n2=n3
            i+=1

count=int(input('enter count'))
fibonacci(count)