#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This file contains all the exercises (Problem 1 and Problem 2)

#### PROBLEM 1 ####


### Introduction

#Say "Hello, World!" With Python

if __name__ == '__main__':
    print("Hello, World!")

#Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print('Weird')
    elif (n%2 == 0) and n>=2 and n<=5:
        print('Not Weird')
    elif (n%2 == 0) and n>=6 and n<=20:
        print('Weird')        
    elif (n%2 == 0) and n > 20:
        print('Not Weird')   

#Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b) 
    print(a/b)

#Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

#Write a function

def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        leap = True
    elif (year % 4 == 0 and year % 100 != 0 ):
        leap = True    
        
    return leap

#Print Function

if __name__ == '__main__':
    n = int(input())
    
    l = []
    v = ""
    
    for i in range(1,n+1):
        l.append(i)
    
    for i in l:
        v += str(i)
    print(v)



### Data Types

#List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # Let's create the ranges in which i, j, k can move
    e = list(range(x+1))
    f = list(range(y+1))
    g = list(range(z+1))

    # I create the list with all the permutations with the syntax contained in the documentation of the lists here:   https://docs.python.org/3/tutorial/datastructures.html
    permut = [ [i, j, k] for i in e for j in f for k in g ]
    permut

    l = [] 

    for i in permut:
        if sum(i) != n:
            l.append(i)
            
    print(l)

#Find the Runner-Up Score!  

if __name__ == '__main__':
    l = []

    if __name__ == '__main__':
        n = int(input())
        arr = map(int, input().split())
    
    for e in arr:
        l.append(e)
    
    l = list(dict.fromkeys(l))    
    l.sort(reverse = True)
    print(l[1])   

#Nested Lists

if __name__ == '__main__':
    l = []
    l2 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])

    l.sort(key = lambda x: (x[1], x[0]))

    if len(l)  == 1:
        print(l[0][0]) # if you have N=1, print the name of the only student in the class
    for i in range(len(l)):
        l2.append(l[i][1])
    
    l2 = list(dict.fromkeys(l2)) #similar to the example here:  https://www.w3schools.com/python/python_howto_remove_duplicates.asp

    for i in range(len(l)):
        if l2[1] in l[i]:  # if the second-lowest grade is common with other students...
            print(l[i][0])

#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split() 
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    
    grades = student_marks[query_name]
    print('%0.2f' % (sum(grades)/len(grades))) # don't know why round() function doesn't work

#Lists

if __name__ == '__main__':
    
    l = []
    
    N = int(input())
    
    
    for i in range(N):  # we have to do N operations on the list
        x = input().split()
        if x[0] == 'insert':  #i = position, e = number you have to insert
            l.insert(int(x[1]), int(x[2]))
        elif x[0] == 'print':  
            print(l)
        elif x[0] == 'sort':
            l.sort()
        elif x[0] == 'pop':
            l.pop(-1)
        elif x[0] == 'reverse':
            l.reverse()
        elif x[0] == 'remove':
            l.remove(int(x[1]))
        elif x[0] == 'append':
            l.append(int(x[1]))
        else:
            print('You have to choose one of the 7 commands above') 

# Tuples

# IMPORTANT NOTE: I don't know why, but it only works if you set Pypy 3 as Language.
# (a computer science colleague tried to explain to me)

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    
    t = tuple([n for n in integer_list])
    print(hash(t)) # it only works with the print() function!!



### Strings

#sWAP cASE

def swap_case(s):
    v = ""
    for i in s:
        if i.isalpha() == False:
            v += i
        elif i.isupper():
            v += i.lower()
        elif i.islower():
            v += i.upper()          
    return v

#String Split and Join

def split_and_join(line):
    x = line.split(" ")
    x = '-'.join(x)
    return x

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print('Hello', first, last + '! You just delved into python.')

#Mutations

def mutate_string(string, position, character):
    l = list(string)
    l[position] = str(character)
    return ''.join(l)

#Find a string

def count_substring(string, sub_string):
    
    counter = 0
    a = len(string)
    b = len(sub_string)
    
    
    for i in range(a-b+1):
        new_s = string[i:i+b]
        if sub_string == new_s:
            counter += 1
            new_s = ""    
    return counter

#String Validators

