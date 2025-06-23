"""

1. Calculate the sum of all the numbers in a tuple.

"""
numbers = (1, 2, 3, 4, 5)
sum_of_numbers = sum(numbers)
print(sum_of_numbers)
#OR
num= ("Ali", "Umair", 11, 31, 8)
a = [x for x in num if isinstance(x, int)]
if a:
    print(f"Sum of integer in tuple is {sum(a)}")
else:
    print("No num is found")
"""

2. Create a tuple with some numbers. Ask a random number from user and 
add that number to the end of the tuple.

"""
numbers = (1, 2, 3, 4, 5)
list1 = []
newNum = int(input("Enter a number: "))
list1.append(newNum)
a = tuple(list1)
sum = numbers + a
print(sum)
"""

3. Write a Python program to get the 4th element and 4th element from 
last of a tuple.

"""
numbers = (1, 2, 3, 4, 5, 6)
print(numbers[3])
print(numbers[-4])

"""

4. Write a Python program to find the repeated items of a tuple.

"""
# tuple1= (1, 2, 3, 3, "Umair")
# rep_items = set()
# seen_items = set()
# a = [x for x in tuple1 if isinstance(x, int)]
# if a:
#     print(a)
# else:
#     print("Nothing found")
# for num in tuple1:
#     if num in seen_items:
#         rep_items.add(num)
#     else:
#         seen_items.add(num)
# print(rep_items)
# tuple2 = (1, 2, 2, 4, 4, 5, "Umair", "Umair", "Ali", "Ali")
# seen_items = set()
# rep_items = set()
# for num in tuple2:
#     if num in seen_items:
#         rep_items.add(num)
#     else:
#         seen_items.add(num)    
# print(tuple(rep_items))

# tuple1=(1,1,2,3,2,4)
# seen_items=set()
# rep_items=set()
# for num in tuple1:
#     if num in seen_items:
#         rep_items.add(num)
#     else:
#         seen_items.add(num)
# print(tuple(rep_items))
list1=[1,1,3,4,4]
list2=[]
rep=[]
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        rep.append(i)
print(rep)

"""

5. Write a Python program to remove a number entered by user from a 
tuple.

"""
list1 = []
for i in range(3):
    print(int(input("Enter the number: ")))
    list1.append(i)
print(list1)
a = tuple(list1)
print(a)
num = int(input("Enter the number to remove: "))
if num in a:
    a = tuple([x for x in a if x != num])
    print(a)
else:
    print("Number is not found in a")
list1=[1,2,3]
to_eliminate=list1.remove(int(input("Enter a number to remove: ")))
print(list1)


"""

6. Write a Python program calculate the product, multiplying all the
numbers of a given tuple.
Original Tuple:
(4, 3, 2, 2, -1, 18)
Product - multiplying all the numbers of the said tuple: -864

"""
tuple1 = (4, 3, 2, 2, -1, 18)
product = 1
for num in tuple1:
    product *= num
print(product)