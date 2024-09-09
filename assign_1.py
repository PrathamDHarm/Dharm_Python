#Write a program using while loop to print even numbers in range of 1 to 25.
i=1
print("Using WHILE LOOP")
while i<25:
    if i%2==0:
        print(i)
    i+=1
print("Using FOR LOOP")
for i in range (1,25):
    if i % 2 ==0:
        print(i)

#Using WHILE LOOP
#2
#4
#6
#8
#10
#12
#14
#16
#18
#20
#22
#24
#Using FOR LOOP
#2
#4
#6
#8
#10
#12
#14
#16
#18
#20
#22
#24
print("---------------------------")

#Write the same using FOR loop.
print("Factorial of a Number (User Input): ")
number = int(input("Enter the number : "))
z=1
for i in range (2, number+1):
    z*=i
print(z,"\n")

#Factorial of a Number (User Input): 
#Enter the number : 5
#120
print("---------------------------")


#4.	Write a function sum_of_squares that computes the sum of the squares
#Example, sum_of_squares(987) should return 194, since9**2 + 8**2 + 7**2 == 81 +   64 + 49 == 194
#Sample 
#sum_of_squares(1)
#1
#sum_of_squares(9)	
#81
#sum_of_squares(11)
#2
#sum_of_squares(121)
#6

print("Sum of Squares")
a=int(input("Enter the number: "))
digits=[int(d) for d in str(a)]
sum_of_squares= sum(d**2 for d in digits)
print(sum_of_squares)
#Sum of Squares
#Enter the number: 121
#6



print("---------------------------")
print("\n")


#5.	Write a Python program to get the Fibonacci series between 0 to 50.
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34

print("Fibonacci Series")
a,b=0,1
while a<=50:
    print(a,end=" ")
    a,b=b,a+b
#Fibonacci Series
#0 1 1 2 3 5 8 13 21 34 
print("\n")
print("---------------------------")


#Using 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1 
#Sample input 
#   s1 = "Samy"
#   s2 = "Kelly"
#Sample output 
#   SaKellymy
print("String Operations")
s1="Samy"
s2="kelly"
print(s1+s2)
#String Operations
#Samykelly


print("---------------------------")


#Accept a long string from user and return each word in reverse way 
#Sample input     
#      My name is Sam I live in Mumbai 
#Sample output 
#      Mumbai in live I Sam is name My 

print("print the sentence in reverse")
a="My name is Sam I live in Mumbai"
l=a.split()
l.reverse()
print(' '.join(l))
#print the sentence in reverse
#Mumbai in live I Sam is name My


print("---------------------------")

#Accept a string from user and print the word with is occurring maximum time. 
#Sample input 
#      My name is Sam.  Sam lives in Mumbai. Sam plays cricket. 
#Sample output 
#      Sam is occurring 3 times 

print("Find duplicates in the sentence")
a="My name is Sam. Sam lives in Mumbai. Sam plays cricket."
words=a.replace('.', '').split()

word_count={}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

d={word: count for word, count in word_count.items() if count>1}

for word,count in d.items():
    print(f"'{word}' occurs {count} times")

#Find duplicates in the sentence
#'Sam' occurs 3 times

    
print("---------------------------")


#Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
my_list=[1,2,3,4,5,20]
for i,value in enumerate(my_list):
    if value ==20:
        my_list[i] =200
        break
print(my_list)

#[1, 2, 3, 4, 5, 200]


print("---------------------------")


#Sort a tuple of tuples by 2nd item 
#Sample input 
#tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d',29))
#Sample output 	
#(('c', 11), ('a', 23), ('d', 29), ('b', 37))

tuple1=(('a',23),('b',37),('c',11),('d',29))
print(sorted(tuple1, key=lambda x: x[1]))

#[('c', 11), ('a', 23), ('d', 29), ('b', 37)]


print("---------------------------")