if __name__ == '__main__':
    s = input()
    
    counter = 0
    
    # 1. alphanumeric check
    for i in s:
        if i.isalnum():
            counter += 1
    if counter > 0:
        print(True)    
        counter = 0
    else:
        print(False)
        
    # 2. alfabetic check    
    for i in s:
        if i.isalpha():
            counter += 1
    if counter > 0:
        print(True)    
        counter = 0
    else:
        print(False)
    
    # 3. digit check    
    for i in s:
        if i.isdigit():
            counter += 1
    if counter > 0:
        print(True)    
        counter = 0
    else:
        print(False)
    
   # 4. lower-case check    
    for i in s:
        if i.islower():
            counter += 1
    if counter > 0:
        print(True)    
        counter = 0
    else:
        print(False)
        
    # 5. upper-case check    
    for i in s:
        if i.isupper():
            counter += 1
    if counter > 0:
        print(True)    
        counter = 0
    else:
        print(False)    

#Text Alignment

#Replace all ______ with rjust, ljust or center. 

# NOTE:
# After many attempts I found that it was enough to change the Language from 'Pypy3' to 'Python 3' and replace the ___ with ljust, rjust and center.
# However, I tried to write some code that also works for even numbers, but it only works partially. Here is how i did:

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

  
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap


'''
# Option 1: do the exercise without importing any library:
if len(s)%n == 0:
    for i in range(len(s)//n):
        new_s = s[i:i+n-1]
        print(new_s)
        new_s = ""
else:
    for i in range(len(s)//n +1):
        new_s = s[4*i:4*i+n]
        print(new_s)
        new_s = ""
    print(s[-(len(s)%n -1) : -1])
'''

# Option 2: use textwrap
def wrap(string, max_width):
    l = textwrap.wrap(string, max_width)
    
    for i in l:
        print(i)
    return '' 

#Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = input().split()

