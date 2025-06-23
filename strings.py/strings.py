"""

1. Python program to print even length words in a string

"""
str1 = "UmairBahsir"
for i in range(len(str1)):
    if i % 2 == 0:
        print(str1[i])
str1=input("Enter a string: ")
for i in range(len(str1)):
    if i%2==0:
        print(str1[i])


"""

2. Write a Python program to calculate the length of a string entered by a 
User.

"""
str1 = input("Enter the string: ")
print(len(str1))

"""

3. Write a Python program to reverse a string entered by User

# """
str1 = input("Enter the string: ")
print(str1[::-1])

"""

4. Count the number of vowels in a string entered by User.

"""
# str1 = input("Enter the string: ")
# count = 0
# for i in str1:
#     if i in "aeiou":
#         count += 1
# print(count)
str1=input("Enter a string: ")
count=0
for i in str1:
    if i in "aeiou":
        count+=1
print(count)
"""

5. Remove the even index characters from the string entered by User.
String: “PythonisGreat”
Answer: “PtoGet”

"""
str1 = "UmairBahsir"
str2 = ""
for i in range(len(str1)):
    if i % 2 != 0:
        str2 += str1[i]
print(str2)

"""

6. Write a Python program to reverse a string if its length is a multiple of 4.

"""
# so
# str1 = input("Enter a string: ")
# if len(str1) %4 == 0:
#     print(str1[::-1])
# else:
#     print(str1)

"""
7. Count number of digits in a string entered by user.

"""
str1 = input("Enter a string: ")
count = 0
for i in str1:
    if i.isdigit():
        count += 1
print(count)

"""

8. Check if the String entered by user is palindrome or not

"""
str1 = input("Enter a string: ")
if str1 == str1[::-1]:
    print("Yeah it is palindrome")
else:
    print("No it is not palindrome")

"""

9. Find all duplicate characters in string entered by user

"""
str1 = input("Enter a new string: ")
str2 = ""
for i in str1:
    if i not in str2:
        str2 += i
    else:
        print(i)
print(str2)

"""

10. Reverse Sort a String entered by user

"""
str1 = input("Enter a string: ")
print(sorted(str1, reverse=True))
str1=input("Enter a string: ")
print(sorted(str1,reverse=True))