#3.	Create below 2 sets and try intersection, union, difference, symmetric_difference() 
#Sample input 
#      set1 = {10, 20, 30, 40, 50}
#      set2 = {60, 70, 80, 90, 10}

set1={10,20,30,40,50}
set2={60,70,80,90,10}

print("Inersection: ",set1 & set2)
print("union: ", set1 | set2)
print("Difference set1 in set2: ",set1-set2)
print("Difference set2 in set1: ",set2-set1)
print("Symettric-Difference: ", set1^set2)

#Output:-
#Inersection:  {10}
#union:  {70, 40, 10, 80, 50, 20, 90, 60, 30}
#Difference set1 in set2:  {40, 50, 20, 30}
#Difference set2 in set1:  {80, 90, 60, 70}
#Symettric-Difference:  {70, 80, 20, 90, 30, 40, 50, 60}


print("---------------------------")


#Using input() function accepts 3 numbers from user and print the biggest number. 
i=0
l=[]
while i<=2:
    a=int(input("Enter the number: "))
    l.append(a)
    i+=1
print("Largest Number: ",max(l))
#Enter the number: 12
#Enter the number: 33
#Enter the number: 44
#Largest Number:  44


print("---------------------------")


#Store the below words and each variable and print it
# Sample input     
# All work and no play make Jack a dull boy. 

a="All work and no play make Jack a dull boy."
words=a.split()
for word in words:
    print(word)

#Output:-
#All
#work
#and
#no
#play
#make
#Jack
#a
#dull
#boy.


print("---------------------------")


#Accept and long string from user and find the number of vowels in that string.
a=input("Enter the sentence: \n")
a.lower()
count=0
vowels="aeiou"
for char in a:
    if char in vowels:
        count+=1
    else:
        count=0
print(count)

#Output:-
#Enter the sentence: 
#aei
#3

print("---------------------------")

#Input 2 numbers from user and an operator from user   + , - ,* , / based on operator do the operation 
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
print("Choose (+ or - or * or %)")
c=input("Enter the Operator: ")

if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print( a/b)
elif c == "%":
    print( a%b)
else:
    print("Invalid Operator")
    
#Output:- 
#Enter the number: 12
#Enter the number: 22
#Choose (+ or - or * or %)
#Enter the Operator: -
#-1

    
print("---------------------------")


#Accept a number from  store it in variable  name as  age
#If the age greater then 18 and equal to 60 then print Person can vote
#If the age is less than 18 and greater than 0 print Person cannot vote 
#Else print invalid age. 

a=int(input("Enter age: \n"))
if a>18 and a<=60:
    print("Elgigble to vote")
elif a>0 and a<18:
    print("Not eligible to vote")
else:
    print("Invalid Input")

#Output:- 
#Enter age: 
#22
#Elgigble to vote

    
print("---------------------------")


#Accept a character from user and check whether is vowel or not. 
a=input("Enter a character: \n")
a.lower()
vowels="aeiou"
if char in vowels:
    print("It is vowel")
else:
    print("it is not a vowel")

#Output:-
#Enter a character: 
#D
#it is not a vowel


print("---------------------------")


#Accept username and   password as string from user. If the username==” Admin” and password==”123” then print Welcome Admin else print invalid username or password.
user=input("User Name: ")
password=input("Password: ")
if user=="Admin" and password=="123":
    print("Welcome Admin")
else:
    print("Invalid username or password")

#Output:-
#User Name: Dharmendra/Admin
#Password: 111/123
#Invalid username or password / Welcome Admin

    
print("---------------------------")


#Write a function called `find_max` that takes a list of numbers as an argument and returns the maximum number in the list.
def exam_score():
    scores=[85,92,78,95,88,76,95,89,91,82]
    print(sum(scores)/len(scores))
    print(max(scores))
    print(min(scores))
    count=0
    mean=sum(scores)/len(scores)
    for i in scores:
        if i<mean:
            count+=1
        
    print(f"Below Aveg({mean}) Score: {count}")

exam_score()
#Output
#87.1
#95
#76
#Below Aveg(87.1) Score: 4


