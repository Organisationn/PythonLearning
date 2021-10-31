def armstrongInInterval(lower,upper):
    displayArmstrong=[]
    for i in range(lower,upper+1):
        sum = 0
        r = 0
        temp = i
        order = len(str(i))
        while(i>0):
            r=i%10
            sum=sum+r**order
            i=i//10
        if (sum == temp):
                displayArmstrong.append(temp)
        else:
                pass

    print('Armstrong numbers are : ' , *displayArmstrong)

lower=int(input('Enter the lower limit'))
upper=int(input('Enter the upper limit'))
armstrongInInterval(lower,upper)