for i in range(int(N)//2):
    print( ('.|.'*(2*i+1)).center(int(M), '-'))

print( ('WELCOME').center(int(M), '-'))

for i in range(int(N)//2 - 1, -1, -1):
    print( ('.|.'*(2*i+1)).center(int(M), '-'))

#String Formatting
# I use the built-in functions of python: bin(), oct(), hex()

def print_formatted(number):
    sp = len(bin(number)[2:])  # length of the binary number in input
    for i in range(1, number+1):
        print((str(i)).rjust(sp, " "), (oct(i)[2:]).rjust(sp, " "), (hex(i).upper()[2:]).rjust(sp, " "), (bin(i)[2:]).rjust(sp, " ") )
        # rjust works for strings!

#Alphabet Rangoli

def print_rangoli(size):
    let = 'abcdefghijklmnopqrstuvwxyz'
    l = []
    l2 = []

    if size == 1:
        print('a')
    else:
        for i in range(0, size):
            l.append(let[i])

        l1 = l[::-1]
        x = '-'.join(l[::-1]) + '-' + '-'.join(l[::-1][-2::-1]) #  central line
        lenght = len(x)

        print( (let[size-1]).center(lenght, '-') )  # 1 cosa da stampare
    
        for i in range(2, size):
            print(('-'.join(l1[0:i]) + '-' + '-'.join(l1[i-2::-1])).center(lenght, '-'))

        print(x) # riga centrale

        for i in range(size-1, 1, -1):
            print(('-'.join(l1[0:i]) + '-' + '-'.join(l1[i-2::-1])).center(lenght, '-'))

        print( (let[size-1]).center(lenght, '-') )  # ultima riga da stampare

#Capitalize!

# Complete the solve function below.
'''
def solve(s):
    l = s.split()
    # s = l[0][0].upper()+l[0][1:] + ' ' + l[1][0].upper()+l[1][1:]  --> WRONG: beacuse if you have more than 2 words it doesn't work! So we can do like this:
    for i in l:
        i[0] = i[0].upper() 
    return s
'''

'''
def solve(s):
    l = s.split()
    x = [] 
    empty = ""

    x = [parola[0].upper()+parola[1:]+" " for parola in l]

    for i in x:
        empty += i
    
    return empty  

# WRONG: watch the spaces!
'''

def solve(s):
    l = s.split(" ")
    x = []
    empty = ""

    for i in l:
        if i == "":
            x += " "
        elif len(i)==1:
            x += i.upper() + " "
        else:
            x += i[0].upper() + i[1:] + " "
            

    for i in x:
        empty += i
        
    return(empty)

#Merge the Tools!

def merge_the_tools(string, k):
    
    if k == 1:
        l = []
        for letter in string:
            l.append(letter)
        for x in l:
            print(x)       
    else:
        for i in range(k):
            t = string[i*k : i*k + k]
            d = {}
            u = ''
            for letter in t:
                d[letter] = 1
     
            for key in d.keys():
                u += str(key)
                
            print(u)    



### Sets

#Introduction to Sets

def average(array):
    mean = sum(set(array))/len(set(array))  #because we need distinct heights, we remove the duplicates turning the list     into a set
    return mean

#No Idea!

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()
integers = input().split() # n integers

a = set(input().split()) # m integers
b = set(input().split()) # m integers
# Why set? Because the last set has a lot of numbers, so I delete the duplicates and it doesn't raise a runtime error

happiness = 0

for i in integers:
    if i in a:
        happiness += 1
    if i in b:   
        happiness -= 1
                
print(happiness) 



#Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT

m = input()
l1 = input()
list1 = set(map(int, l1.split()))

n = input()
l2 = input()
list2 = set(map(int, l2.split()))

a = list1.difference(list2)
b = list2.difference(list1)

lista = []
for i in a:
    lista.append(i)
for i in b:
    lista.append(i)    
    
lista = sorted(lista)
for i in lista:
    print(i)

#Set .add() 

# Enter your code here. Read input from STDIN. Print output to STDOUT

s = set()

n = int(input())
for i in range(n):
    x = input()
    s.add(x)
print(len(s))  

#Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
N = int(input())


for i in range(N):
    x = input().split()
    if x[0] == 'pop':
        s.pop()
    if x[0] == 'remove':
        s.remove(int(x[1]))
    if x[0] == 'discard':
        s.discard(int(x[1]))
        
print(sum(s)) 

#Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s1 = set(map(int, input().split()))

b = int(input())
s2 = set(map(int, input().split()))

s3 = set(s1.union(s2))

counter = 0

for i in s3:
    counter += 1
    
print(counter)   

#Set .intersection() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
s1 = set(map(int, input().split()))

b = int(input())
s2 = set(map(int, input().split()))

s3 = set(s1.intersection(s2))

counter = 0

for i in s3:
    counter += 1
    
print(counter) 

#Set .difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n_english = int(input())
s_english = set(map(int, input().split()))

b_french= int(input())
s_french = set(map(int, input().split()))

s3 = set(s_english.difference(s_french))

counter = 0

for i in s3:
    counter += 1
    
print(counter)  

#Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT


n_english = int(input())
s_english = set(map(int, input().split()))

b_french= int(input())
s_french = set(map(int, input().split()))

s3 = set(s_english.symmetric_difference(s_french))

counter = 0

for i in s3:
    counter += 1
    
print(counter) 

#Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT

n_a = int(input())
s_a = set(map(int, input().split()))
s_a
n = int(input())

for i in range(n):
    x1 = input().split()
    x2 = map(int,input().split())
    
    if x1[0] == 'intersection_update':
        s_a.intersection_update(x2)
    elif x1[0] == 'symmetric_difference_update':
        s_a.symmetric_difference_update(x2)
    elif x1[0] == 'difference_update':
        s_a.difference_update(x2)
    elif x1[0] == 'update':
        s_a.update(x2)
        
    x1 = ""
    x2 = []
    
    
print(sum(s_a))

#The Captain's Room 

# Enter your code here. Read input from STDIN. Print output to STDOUT

#def find_the_captain(n, l):
#    for i in l:
  #      if l.count(i) == 1:
   #         return i

n = int(input())
l = list(map(int, input().split()))

d = {i:0 for i in l} # I had runtime errors. In order to fix them i tried to convert the list in a set but it didn't work. so, i use the dictionary to delete the duplicates and go faster.

for i in l:
    d[i] += 1  
    
for j in d:
    if d[j] == 1:
        print(j) 

#Check Subset

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for i in range(t):
    n_a = int(input())
    a = list(map(int, input().split()))
    
    n_b = int(input())
    b = list(map(int, input().split()))
    
    counter = 0
    
    for i in a:
        if i in b:
            counter += 1
            
    if counter == n_a:
        print(True)
    else:
        print(False)

#Check Strict Superset

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = list(map(str, input().split()))
n = int(input())
counter = 0

for i in range(n):
    s = list(map(str, input().split()))
    
    if(all(i in a for i in s)):  # cool command i found here:  https://codeworld19.blogspot.com/2020/08/check-strict-superset-in-python-hacker.html
        counter += 1
        
if counter == n:
    print(True)
else:
    print(False)



### Collections

#collections.Counter()

# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

x = int(input())
store = collections.Counter(map(int, input().split()))
n = int(input())

money = 0

for i in range(n):
    shoe, price = map(int, input().split())

    if store[shoe] > 0:  # >0 means that there are still shoes in the shop. That value could be also negative...
        store[shoe] -= 1
        money += price
        
print(money)

#DefaultDict Tutorial

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

d = defaultdict(list)
n, m = map(int,input().split())

for i in range(n):
    a = input()
    d[a].append(str(1+i)) # why str? Because later we use the join function, that only works for string, not for integers.
    # But what are we doing here?
    # Since we can't have duplicate keys in a dictionary, we put in the
    # list the position where the a as been called. For more info:  https://thispointer.com/can-a-dictionary-have-duplicate-keys-in-python/#:~:text=The%20straight%20answer%20is%20NO,in%20a%20dictionary%20in%20Python.
    
        
for j in range(m):
    b = input()
    
    if len(d[b]) > 0:
        print(' '.join(d[b]))
    else:
        print(-1)  

#Collections.namedtuple()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
col = namedtuple('col', input())

tot_marks = 0

for i in range(n):
    a, b, c, d = map(str, input().split() )
    student = col(a, b, c, d)

    tot_marks += int(student.MARKS)
    
print(tot_marks/n)   

#Collections.OrderedDict()

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

d = {}

n = int(input())

for i in range(n):
    x = list(map(str, input().split()))
    net_price = x[-1]
    item_name = " ".join(x[:-1])
    
    if item_name not in d:
        d[item_name] = int(net_price)
    else:
        d[item_name] += int(net_price)
        
for food in d:
    print(food, d[food])

#Word Order

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

d = {}
n = int(input())

for i in range(n):
    x = list(map(str, input().split()))
    w = " ".join(x)
    
    if w not in d:
        d[w] = 1
    else:
        d[w] += 1
        
print(len(d))

el = ""

for word in d:
    el += str(d[word]) + " "
    
print(el)    

#Collections.deque()

from collections import deque
dq = deque()

for i in range(int(input())):
    command = list(map(str, input().split()))
    
    if command[0] == 'pop':
        dq.pop()
    elif command[0]  == 'popleft':
        dq.popleft()
    elif command[0] == 'append':
        dq.append(command[1])
    elif command[0] == 'appendleft':
        dq.appendleft(command[1])                  
        
x = ""

for i in dq:
    x += str(i) + " "

print(x)

#Company Logo

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':

    d = Counter(sorted([i for i in input()]))
    
    x = {k: v for k, v in sorted(d.items(), key=lambda x: x[1], reverse = True)} # sort
    
    counter = 0
    for k in x:
        print(k, x[k])
        counter +=1
        if counter == 3:
            break



### Date and Time

#Calendar Module

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

month, day, year = map(int, input().split())


print(days[calendar.weekday(year, month, day)])

#Time Delta

#!/bin/python3

import math
import os
import random
import re
import sys

# Websites I used to get the informations:
# 1)   https://docs.python.org/3/library/datetime.html
# 2)   https://www.adamsmith.haus/python/answers/how-to-find-the-number-of-seconds-between-two-datetime-objects-in-python
# 3)   https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime

# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

from datetime import datetime

# Complete the time_delta function below.

def time_delta(t1, t2):
    date1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    date2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    
    return str( abs(int((date1-date2).total_seconds() ))) 
    # NOTE: str in important! In fact, at line 39 we have delta + \n. If we dont put delta as a string it raises the following error: "TypeError: unsupported operand type(s) for +: 'int' and 'str'"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()





### Exceptions

#Exceptions

# Enter your code here. Read input from STDIN. Print output to STDOUT

# INTEGER DIVISION: a//b

n = int(input())

for i in range(n):
    a, b = [x for x in input().split()]
    
    try:
        print( int(a)//int(b) ) 
    except ValueError as v:
        print('Error Code:', v)
    except ZeroDivisionError as z:
        print('Error Code:', z)   



### Built-ins

#Zipped!

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, x = map(int, input().split())

l = []

for i in range(x):
    l.append(list(map(float, input().split())))
    
stud = list(zip(*l)) # you need to insert 'list' to view the zipped list

for i in stud:
    print(sum(i)/len(i))

#Athlete Sort

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key = lambda x: x[k])

    for i in arr:
        x = ""
        for j in i:
            x += str(j) + " "
        print(x)

#ginortS

# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()

low = ""
up = ""
num_ev = ""
num_odd = ""

for i in s:
    if i.islower():
        low += i
    elif i.isupper():
        up += i
    elif  (i.isdigit() and int(i)%2 == 0):
        num_ev += i
    elif  (i.isdigit() and int(i)%2 != 0):
        num_odd+= i

# print('Even: ', num_ev)
# print('Odd: ', num_odd)
        
a = sorted(low), sorted(up), sorted(num_odd), sorted(num_ev)       
b = ""

for i in a:
    for j in i:
        b += j
        
print(b)               



### Python Functionals

#Map and Lambda Function

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    
    if n == 1:
        return [0]
    elif n == 0:
        return []
    else:
        fib = [0, 1]    
        for i in range(n-2):
            fib.append(fib[-1]+fib[-2])
        
        return fib    





### Regex and Parsing challenges

#Detect Floating Point Number

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for i in range(t):
    x = input()
    if x == '0':
        print(False)
        break
    try:
        float(x)
        print(True)
    except ValueError:
        print(False)    

#Re.split()

# For info:   https://pynative.com/python-regex-split/

regex_pattern = r"\D"	# Do not delete 'r'.  --> \D is the command that corresponds to every non digit element

#Group(), Groups() & Groupdict()

# re.search():  https://www.guru99.com/python-regular-expressions-complete-tutorial.html
import re

s = input()
y = ""

for i in s:
    repetition = i*2
    if re.search(repetition, s) and i.isalnum():
        y += i
        break    
if y=="":
    print(-1)
else:          
    print(y)

#Re.findall() & Re.finditer()

# Enter your code here. Read input from STDIN. Print output to STDOUT

# To get to the solution I consulted these links:

# https://www.codexpedia.com/regex/regex-symbol-list-and-regex-examples/  :
# {n,}, Curly brackets with a number and a comma, matches minimum number of times the preceding character. For example, the below regex matches google, gooogle, gooooogle, goooooogle, ...

# https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet  :
# x(?=y) -- >Lookahead assertion: Matches "x" only if "x" is followed by "y"
# (?<=y)x -- >Lookbehind assertion: Matches "x" only if "x" is preceded by "y"

import re

s = input()
x = re.findall(r'(?<=[^AEIOUaeiou])[AEIOUaeiou]{2,}(?=[^AEIOUaeiou])', s)

if len(x) == 0:
    print(-1)
else:
    [print(i) for i in x]

#Re.start() & Re.end()

# Enter your code here. Read input from STDIN. Print output to STDOUTimport re

'''
import regex as re
s = input()
k = input()
l = []

x = re.findall(k,s, overlapped = True) 
br = len(x)

for i in range(len(s)):
    if len(l) == br:
        break
    else:
        m = re.search(k, s[i:])
        l.append( (m.start()+i, m.end()-1+i) )   
         
        
if len(l) == 0:
    print( (-1, -1))
else:
    for i in l:
        print(i)
'''


import re

s = input()
k = input()
k1 = re.compile(k)
l = []

if k not in s:
    print( (-1, -1) )

for i in range(len(s)-len(k)):
    m = re.search(k1, s[i:])
    if m:
        l.append( (m.start()+i, m.end()+i-1) )    
    
d = {k:0 for k in l}
for i in d.keys():
    print(i)

#Regex Substitution

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

'''
def change_symbols(s):
    new_s = s.replace("&&", "and" )
    new_s2 = new_s.replace('||', 'or')
    return new_s2
'''  # he wants a regex function inside...

def sub_symbol(s):
    if s.group(0) == '&&':
        return 'and'
    elif s.group(0) == '||':
        return 'or'
    
n = int(input())
for i in range(n):
    l = input()
    if l == "":
        print("")    
    else:    
        x = re.sub(r'(?<= )(&&|\|\|)(?= )', sub_symbol, l)
        print(x)

#Validating Roman Numerals

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# I had to watch here for the rules: https://www.cuemath.com/numbers/roman-numerals/
# (and I also asked for help to my colleagues)

# Remember: 1 <= number <= 3999

regex_pattern = r"([M]{0,3})(D?C{0,3}|C[MD])(L?X{0,3}|X[CL])(V?I{0,3}|I[XV])$"	# (thousands)(cent)(dec)(sing).
# If you don't put the $ it won't work! That's because if the number ends with IIII, the patter would get it as wright, because it has I{0, 3}, followed by another I. We need to tell it to stop the count after the 3rd I.

#Validating phone numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for i in range(n):
    phone = input()
    if re.search(r'[a-zA-Z]', phone):
        print('NO')
    elif re.search(r"^[789]", phone) and len(phone) == 10:
        print('YES')
    else:
        print('NO') 

#Validating and Parsing Email Addresses

# Enter your code here. Read input from STDIN. Print output to STDOUT

# [\w-] is the same as [A-Za-z0-9_-]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet

import re

n = int(input())

for i in range(n):
    name, mail = input().split()
    if re.match(r'<[a-zA-Z][A-Za-z0-9_.+-]+@[A-Za-z]+\.[A-Za-z]{1,3}>', mail):
        print(name, mail)

#Hex Color Code

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for i in range(n):
    hx = input()
    
    x = re.findall(r'(#[0-9a-fA-F]{3,6})(?=[,;\)])', hx)  # ?=[,;\)] menas: only if it's followed y a ,;)
    if x:
        print(*x, sep = '\n')   #* to extract from the []



#HTML Parser - Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Copy and paste from the example...

from html.parser import HTMLParser   # I had to ckeck online because it raise a ModuleNotFoundError


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attributes):
        print('Start', ':', tag) 
        for x in attributes:
            print('->', x[0], '>', x[1])
            
    def handle_endtag(self, tag):
        print('End   :', tag)
        
    def handle_startendtag(self, tag, attributes):
        print('Empty', ':', tag)
        for y in attributes:
            print('->', y[0], '>', y[1])
            
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

n = int(input())
l = []
for i in range(n):
    l.append(input())
    
parser.feed(''.join(l)) 

#HTML Parser - Part 2

# https://devpractical.com/make-singleline-and-multiline-comments-html/
#You can create a single line comment by putting <!-- at the start and --> at the end of your comment.

# https://www.tutorialspoint.com/html/html_comments.htm
# You can comment multiple lines by the special beginning tag <!-- and ending tag --> placed before the first line and end of the last line

# So we will use the \n symbol:

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:  # means that you're commenting multiple lines
            print('>>> Multi-line Comment', data, sep = '\n') 
        else:
            print('>>> Single-line Comment', data, sep = '\n')     
    def handle_data(self, data):
        if not '\n' in data:   # My colleagues told me this... i couldn't figure it out
            print('>>> Data', data, sep = '\n')   
        
# HackerRank gives us this block of code:
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Detect HTML Tags, Attributes and Attribute Values

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Note (from the text): Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->). Comments can be multiline.
# All attributes have an attribute value.

