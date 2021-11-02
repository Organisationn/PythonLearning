sizeOfArray=int(input('Please enter the size of the array: '))

numbersArray=[]
count=0
while(count<sizeOfArray):
    try:
        number=int(input('Enter a number: '))
        numbersArray.append(number)
        count += 1
    except ValueError:
        print('This is not a number!!!')
        pass

print(numbersArray)