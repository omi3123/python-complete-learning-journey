list1= [1, 2, 3, "Umair", True, False, 5, 7]
sumList=[x for x in list1 if isinstance(x,int)]
prod=1
if sumList:
    for i in sumList:
        prod+=i
    print(f"product is {prod}")
else:
    print("nothing")
"""

1. Write a Python program to sum all the items in a list.

"""
# list1= [1, 2, 3, 4, 5]
# sum_list = list1[0]+list1[1]+list1[2]+list1[3]+list1[4]
# print(sum_list)
# list1= [1, 2, 3, "Umair", True, False, 5, 7]
# a= [x for x in list1 if isinstance(x, int)]
# if a:
#     print(f"Sum of integer is {sum(a)}")
# else:
#     print("No integer in the list")

# list2= [34, True, "Umair", "Ali", 36]
# a= [x for x in list2 if isinstance(x, int)]
# if a:
#     print(f"The sum of integers is {sum(a)}")
# else:
#     print("No integers in the list")
# list1 = [1,2,3,4,5]
# a = sum(list1)
# print(a)
list1=[1,2,3,4,5]
vari=[allNum for allNum in list1 if allNum%2==0]
if vari:
    print(f"even number is {vari}")

"""

2. Write a Python program to multiply all the items in a list.

"""

# list1= [2, 4, 6, "Umair"]
# a= [x  for x in list1 if isinstance(x, int)]
# print(a)
# product= a[0]*a[1]*a[2]

# print(product)
# # if a:
#     print(f"The product of integers is {(a*a)}")
# else:
#     print("No product")
# list1= [2, 4, 6, "Umair"]
# integers= [x  for x in list1 if isinstance(x, int)]
# product= 1 
# if integers:
#     for x in integers:
#         product*= x
#     print(f"The product of integers is {product}")
# else:
#     print("There were no integers")
list1=[1,2,3,4,5,"Usama"]
integers=[char for char in list1 if isinstance(char,int)]
product=1
if integers:
    for x in integers:
        product*=x
    print(f"prodcut is {product}")
"""

3. Take 10 integer inputs from user and store them in a list and print them 
on screen.

"""
list1= []
for i in range(1, 11):
    inputVar= int(input("Enter the integers: "))
    print(i)    
    list1.append(inputVar)
print(list1)

"""

4. Take 20 integer inputs from user and print the following:
a. number of positive numbers
b. number of negative numbers
c. number of odd numbers
d. number of even numbers
e. number of 0s.

"""
# posNum= 0
# negNum= 0
# oddNum= 0
# evenNum= 0
# zeroNum= 0
# for i in range(1, 5):
#     inputVar= int(input("Enter the integers: "))
#     if inputVar > 0:
#         posNum+= 1
#     elif inputVar < 0:
#         negNum+= 1
#     elif (inputVar %2 == 0):
#         evenNum+= 1
#     elif (inputVar %2 != 0):
#         oddNum+= 1
#     elif inputVar == 0:
#         zeroNum+= 1
#     else:
#         print("No number found")
# print(f"The total number of postive integers are {posNum} ")
# print(f"The total number of negative integers are {negNum} ")
# print(f"The total number of even integers are {evenNum} ")
# print(f"The total number of odd integers are {oddNum} ")
# print(f"The total number of zero integers are {zeroNum} ")

posNum = 0
negNum = 0
oddNum = 0
evenNum = 0
zeroNum = 0
for i in range(5):  
    inputVar = int(input("Enter an integer: "))
    if inputVar == 0:
        zeroNum += 1
    else:
        if inputVar > 0:
            posNum += 1
        elif inputVar < 0:
            negNum += 1
        if inputVar % 2 == 0:
            evenNum += 1
        else:
            oddNum += 1
print(f"The total number of positive integers is {posNum}")
print(f"The total number of negative integers is {negNum}")
print(f"The total number of even integers is {evenNum}")
print(f"The total number of odd integers is {oddNum}")
print(f"The total number of zero integers is {zeroNum}")

"""

5. Take 10 integer inputs from user and store them in a list. Again, ask user 
to give a number. Now, tell user whether that number is present in list or 
not

"""
list1 = []
for i in range(11):
    inputVar = int(input("Enter an integer: "))
    list1.append(inputVar)
print(list1)
num = int(input("Enter a number to check: "))
if num in list1:
    print(f"{num} is present in the list")
else:
    print(f"{num} is not present in the list")

"""

6. Make a list by taking 10 inputs from user. Now delete all repeated
elements of the list.
E.g.-
INPUT: [1,2,3,2,1,3,12,12,32]
OUTPUT: [1,2,3,12,32]

"""
# list1= []
# filtered_list=[]
# for i in range(5):
#     inputVar = int(input("Enter an integer: "))
#     list1.append(inputVar)
#     if inputVar  not in filtered_list:
#         filtered_list.append(inputVar)
# print(filtered_list)
listed=[1,2,3,4,555,555,6,6,5,4,3]
filtered_list=[]
for i in listed:
    if i not in filtered_list:
        filtered_list.append(i)
print(filtered_list)
"""

7. Ask user to give integer inputs to make a list. Store only even values given 
and print the list.

"""
list1 = []
for i in range(5):
    inputVar = int(input("Enter an integer: "))
    list1.append(inputVar)
    if inputVar % 2 == 0:
        list1.append(inputVar)
    print(list1)