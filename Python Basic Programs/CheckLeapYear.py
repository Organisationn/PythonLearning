def checkLeapYear(yy):
    if((yy%400==0) or (yy%100!=0) and (yy%4==0)):
        print('given year is leap year')
    else:
        print('not a leap year')
year=int(input('please enter the year'))
checkLeapYear(year)