"""

1. Write a Python function to find the Max of three numbers.

"""
def maxofNum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else: 
        return c
print(maxofNum(11, 12, 13))

"""

2. Write a Python function to sum all the numbers in a list.

"""

def sumList(list1):
    return sum(list1)
print(sumList([1, 2, 3, 4, 5]))

"""

3. Write a Python function to reverse a string.

"""
def rString(str1):
    return str1[::-1]
print(rString("Hello World"))

"""

4. Write a Python function that takes a number as a parameter and check 
the number is prime or not.

"""
# def primeNum(num1):
#     totalFactor = 0
#     for i in range(1, num1 +1):
#         if num1 % i == 0:
#             totalFactor += 1
#     if totalFactor == 2:
#         print(f"{num1} is a prime number")
#     else:
#         print("No num is found as a prime number")
# primeNum(13)

# def primeNum(num1):
#     total_factor=0
#     for i in range(1,num1+            1):
#         if num1%i==0:
#             total_factor+=1
#     if total_factor==2:
#         print(f"{num1} is a prime number")
#     else:
#         print("No")
# print(primeNum(23))
def prime_number(number):
    total_factor=0
    for i in range(1,number+1):
        if number%i==0:
            total_factor+=1
    if total_factor==2:
        print("Prime Number")
    else:
        print("Not a prime number")
print(prime_number(23))
"""

5. Write a Python program to print the even numbers from a given list.
Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result: [2, 4, 6, 8]

"""
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def evenNumList(list1):
#     return [i for i in list1 if i % 2 == 0]
# print(evenNumList(list1))
def even_number_list(list_):
    return [i for i in list_ if i%2==0]
print(even_number_list([1,2,3,4,5,6,7,8]))
"""

6. Write a Python function that checks whether a passed string is 
palindrome or not.

"""
def palindrome(str1):
    return str1 == str1[::-1]
print(palindrome("madam"))