student_info = {"name" : "Umair", "roll" : 23, "total marks": 100}
for i in student_info:
    print(i, student_info[i], sep=":") 
"""

1. Merge two Python dictionaries into one.

"""
# dict1 = {"name" : "Umair", "roll" : 23, "total marks" : "100"}
# dict2 = {"name" : "Ali", "roll" : 22, "total marks" : 100}
# dict1.update(dict2)
# print(dict1)

dict1 = {"name" : "Umair", "roll" : 23, "total marks" : "100"}
dict2 = {"name" : "Ali", "roll" : 22, "total marks" : 100}
dict1.update(dict2)
print(dict1)
"""

2. Write a python program to find the sum of all items in a dictionary.

"""
dict1 = {"student1 number" : 78, "student2 number" : 79, "student3 number" : 80}
print(sum(dict1.values()))
dict1 = {"student1 number" : 78, "student2 number" : 79, "student3 number" : 80}
print(sum(dict1.values()))
"""
3. Write a python program to check whether a given key already exists in a 
dictionary.

"""
dict1 = {"name" : "Umair", "roll" : 23, "marks" : 100}
if "name" in dict1:
    print("Key exists")
else:
    print("Not found")

"""

4. Write a Python program to iterate over dictionaries using for loops.

"""
dict1 = {"name" : "Umair", "roll" : 23, "marks" : 100}
for i in dict1:
    print(i, dict1[i], sep=":")

"""

5. Write a Python program to generate and print a dictionary that contains 
a number (between 1 and n) in the form (x, x*x).
Sample Dictionary: (n = 6)
Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

"""
# n = 6
# dict1 = {i: i*i for i in range(1, n+1)}
# print(dict1)

n = 6
list1 = []
for i in range(1, n+1):
    a = (i, i*i)
    list1.append(a)
print(dict(list1))

"""

6. Write a Python program to map two lists into a dictionary.

"""
list1 = ["name", "roll", "marks"]
list2 = ["Umair", 100]
dict1 = dict(zip(list1, list2))
print(dict1)

"""

7. Write a Python program to get the maximum and minimum value in a 
dictionary.

"""
dict1 = {"score" : 21, "roll" : 23, "marks" : 100}
print(max(dict1.values()))
dict2 = {"score" : 20, "roll" : 21, "marks" : 20}
print(min(dict2.values()))

"""

8. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'hellopython'
Expected output: {'h': 2, 'e': 1, 'l': 2, 'o': 2, 'p': 1, 'y': 1, 't': 1, 'n': 1}

"""
# str1 = "hellopython"
# n = len(str1)
# list1 = []
# for char in range(1, n+1):
#     a = (n, char)
#     print(a)
# yeah
# str1 = "hellopython"
# list1 = []
# for i in str1:
#     list1.append(i)
# print(list1)

# str1 = "hellopython"
# dict1 = {}
# for char in str1:
#     if char in dict1:
#         dict1[char] += 1
#     else:
#         dict1[char] = 1
# print(dict1)


str1="hellopython"
dict1={}
for i in str1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)
"""
 
 9. Write a Python program to print a dictionary in table format.

"""
# dict1 = {"Name" : "Umair", "Friend" : "Ali", "Dream" : "Backend Developer"}
# for k,v in dict1.items():
#     print("{:6s}{}".format(k, v))

# dict2 = {"Name: ": "Muhammad Umair Bahsir", "DOB" : 2003, "BM" : "Nov"}
# for k,v in dict2.items():
#     print("{:6s}{}".format(k, v))

dict2 = {"Name: ": "Muhammad Umair Bahsir", "DOB:" : 2003, "BM:" : "Nov"}
for k,v in dict2.items():
    print("{:6s}{}".format(k,v))

"""

10. A Python Dictionary contains List as value. Write a Python program to 
clear the list values in the said dictionary.
Original Dictionary:
{'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
Clear the list values in the said dictionary:
{'C1': [], 'C2': [], 'C3': []}

"""
# dictMain = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for k , v in dictMain.items():
#     dictMain[k]=[]
# print(dictMain)
# dictValues = dictMain.values()
# for value in dictValues:
#     for i in range(len(value)):
#         value.clear()
# print(dictMain)
# OR
dictMain = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
for i in dictMain.keys():
    dictMain[i] = []
print(dictMain)

"""

11. Write a Python program to convert a given dictionary into a list of lists.
Original Dictionary:
{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
Convert the said dictionary into a list of lists:
[[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
Original Dictionary:
{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie 
Rowe'}
Convert the said dictionary into a list of lists:
[['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 
'Jamie Rowe']]

"""
dict1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
myList = []
for k,v in dict1.items():
    myList.append([k, v])
print(myList)
#Prime or not
n=int(input("enter n value: "))
i=2
while i<=(n-1):
    if n%i==0:
        print("non prime")
        exit()
    else:
        i+=1
print("Prime")