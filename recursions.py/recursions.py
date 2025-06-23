#Factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
#Fibomacci
def fibonacci(n):
    if n <= 1:  
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5))
#Sum of natural
def sum_natural(n):
    if n == 1: 
        return 1
    else:
        return n + sum_natural(n - 1)  
print(sum_natural(10))
#Power
def power(x, y):
    if y == 0: 
        return 1
    else:
        return x * power(x, y - 1)  
print(power(5,3))
#Reverse String
def reverse_string(s):
    if len(s) == 0:  
        return s
    else:
        return reverse_string(s[1:]) + s[0] 
print(reverse_string("umair"))