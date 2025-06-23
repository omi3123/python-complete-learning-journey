"""

1. Take two numbers as input from User and print which one is greater or 
are they equal.

"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter secound number: "))
if num1 > num2:
    print("num1 is greater")
elif num1 < num2:
    print("num2 is greater")
else:
    print("num1 and num2 are equal")

"""

2. Take three numbers as input from User and print which one is greater or 
are they equal.

"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter secound number: "))
num3 = int(input("Enter third number: "))
if num1 > num2 and num1 > num3:
    print("num1 is greater")
elif num2 > num1 and num2 > num3:
    print("num2 is greater")
else:
    print("num3 is greater")

"""

3. Take Salary as input from User and Update the salary of an employee
a. salary less than 10,000, 5 % increment
b. salary between 10,000 and 20, 000, 10 % increment
c. salary between 20,000 and 50,000, 15 % increment
d. salary more than 50,000, 20 % increment

"""  
salaryPerson = int(input("Enter salary: "))
if salaryPerson < 10000:
    salaryPerson = salaryPerson + (salaryPerson * 0.05)
elif salaryPerson > 10000 and salaryPerson < 20000:
    salaryPerson = salaryPerson + (salaryPerson * 0.1)
elif salaryPerson > 20000 and salaryPerson < 50000:
    salaryPerson = salaryPerson + (salaryPerson * 0.15)
else:
    salaryPerson = salaryPerson + (salaryPerson * 0.2)
print(salaryPerson)

"""

4. Ask the number from User and print whether the number is Odd or Even.

"""
num1 = int(input("Enter the number: "))
if num1 % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

"""

5. A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 – A
Ask user to enter marks and print the corresponding grade.

"""
marks = int(input("Enter the marks: "))
if marks < 25:
    print("Grade is F")
elif marks >= 25 and marks <= 45:
    print("Grade is  E")
elif marks >= 45 and marks <= 50:
    print("Grade is D")
elif marks >= 50 and marks <= 60:
    print("Grade is C")
elif marks >= 60 and marks <= 80:
    print("Grade is B")
else:
    print("Grade is A")

"""

6. A student will not be allowed to sit in exam if his/her attendance is less 
than 75%.
a. Take following input from user
i. Number of classes held
ii. Number of classes attended.
b. Print percentage of class attended
c. Print Is student is allowed to sit in exam or not.

"""
classesHeld = int(input("Enter the number of classes held: "))
classesAttend = int(input("Enter the number of classes attend: "))
percentage = (classesAttend / classesHeld) * 100
print(percentage)
if percentage < 75:
    print("You are not allowed to enter the exam")
else:
    print("You are allowed to enter the exam")

"""

7. Calculate the purchase amount after deduction criteria on printed price
a. printed price between 500 and 1000, allow 5% discount
b. printed price between 1000 and 5000, allow 10% discount
c. printed price between 5000 and 10000, allow 15% discount
d. printed price more than 10000, allow 20% discount

"""
printPrice = int(input("Enter the printed price: "))
if printPrice > 500 and printPrice < 1000:
    discount = 0.05
    print("Discount is 5%")
elif printPrice > 1000 and printPrice < 5000:
    discount = 0.10
    print("Discount is 10%")
elif printPrice > 5000 and printPrice < 10000:
    discount = 0.15
    print("Discount is 15%")
else:
    discount = 0.20
    print("Discount is 20%")