import random
# 1)random module provides a random() method which generates a float number between 0 and 1
n=random.random()
print(n)

# 2)random module provides the randint() method that generates an integer number within a specific range.
n=random.randint(0,50)
print(n)

n=random.randint(100,500)
print(n)

#using for loop
rand_list=[]
for i in range(0,10):
    n=random.randint(1,50)
    rand_list.append(n)
print(rand_list)

#3)random module also provides the sample() method, which directly generates a list of random numbers
# we have used the range() function, which generates the numbers between the given range.

random_list=random.sample(range(10,40),3)
print(random_list)