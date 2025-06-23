"""

10. Print first 10 Natural numbers.

"""
i = 0
for i in range(1, 11):
    print(i)

"""

11. Print all the even numbers from 1 to 100.

"""
for i in range(2, 101, 2):
    print(i)

"""

12. Find sum of N numbers where N is input from User.

"""
n = int(input("Enter the number of elements: "))
sum = 0
for i in range(n+1):
    sum += i
print(sum)

"""
for i in range(2)
13. Check whether number entered by User is Prime or Not using for loop.

"""
num = int(input("Enter the number: "))
is_prime = True
for i in range(2, num):
    if (num % i == 0):
        is_prime = False
        break
if is_prime and num > 1:
    print("Number is Prime")
else:
    print("Number is not prime")    

"""

14. Check whether number entered by User is Armstrong or not.

"""
num = int(input("Enter a number: "))
a = str(num)
print(a)
sum = 0
for i in a:
    sum += int(i)**len(a)
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong")

"""

15. Print multiplication table of a number entered by user.

"""
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{i} X {num} = {num*i}")

"""

16. Program to display all the prime numbers within a range.

"""
is_prime = True
for i in range(1, 101):
    if i%2 != 0 and is_prime:
        print(i)
        is_prime = False
    continue
if is_prime:
    print("These are prime number")
else:
    print("No prime number found")
print(i)    
number = int(input("Enter any number = "))
for i in range(1, number + 1):
    totalFactors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            totalFactors += 1
    if totalFactors == 2:
        print(f"{i} is a prime number")