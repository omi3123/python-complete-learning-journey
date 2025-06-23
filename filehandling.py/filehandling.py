"""

1. Write a Python program to read an entire text file.

"""
f = open("myfile.txt", "r" )
text = f.read()
print(text)
f.close()

"""

2. Write a Python program to read a file line by line and store it into a list.

"""
f = open('myfile.txt', 'r')
text = f.readlines()
print(text)
f.close

"""

3. Write a python program to find the longest words.

"""
# f = open('myFile.txt', 'r')
# text = f.read()
# words = text.split()
# longestWord = max(words, key= len)
# print(longestWord)
# f.close

# f = open("myFile.txt", "r")
# words = f.read().split()
# print(words)
# longWord = ""
# for i in words:
#     if len(i) > len(longWord):
#         longWord = i
# print(longWord)
# f.close()
f=open('myFile.txt','r')
text=f.read()
words=text.split()
longest_word=max(words,key=len)
print(longest_word)
f.close()

"""

4. Write a Python program to count the number of lines in a text file.

"""
f = open('myFile.txt', 'r')
count = 0
for line in f:
    count += 1
print(count)
f.close()


"""

5. Write a Python program to count the frequency of words in a file.

"""
f = open('myFile.txt', 'r')
word = f.read().split()
myWord = []
for i in word:
    if i not in myWord:
        myWord.append(i)
for i in myWord:
    print(i, myWord.count(i))
f.close()

"""

6. Write a Python program to copy the contents of a file to another file.

"""
f = open('myFile.txt', 'r')
copy = f.read()
f.close()
f = open("myFile2.txt", "w")
f.write(copy)
f.close()

"""

7. Write a Python program to read a random line from a file

"""
import random
f = open('myFile.txt', 'r')
lines = f.readlines()
f.close()
print(random.choice(lines))