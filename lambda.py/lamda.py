#1
add=lambda x,y:x+y
print(add(5,3))
#2
numbers=[1,2,3,4,5]
squared=map(lambda x: x**2,numbers)
print(list(squared))
#3
numbers=[1,2,3,4,5,6]
even=filter(lambda x:x%2==0,numbers)
print(list(even))
#4
students=[("ali",21),("umer",20),("usama",22)]
sorted_students=sorted(students,key=lambda x:x[1])
print(sorted_students)
#5
def multiplication(n):
    return lambda x:x*n
multiple=multiplication(2)
print(multiple(5))
#6
from functools import reduce
numbers=[1,2,3,4,5]
factorial=reduce(lambda x,y:x*y,numbers)
print(factorial)
#7
words = ["apple", "banana", "cherry"]
uppercased_words = map(lambda word: word.upper(), words)
print(list(uppercased_words))  
#8
students={"ALi":21,"Umer":22,"Usama":23}
to_map=map(lambda score:score+5,students.values())
print(list(to_map))