from html.parser import HTMLParser   # like tge previous exercises

n = int(input())
l = []

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attributes):
        print(tag)   # in the other exercises we had print('Start :', tag)
        for i in attributes:
            print('->', i[0], '>', i[1])  # x[1] is the value, x[0] the attribute
        
    # No comments
            
    def handle_startendtag(self, tag, attributes):
        print(tag)  # the same as line 12
        for j in attributes:
            print('->', j[0], '>', j[1])  # -> attribute > value
            
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

for i in range(n):
    parser.feed(input())

#Validating UID 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(input())

for i in range(t):
    uid = input()
    if (uid.isalnum()) and (len(set(uid)) == 10) and bool(re.search(r'(.*[A-Z]){2,}', uid)) and bool(re.search(r'(.*[0-9]){3,}', uid)):  # I use set to be sure there are no duplicates
        print('Valid')       
    else:            
        print('Invalid')  

#Validating Credit Card Numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for i in range(n):
    card = input()
    
    if len(card)>19:
        print('Invalid')
    else:    
        if re.match(r'^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})', card) and not re.search(r"([\d])(-?\1){3}", card):  # I had to ckeck online how not to repet a charachter n times
            print('Valid')
        else:
            print('Invalid')

#Validating Postal Codes

# IMPORTANT NOTE: A score of 0 will be awarded for using 'if' conditions.

