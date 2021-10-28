def numberCheck(a):
    if a>0:
        print('number is positive')
    elif a<0:
        print('number is negative')
    else:
        print('number entered is 0')

n=int(input("please enter the number"))
numberCheck(n)