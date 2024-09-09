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
print("------------------------------------------------------------------------")

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

    print("Task 1:-\n")

    print("key_value", key_value)
    
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

print("------------------------------------------------------------------------")

# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict
import numpy as np

dict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(dict)

keys = list(dict.keys())
values = list(dict.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print(sorted_dict)

print("------------------------------------------------------------------------")

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

print("------------------------------------------------------------------------")

#Decorative P2

def dec(func):
    def st(*args, **kwargs):
        print("$"*5)
        res=func(*args, **kwargs)
        print(f"Welcome {res}")
        print("$"*5)
    return st

@dec    
def printssss(x):
    return x

x=input("Enter the name: ")
printssss(x)

print("------------------------------------------------------------------------")

#Collections
from collections import Counter
l=['A','B','A','C','D']
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

#re-inserting the element
od['a']=9

#printing the updated values
for key, value in od.items(): 
    print(key, value)

print("------------------------------------------------------------------------")
# Python program to demonstrate 
# ChainMap dictionaries all in one 
   
   
from collections import ChainMap,Counter
   
   
d1 = {'a': 1, 'b': 2}



# Defining the chainmap
l=Counter(l)
c = ChainMap(d1) 

print(type(c))
print("Before Adding:\n",c)

c=c.new_child(l)
print("After adding:\n",c)

print("------------------------------------------------------------------------")

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

print("------------------------------------------------------------------------")

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
      
l1=[3, 4, 5, 20, 5, 25, 1, 3]
l1.pop(1)
print(l1)