regex_integer_in_range = r"^[1-9]([0-9]{5})$"	# exactly 6 charachters, starting from 100000 to 999999, can't start with with 0

# for matching the same text again, I used the commands ilustrated in this link:
# https://www.regular-expressions.info/backref.html

# regex_alternating_repetitive_digit_pair = r"1\d1|2\d2|3\d3|4\d4|5\d5|6\d6|7\d7|8\d8|9\d9|0\d0"     --> doesn't works with overlappings!
regex_alternating_repetitive_digit_pair = r'(\d)(?=(.){1}\1)'  # note \1 doesn't work with []

#Matrix Script

#!/bin/python3

# NOTE: A  score will be awarded for using 'if' conditions

import math
import os
import random
import re
import sys

###############################################
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
###############################################

# Step 1: We put all the elements in the columns togheter with the zip command, and then we insert in an empty string
phrase = ''
for charachter in zip(*matrix):  # it doesn't say I can't use for loops
    phrase += ''.join(charachter)
        
# Now phrase is something like:  This$#is% Matrix#  %!  
    
# Now I have to delete the non-alphanumeric elements... but not all of them! Only the ones that stands between 2 alphanumeric charachters. So the pattern will be:

pattern = r'(?<=[A-Za-z0-9])([^A-Za-z0-9]){1,}(?=[A-Za-z0-9])'

