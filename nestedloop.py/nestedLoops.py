"""


17. Make the following Patterns using for
a.
*
**
***
****
*****

"""
# n = 5
# for x in range(1, n + 1):
#     for y in range(1, x + 1):
#         print("*", end=" ")
#     print()
n=5
for x in range(1,n+1):
    for j in range(1,x+1):
        print("*",end=" ")
    print()
"""

b. 1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""
# n = 5
# for x in range(1, n + 1):
#     for y in range(1, x + 1):
#         print(y, end=" ")
#     print()
n=5
for x in range(1,n+1):
    for j in range(1,x+1):
        print(j,end=" ")
    print()
"""
Make the pattern using for nested loop
c.
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1

"""
n = 5
for x in range(1, n + 1):
    for y in range(n, n - x, -1):
        print(y, end=" ")
    print()

"""
d. Make this pattern using nested for loop.
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

"""

for x in range(5, 0, -1):
    for y in range(x):
        print(x, end=" ")
    print()

"""
e. Make this pattern using nested for loop
        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1

"""
for i in range(1, 6):
    for j in range(5, i, -1):
        print(f" ", end=" ")
    for k in range(i, 0, -1):
        print(f" {k}", end="")
    print()

"""

f. Make this pattern using nested for loops.
        5
      4 5
    3 4 5
  2 3 4 5
1 2 3 4 5

"""

"""

18. Write a program to display following Output
a. 1 2 3 4 5 6 7 8 9 10

"""
for i in range(1, 11):
    print(i, end=" ")

"""

18. Write a program to display following Output
b. 2 4 6 8 10 12 14 16 18 20

"""
for i in range(2, 21, 2):
    print(i, end=" ")

"""

18. Write a program to display following Output
c. 3 6 9 12 15 18 21 24 27 30

"""
for i in range(3, 31, 3):
    print(i, end=" ")

"""

18. Write a program to display following Output
d. 4 8 12 16 20 24 28 32 36 40

"""
for i in range(4, 41, 4):
    print(i, end=" ")

"""

18. Write a program to display following Output
e. 5 10 15 20 25 30 35 40 45 50

"""
for i in range(5, 51, 5):
  print(i, end=" ")