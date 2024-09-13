import time

#dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
#dict2 = dict1.copy()
#print(dict2)
#dict1.clear()
#print(dict1)
#print(dict2.get(1))
#print(dict2.items())
#print(dict2.keys())

#dict2.pop(4)
#print(dict2)
#dict2.popitem()
#print(dict2)
#dict2.update({3: "Scala"})
#print(dict2)
#print(dict2.values())

myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

# Sort the dictionary items by values in descending order
sorted_items = sorted(myDict.items(), key=lambda item: item[1], reverse=False)

# Print the keys in the order of sorted values
for key, value in sorted_items:
    print(key, value)

time.sleep(3)
print("-------------------Functions in Python-----------------------------------")


# Function calling
def dictionary():
    # Declare hash function
    key_value = {}

# Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323


    print("Input Order of key_value", key_value)
    print("Sorted By Values: \n")
    
    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for i,j in sorted(key_value.items(),key=lambda item: item[1]):
        print(i,j, end="\n")


def main():
    # function calling
    dictionary()


# Main function calling
if __name__ == "__main__":
    main()

time.sleep(3)
print("-------------------------Sorted Dictionary In Python--------------------")


# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict
import numpy as np

dict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
print("Original Dictionary: \n",dict)

keys = list(dict.keys())
values = list(dict.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print("After Sorted: \n",sorted_dict)
time.sleep(3)
print("-----------------------------Decorative In Python------------------------")

#Decorative P1
def stars(func):
    def st():
        print("*" * 10)
        result = func()  # Call the function and store the result
        print("Sum:", result)  # Print the sum after the first set of stars
        print("*" * 10)
        return result  # Return the result of the original function
    return st  # Return the function itself, not the result of calling it

@stars  # Decorate the adding function with stars
def adding(a=2, b=2):
    return a + b  # Return the sum

adding()  # Call the decorated function
time.sleep(3)
print("-----------------------------Decorative In Python------------------------")


#Decorative P2

def dec(func):
    def st(*args):
        print("$"*5)
        res=func(*args)
        print(f"Welcome {res}")
        print("$"*5)
    return st

@dec    
def printssss(x):
    return x

x=input("Enter the name: ")
printssss(x)
time.sleep(3)
print("--------------------------OrderedDict() in Python------------------------")


#Collections
from collections import Counter
l=['A','B','A','C','D','F','E','E']
print(Counter(l))

# A Python program to demonstrate working
# of OrderedDict 

from collections import OrderedDict 
  
print("This is a Dict:\n") 
d = {} 
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
  
for key, value in d.items(): 
    print(key, value) 
  
print("\nThis is an Ordered Dict:\n") 
od = OrderedDict() 
od['a'] = 1
od['c'] = 3
od['b'] = 2
od['d'] = 4

#deleting the specified element
od.pop('a')
print("a=1 is been deleted")

#re-inserting the element
od['a']=9
print("a=9 is inserted")

#printing the updated values
for key, value in od.items(): 
    print(key, value)
time.sleep(3)
print("--------------------ChainMap dictionaries in Python----------------------")
# Python program to demonstrate 
# ChainMap dictionaries all in one 
   
   
from collections import ChainMap,Counter   
d1 = ['a', 'b','b']
d1=Counter(d1)



# Defining the chainmap
l=Counter(l)
c = ChainMap(d1) 

print(type(c))
print("Before Adding:\n",c)

c=c.new_child(l)
print("After adding:\n",c)
time.sleep(3)

print("------------------------namedtuple() in Python--------------------------")

# Python code to demonstrate namedtuple()
  
from collections import namedtuple
  
# Declaring namedtuple() 
Student = namedtuple('Student',['name','age','DOB']) 
  
# Adding values 
S = Student('Nandini','19','2541997') 

print(S)
print("DATA TYPE: ",type(S))
# Access using index 
print ("The Student age using index is : ",end="") 
print (S.age) 
  
# Access using name  
print ("The Student name using keyname is : ",end ="") 
print (S.name)
time.sleep(3)
print("-------------------Append (Left or Default) in Python-------------------")

from collections import deque

# Initial list operations
l = ['A', 'B', 'A', 'C', 'D']
l.append("C")  # Append "C" to the end of the list
print("Default append() (right): ", l)  # Output: ['A', 'B', 'A', 'C', 'D', 'C']

# Convert the list to a deque
l = deque(l)
l.appendleft(22)  # Add 22 to the front of the deque
print("Using appendleft(): ", l)  # Output: deque([22, 'A', 'B', 'A', 'C', 'D', 'C'])

# Deleting elements from deque
print("To delete")
l.popleft()  # Remove and return the front element (22)
l.pop()  # Remove and return the end element ('C')

# The deque is now: deque(['A', 'B', 'A', 'C', 'D'])
print(l)
time.sleep(3)
print("------------------------------------------------------------------------")

print("-----------------------Exceptions in Python-----------------------------")

while True:
    x=int(input("Please enter the number: "))
    y=int(input("Please enter the number: "))
    try:
        print(x/y)
        break
    except ArithmeticError:
        print("Invalid Input. Input should be integer")

time.sleep(3)
print("----------------------Inheritance in Python-----------------------------")

class Parent:
    def __init__(self,pname,pid):
        self.pname=pname
        self.pid=pid
    def prints(self):
        print(self.pname,self.pid)

class Child(Parent):
    def __init__(self,cname,cid,year):
        #Parent.__init__(self,cname,cid)
        super().__init__(cname,cid)
        self.year=year
    def welcome(self):
          print("Welcome", self.pname, self.pid, "to the class of", self.year)

x=Child("Sai",22,2022)
x.prints()
print(x.year)
x.welcome()
    

myTuple=("apple","banana","orange")

myit=iter(myTuple)

for i in myTuple:
    print(i)

#for i in range (len(myTuple)):
#    print(myTuple[i])

time.sleep(3)
print("----------------------Polymorphism in Python-----------------------------")

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

time.sleep(3)    
print("----------------------Password Tkinter in Python---------------------")

import tkinter as tk
import random
import string

# Initialize the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")

# Create the first scale (0 to 100)
scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale.pack()

# Function to get the current value of the first slider and generate a random string
def get_value():
    # Get the value from the first scale (0 to 100)
    x = scale.get()
    print(f"Slider value: {x}")
    
    result = ""  # Initialize an empty string to store the final result
    
    
    for i in range(3):  # Generate 3 random letter-number pairs
        y = random.randint(0, x)  # Generate a random number between 0 and x
        randomLetter = random.choice(string.ascii_letters)  # Generate a random letter
        s = randomLetter + str(y)  # Combine the letter and number into a string
        result += s  # Accumulate the result
    
    print(f"S: {result}")  # Print the final result string
    return result[:5]

# Function to update the label with the generated string
def update_label():
    result = get_value()
    label1.config(text=result)

# Create a button to print the current value, random number, and selected character
button = tk.Button(root,text="Get Value", command=update_label)
button.pack()

# Create a label to display the generated string
label1 = tk.Label(root, text="Generated String: ")
label1.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

time.sleep(3)
print("----------------------Data Types in Python---------------------")

#Complex Data Type
x=complex(3,4)
print(x)

#Set Data Type
x={2,344,3,3}
print(x)
print(b"hello")

#encode
txt = "Hi I'm Dharmendra"

x = txt.encode()

print(x)

x=[2,344,3,3]
print(x.count(3))
y=[23,34234,343]

print(x)

x.append(y)
print("Using append ",x)
x=[2,344,3,3]
x.extend(y)
print("Using extend ",x)
      
l2=[3, 4, 5, 20, 5, 25, 1, 3]
l2.pop(1)
print(l2)
print(type(l2))

time.sleep(3)
print("----------------------Merge in Python---------------------")

from collections import defaultdict

l1=[1,2,3,4]
l2=[34,3434,55,324]
x=zip(l1,l2)
y=defaultdict(list)

for i,j in (x):
    y[i].append(j)
print(y)
time.sleep(3)
print("----------------------Minimum in Python---------------------")

temp=min(y.values())
res=[key for key in y if y[key] == temp]
print(f"Key of the min value from the dict is {res}")

print("-----------------------------------------------------------")

if __name__ == '__main__':
    arr = []  # Initialize an empty list

    # Perform the operations as given in the input
    arr.insert(0, 5)  # Insert 5 at index 0
    arr.insert(1, 10)  # Insert 10 at index 1
    arr.insert(0, 6)  # Insert 6 at index 0

    print(arr)  # Print the list after insertions

    arr.remove(6)  # Remove the first occurrence of 6
    arr.append(9)  # Append 9 to the end of the list
    arr.append(1)  # Append 1 to the end of the list

    arr.sort()  # Sort the list
    print(arr)  # Print the list after sorting

    arr.pop()  # Remove the last element
    arr.reverse()  # Reverse the list

    print(arr)  # Print the list after reversing


print("-------------------------swapcase() in Python------------------")

def swap_case(x):
    swapcase_x = x.swapcase()
    return swapcase_x
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

print("-------------------------count string in Python------------------")
def count_substring(string, sub_string):
    count = start = 0
    while True:
        start = string.find(sub_string, start)
        if start == -1:
            break
        count += 1
        start += 1  # Move past the current match to find overlapping matches
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

print("-------------------------Split & Join in Python------------------")
def split_and_join(line):
    # write your code here
    words=line.split(" ")
    x="-".join(words)
    return x

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

print("--------------------String Validations in Python------------------")

if __name__ == '__main__':
    s = input()
    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.islower())
    print(s.isupper())

print("--------------------Nested List in Python------------------")

if __name__ == '__main__':
    scores = {}
    
    # Collecting input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores[name] = score  # Store the score as a float value, not a set
    
    # Sort the dictionary by the scores (values)
    sorted_scores = sorted(scores.items(), key=lambda item: item[1])
    
    # Find the second lowest score
    lowest_score = sorted_scores[0][1]
    
    # Finding the second lowest score
    second_lowest_score = None
    for name, score in sorted_scores:
        if score > lowest_score:
            second_lowest_score = score
            break
    
    # Collect all students with the second lowest score and sort them alphabetically
    students_with_second_lowest_score = sorted([name for name, score in sorted_scores if score == second_lowest_score])
    
    # Print the students with the second lowest score
    for student in students_with_second_lowest_score:
        print(student)
#Input

#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39


print("--------------------String Mutations in Python------------------")

def mutate_string(string, position, character):
    x=string[:position]+character+string[position+1:]
    return x

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#Input:
#abracadabra
#5 k

print("--------------------Capitalize in Python------------------")

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join([word.capitalize() for word in s.split(' ')])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#hello world