# that matches all the non-alphanum charachters between two alphanum elements.
# After the matching, we want it to be substituted by an empty space:
clean_phrase = re.sub(pattern, ' ', phrase)

# And then we print the cleaned phrase:
print(clean_phrase)



### XML

#XML 1 - Find the Score

# https://docs.python.org/3/library/xml.etree.elementtree.html
# https://python.readthedocs.io/en/v2.7.2/library/xml.etree.elementtree.html

 # Each element has a number of properties associated with it: [...] a number of attributes, stored in a Python dictionary.
 
 # We need the number of attributes of any element. We can use:
 # keys() --> "Returns the elements attribute names as a list"
 # iter() --> because 'node' is not iterable!

def get_attr_number(node):
    iterable_node = node.iter() # without iter() it will count less attributes
    score = 0
    for i in iterable_node:
        score += len(i.keys())
    return score

#XML2 - Find the Maximum Depth


# Since I have never heard about XML and depth, I searched some info online. It seems that the maximum depth is basically the max number od indentations. 
# Furthermore, every 'elem' has one or more child. If there is at leats 1 child, depth += 1

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # So, we start from the root (see the grey code at the bottom). It means that:
    if level == maxdepth:
        maxdepth += 1  # and this is clear
        
    # Now, since an 'elem' can have some children:
    for child in elem:
        depth(child, level+1)  # it seems this is a recursive function. I found some info here:  https://stackoverflow.com/questions/6507048/python-how-to-write-an-iterative-function