print("---------------------------")


#Write a function called 'greet_user" that takes a user's name as an argument and returns a greeting and returns a greeting message in the form of "hello, [name]!"
def greet_user(user):
    print(f"Hello,{user}!")

user=input("Enter Name: ")
greet_user(user)
#Enter Name: Sai
#Hello,Sai!


print("---------------------------")


#Write a function called `is_even` that takes an integer as an argument and returns `True` if the number is even and `False` if the number is odd.
def is_even (a):
    if a%2==0:
        print("True")
    else:
        print( "False")
a=int(input("Enter a number: "))
is_even(a)
#Enter a number: 12
#True


print("---------------------------")


#Write a function called `fibonacci` that takes an integer `n` as an argument and returns the `n`-th Fibonacci number. Use recursion for this exercise.
def fibonacci(n):
    if n<=0:
        return "Input should be a positive integer"
    elif n ==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=10
print("Fibonacci series up to",n,"terms")
for i in range (1,n+1):
    print(fibonacci(i))
#Fibonacci series up to 10 terms
#0
#1
#1
#2
#3
#5
#8
#13
#21
#34

    
print("---------------------------")


#Write a function called `is_palindrome` that takes a string as an argument and returns `True` if the string is a palindrome and `False` otherwise.
def is_palindrome(s):
    rev="".join(c for c in s if c.isalnum())
    return rev == rev[::-1]

string = "121"
if is_palindrome(string):
    print( "True")
else:
   print("false")

#True


print("---------------------------")


#Create an empty dictionary and do following operation on it 
#   Add 5 key and values in it 
#   Accept a key from user and remove that key and values from dictionary 
#   Accept a key from user and print the value of that key 
#   Accept all key and values from the dictionary  

print("Dictionary ")

lib={}

def switch(x):
    if x==1:
        id=int(input("Enter the id of the book: "))
        if id in lib:
                print(id, "Already Existed")
        else:
            title=input("Title: ")
            author=input("Author: ")
            year=int(input("Publication Year: "))
            lib[id]=[title,author,year]
            print("Added Successfully")
    elif x==2:
        id=int(input("Enter the id of the book: "))
        if id in lib:
            del lib[id]
            print(id, "Deleted Successfully")
        else:
            print("Already Deleted")
    elif x==3:
        id=int(input("Enter the id of the book: "))
        print(lib[id])
    elif x==4:
        print(lib)
    else:
        exit()

while True:
    print("1.Add")
    print("2. Remove")
    print("3. Search")
    print("4. Display")
    print("5. Exit")
    x=int(input("Choose the option: "))
    switch(x)


#Dictionary 
#1.Add
#2. Remove
#3. Search
#4. Display
#5. Exit
#Choose the option: 1
#Enter the id of the book: 12
#Title: MockingBird
#Author: Harper
#Publication Year: 1960
#Added Successfully
31.Add
#2. Remove
#3. Search
#4. Display
#5. Exit
#Choose the option: 2
#Enter the id of the book: 12
#12 Deleted Successfully
#1.Add
#2. Remove
#3. Search
#4. Display
#5. Exit
#Choose the option: 4
#{}
#1.Add
#2. Remove
#3. Search
#4. Display
#5. Exit
#Choose the option:

print("----------------------File Operation task--------------------------------")
#1.	Write all file content into new file by skipping  line 5  from following file
file=open(r"C:\Users\d.hanumansetty\OneDrive - Accenture\Desktop\Python Training\test.txt",'w')
for i in range (1,8):
    file.write(f"line {i}\n")
file=open(r"C:\Users\d.hanumansetty\OneDrive - Accenture\Desktop\Python Training\test.txt",'r+')
dest_file=open(r"C:\Users\d.hanumansetty\OneDrive - Accenture\Desktop\Python Training\newFile.txt",'w+')
print("test file Data: ",file.read())
file.seek(0)
for i,line in enumerate(file):
    if i!=4:
        dest_file.write(line)
