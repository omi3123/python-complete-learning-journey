"""

1. Write a program that takes two numbers as input from the user and then 
prints the sum of these numbers.

"""
num1= int(input("Enter first number: "))
num2= int(input("Enter secound number: "))
sum= num1+num2
print(sum)

"""

2. Write a Program that takes Length and Breadth as input from user and 
print the Area of Rectangle.

"""
len= int(input("Enter the lenght: "))
bread= int(input("Enter the breadth: "))
area= len*bread
print(area)

"""

3. Ask 3 numbers from User and Calculate the Average.

"""
num1= int(input("Enter number 1: "))
num2= int(input("Enter number 2: "))
num3= int(input("Enter number 3: "))
sum= num1+num2+num3
average= sum/3
print(average)

"""

4. Calculate sum of 5 subjects and Find percentage.

"""
# subjects marks should be between 1-1000
# total marks are 500
sub1= int(input("Enter marks of subject 1: "))
sub2= int(input("Enter marks of subject 2: "))
sub3= int(input("Enter marks of subject 3: "))
sub4= int(input("Enter marks of subject 4: "))
sub5= int(input("Enter marks of subject 5: "))
gainMarks= sub1+sub2+sub3+sub4+sub5
percentage= (gainMarks/500)*100
print(percentage)

"""

5. Ask value in Rupees and Convert into Paise.

"""

amount= int(input("Enter the amount in Rupees: "))
paise= amount*100
print(paise)

"""

6. Calculate Area of Square by taking Length from User.

"""
len= int(input("Enter the length1: "))
area= len*len
print(f"The area of a square is {area}")

"""

7. Ask number of games played in a tournament. Ask the user number of 
games won and number of games loss. Calculate number of tie and total 
Points. (1 win= 4 points, 1 tie =2 points)

"""

gamesPlayed= int(input("Enter the number of games played: "))
gamesWon= int(input("Enter the number of games won: "))
gamesLoss= int(input("Enter the number of games loss: "))
gamesTie= 10-(gamesWon+gamesLoss)
wonPoints= 4*gamesWon
print(f"Total games tie are {gamesTie}")
tiePoints= 2*gamesTie
print(f"Total tie points are {tiePoints}")
print(f"Total winnig points are {wonPoints}")