### Closures and Decorations

#Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        lis = []

        for i in l:
            if i[0]=='0' and len(i)>10:
                i = '+91' + " " + i[1:6] + " " + i[6:]
                lis.append(i)
            elif i[0] == '+' and len(i)>10:
                i = '+91' + " " + i[3:8] + " " + i[8:]
                lis.append(i)
            elif i[0] == '9' and len(i)>10:
                i = '+91' + " " + i[2:7] + " " + i[7:]
                lis.append(i)
            elif len(i) == 10:
                i = '+91' + " " +  i[:5] + " " + i[5:]
                lis.append(i)
                
        for i in sorted(lis):
            print(i)    
                       
    return fun

#Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        a =  map(f, sorted(people, key = lambda age: int(age[2])) )  # NOTE: I had to watch a tutorial to undesrtand what I was suppposed to do here...
        return a
        
    return inner



### Numpy

#Arrays

def arrays(arr):
    a = numpy.array(arr[::-1], float)
    return a

#Shape and Reshape

import numpy

a = numpy.array( list(map(int, input().split())) )

a.shape = (3, 3)
print(a)



#Transpose and Flatten

import numpy


n, m = map(int, input().split())
l = []

for i in range(n):
    l.append( list(map(int, input().split())) )
    
my_array = numpy.array(l)

print(numpy.transpose(my_array))
print (my_array.flatten())

#Concatenate

import numpy


n, m, p = map(int, input().split())
l1 = []
l2 = []

for i in range(n):
    l1.append( list(map(int, input().split())) )
    
for j in range(m):
    l2.append( list(map(int, input().split())) )
    
l1 = numpy.array(l1)
l2 = numpy.array(l2)

print (numpy.concatenate((l1, l2), axis = 0))



#Zeros and Ones

import numpy

x_y_z = tuple(map(int, input().split()))
if not input:
    input = 0

print(numpy.zeros((x_y_z), dtype = numpy.int))
print(numpy.ones((x_y_z), dtype = numpy.int))

#Eye and Identity

import numpy

n, m = map(int, input().split())

numpy.set_printoptions(legacy = '1.13')
print(numpy.eye(n, m))

#Array Mathematics

import numpy


n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append( list(map(int, input().split())) )

for i in range(n):  
    b.append( list(map(int, input().split())) )
   
a = numpy.array(a)
b = numpy.array(b)    
    