dest_file=open(r"C:\Users\d.hanumansetty\OneDrive - Accenture\Desktop\Python Training\newFile.txt",'r')
print("NewFile Data: ",dest_file.read())
file.close()

#Output:-
# line 1
#line 2
#line 3
#line 4
#line 5
#line 6
#line 7

#NewFile Data: 
# line 1
#line 2
#line 3
#line 4
#line 6
#line 7



#Accept a file name from user and print the file contain from last line to first line 
file=open(r"C:\Users\d.hanumansetty\OneDrive - Accenture\Desktop\Python Training\test.txt",'r')
print(file.read())

#Output:-
#line 1
#line 2
#line 3
#line 4
#line 5
#line 6
#line 7


#Accept data from user till the user enter ‘stop’. Write all data in CSV with each data on new line 
#Sample input 
#ID     Name    Age 
#110   Sam      22
#111   Paul      33
#102   Max       44

employee = {}

def add():
    empId = int(input("Employee ID: "))
    if empId in employee:
        print("Already Existing")
    else:
        employee[empId] = {
            "EmpName": input("Employee Name: "),
            "EmpAge": int(input("Employee Age: ")),
            "EmpSal": float(input("Employee Salary: "))
        }

def display():
    if not employee:
        print("No employees to display.")
    else:
        for empId, details in employee.items():
            print(f"ID: {empId}, Name: {details['EmpName']}, Age: {details['EmpAge']}, Salary: {details['EmpSal']}")

def search():
    empId = int(input("Employee ID: "))
    if empId in employee:
        details = employee[empId]
        print(f"ID: {empId}, Name: {details['EmpName']}, Age: {details['EmpAge']}, Salary: {details['EmpSal']}")
    else:
        print("Employee not found")

def update():
    empId = int(input("Employee ID: "))
    if empId in employee:
        employee[empId]['EmpSal'] = float(input("Updated Employee Salary: "))
        print("Updated successfully")
    else:
        print("Employee not found")

while True:
    print("1. Add")
    print("2. Search")
    print("3. Display")
    print("4. Update")
    print("5. Exit")
    
    try:
        x = int(input("Choose Option: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if x == 1:
        add()
    elif x == 2:
        search()
    elif x == 3:
        display()
    elif x == 4:
        update()
    elif x == 5:
        break
    else:
        print("Invalid choice. Please select a valid option.")



#Write program to read  the contain of json file 
import pandas as pd

ds=pd.read_json(r"C:\Users\d.hanumansetty\OneDrive - Accenture\Documents\hi.json")
print(ds)


#Create  a table in database as student which has studentid , studentname and studentage as coloumns 
import pandas as pd

df=pd.DataFrame({"StudentId":[101,102,103],"StudentName":["Ram",'Sam','Dam'],"StudentAge":[20,18,19]})
print(df)


#Accept values from user and insert 5 record in student table.
#Print all the data from student table 
import pandas as pd
i=0
d=[]
while i<5:
    id=int(input("student Id:"))
    name=input("Name: ")
    age=int(input("Age: "))
    d.append({'StudentId':id,'Studentname':name,'StudentAge':age})
    df=pd.DataFrame(d)
    i+=1
print(df)



#Accept values from user and insert 5 record in student table.
#Print all the data from student table 
import sqlite3

con=sqlite3.connect(r"C:\Users\d.hanumansetty\OneDrive - Accenture\Desktop\python\demo2.db")
cur=con.cursor()

cur.execute("create table stud(id int primary key,name text,age int)")
con.commit()

cur.execute("insert into stud values(101,'Sai',18)")
cur.execute("insert into stud values(102,'Dharm',17)")
cur.execute("insert into stud values(103,'Govind',18)")
cur.execute("insert into stud values(104,'Prathamesh',20)")
cur.execute("insert into stud values(105,'Ajay',20)")
con.commit()
cur.execute('select * from stud')
cur.fetchall()
 
