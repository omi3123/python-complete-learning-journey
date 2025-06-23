#1
numbers=[1,2,3,4,5,6]
even=filter(lambda x:x%2==0,numbers)
print(list(even))
#2
words=['apple','cherry','banana']
to_filter=filter(lambda word:len(word)>5,words)
print(list(to_filter))
#3
words=['apple','banana','cherry']
toF=filter(lambda word:len(word)>5,words)
print(list(toF))
#4
def is_positive(num):
    return num>0
numbers=[-1,-2,-3,4]
to_filter=filter(is_positive,numbers)
print(list(to_filter))
#5
names=['Ali','Umer','Usama']
to_filter=filter(lambda name:name.startswith('A'),names)
print(list(to_filter))
