# intializing the list
arr = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# initializing dict to store frequency of each element
elements_count = {}
# iterating over the elements for frequency
for element in arr:
   # checking whether it is in the dict or not
   if element in elements_count:
      # incerementing the count by 1
      elements_count[element] += 1
   else:
      # setting the count to 1
      elements_count[element] = 1
# printing the elements frequencies
for key, value in elements_count.items():
   print(f"{key}: {value}")