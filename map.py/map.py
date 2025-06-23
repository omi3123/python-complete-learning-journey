#1
numbers=[1,2,3,4,5]
squared=map(lambda x:x**2,numbers)
print(list(squared))
#2
words = ["apple", "banana", "cherry"]
uppercased_words = map(lambda word: word.upper(), words)
print(list(uppercased_words))  
#3
def double(x):
    return x * 2
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)
print(list(doubled_numbers))  
#4
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summed_numbers = map(lambda x, y: x + y, numbers1, numbers2)
print(list(summed_numbers)) 
#5
students={"ALi":21,"Umer":22,"Usama":23}
to_map=map(lambda score:score+5,students.values())
print(list(to_map))