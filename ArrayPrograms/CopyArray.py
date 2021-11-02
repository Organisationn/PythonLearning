# 1st way

# arr1=[1,2,3,4,5]
# arr2 = [None] * len(arr1);
#
# for i in range(0,len(arr1)):
#     arr2[i]=arr1[i]
#
# print("Elements of original array: ");
# for i in range(0, len(arr1)):
#    print(arr1[i]),
#
# print("Elements of new array: ");
# for i in range(0, len(arr2)):
#    print(arr2[i]),

#2nd way
# arr1=[10,20,30,40,50]
# arr2=[]
# for i in range(0,len(arr1)):
#     arr2.append(arr1[i])
# print(arr2)

#3rd syntax for for loop
# def Cloning(li1):
#     li_copy = []
#     for item in li1:
#         li_copy.append(item)
#     return li_copy
#
# # Driver Code
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = Cloning(li1)
# print("Original List:", li1)
# print("After Cloning:", li2)

#4th way using copy()
# arr1=[1,3,2,33,54]
# arr2=arr1.copy()
# print(arr1)
# print(arr2)

#5th way using list()
arr1=[1,3,2,33,54]
arr2=list(arr1)
print(arr1)
print(arr2)