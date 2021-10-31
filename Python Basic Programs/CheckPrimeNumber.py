def checkPrime(n):
    if n!=1 and n>0:
        count = 0
        if (n > 1):
            for i in range(2, n):
                if (n % i == 0):
                    count = count + 1
            if(count>0):
                print("not prime")
            else:
                print("prime")
    else:
        print('It"s a special number..')

        # if (n > 1):
        #     count = 0
        #     for i in range(2, n + 1):
        #         if (n % i == 0):
        #             count = count + 1
        #     if(count>1):
        #         print("not prime")
        #     else:
        #         print("prime")
        # else:
        #     if n==1:
        #         print('1 is a special number')
        #     else:
        #         print('To banda.. mu kahibini')

num=int(input('enter number'))
checkPrime(num)
