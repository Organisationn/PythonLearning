def checkPrimeInRange(m,n):#m=10 n =15
    DisplayPrime=[]
    for i in range(m,n+1):#10 ru 16
        if(i!=1 and i>0):
            count=0
            for k in range(2,i):
                if(i%k==0):
                    count+=1
                    break
            if(count>0):
                pass
            else:
                # print(i,'prime')
                DisplayPrime.append(i)
        else:
            print('it"s a special number')
    print("Prime numbers within range are: ",DisplayPrime)
    print(' '.join(map(str, DisplayPrime)))
    # printing the list using * operator separated by space
    print(*DisplayPrime)
    # printing the list using * and sep operator
    print(*DisplayPrime,sep=',')
    for x in range(0,len(DisplayPrime)):
        print(DisplayPrime[x])
m=int(input('enter lower range'))
n=int(input('enter upper range'))
checkPrimeInRange(m,n)