print(numpy.add(a, b))    
print(numpy.subtract(a, b))    
print(numpy.multiply(a, b))    
print(a//b)    
print(numpy.mod(a, b))
print(numpy.power(a, b))  

#Floor, Ceil and Rint

import numpy

numpy.set_printoptions(legacy = '1.13')
a = numpy.array(list(map(float, input().split())))


l1 = numpy.floor(a)
l2 = numpy.ceil(a)
l3 = numpy.rint(a)

print(l1)
print(l2)
print(l3)

#Sum and Prod

import numpy


n, m = map(int, input().split())
l = []

for i in range(n):
      l.append( list(map(int, input().split())) )
      
l = numpy.array(l)

l1 = numpy.sum(l, axis = 0)
print(numpy.prod(l1))

#Min and Max

import numpy

n, m = map(int, input().split())
l = []

for i in range(n):
    l.append( list(map(int, input().split())) )
    
l = numpy.array(l)    

print( max(numpy.min(l, axis = 1)) )

#Mean, Var, and Std

import numpy

n, m = map(int, input().split())
l = []

for i in range(n):
    l.append( list(map(int, input().split())) )
    
l = numpy.array(l)

print(numpy.mean(l, axis = 1))
print(numpy.var(l, axis = 0))
print(round(numpy.std(l), 11))

#Dot and Cross

import numpy

n = int(input())

a = []
b = []

for i in range(n):
    a.append( list(map(int, input().split())) )

for j in range(n):
    b.append( list(map(int, input().split())) )
    
a = numpy.array(a)
b = numpy.array(b)

print(numpy.dot(a, b))

#Inner and Outer

import numpy



a = numpy.array(list(map(int, input().split())))
b = numpy.array(list(map(int, input().split())))

print(numpy.inner(a, b))
print(numpy.outer(a, b))

#Polynomials

import numpy



coeff = numpy.array(list( (map(float, input().split())) ))
x = float(input())

print(numpy.polyval(coeff, x))

#Linear Algebra

import numpy

n = int(input())

a = []

for i in range(n):
    a.append( list(map(float, input().split())) )
    
a = numpy.array(a)
print(round(numpy.linalg.det(a),2)) 




##### PROBLEM 2 #####


# Challenge 1: Birthday Cake Candles

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    from collections import Counter
    
    a = Counter(candles)
    return a[max(a)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# Challenge 2: Number Line Jumps

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    k1 = []
    k2 = []
    
    if ((x2 > x1) and (v2 > v1)) or ((x1 > x2) and (v1 > v2)):  # see the explanation at the bottom of the text of the exercise: if one kangaroo starts haed and has a longer jump, the kangaroo that starts before him will never meet his friend
        return 'NO'
    
    for i in range(x1+v1, 19681908, v1):  # I put a very big range to be sure to capture all the possible options   
        k1.append(i)
    
    for j in range(x2+v2, 19681908, v2):
        k2.append(j)
      
    check = 0    
    for time in range(min(len(k1), len(k2))):  # not only the two kangaroos have to arrive at the same spot, but they have to arrive there at the same time. So we check how many times this happens. If check > 0 it means that there has been at least one moment where the two animals arrived at the same place starting from different positions
        if k1[time] == k2[time]:
            check += 1
            
    if check > 0:
        return 'YES'
    else:
        return 'NO'        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# Challenge 3: Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    cumulative = 0
    people = 5
    likes = math.floor(people/2)
    cumulative += likes
    
    for i in range(n-1):
        people = likes * 3
        likes = math.floor(people/2)
        cumulative += likes
        
    return cumulative   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Challenge 4: Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

# So here we need to do a recursive function. I found something on the internet:
# https://www.geeksforgeeks.org/recursion-in-python/

def superDigit(n, k):
    if len(n) == 1:
        return n  # our final result
    
    # But now we want len(n) == 1
        
    else:
        # p = n*k
        #l = 0
        #for number in p:
        #    l += int(number)  # can't do this because it raises 4 RunTimeErrors
        
        l = sum(list(map(int, n)))
        return superDigit(str(l*k), 1)
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()



# Challenge 5: Insertion Sort - Part 1

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    unsorted = arr[-1]


    for i in range(n-1, -1, -1):
        if arr[i] >= unsorted and arr[i-2] >= unsorted and i>1:
            arr[i] = arr[i-1]
            if arr[0] != arr[1]:
                print(*arr)  
        elif arr[i-2] < unsorted:
            arr[i] = arr[i-1]
            print(*arr)
            arr[i-1] = unsorted
            print(*arr)
            break
        elif i == 1:
            arr[i] = arr[i-1]
            print(*arr)
            arr[i-1] = unsorted
            print(*arr)


        
    #if arr[0] == arr[1]:
    #    arr[1] = unsorted
    #print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# Challenge 6: Insertion Sort - Part 2
def insertionSort2(n, arr):
    
    if arr[0] < arr[1]:
        print(*arr)
    else:
        arr[0], arr[1] = arr[1], arr[0]
    
    for i in range(1, n-1):
        if arr[i] <= arr[i+1] and arr[i] >= arr[i-1]:
            print(*arr)
        elif arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)

