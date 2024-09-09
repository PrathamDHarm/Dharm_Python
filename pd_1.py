import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import re
import tkinter as tk




#file2=pd.read_csv(r"C:\Users\d.hanumansetty\Downloads\student_1.csv")
#print(file2)

#print(file2.isnull().sum())
#ss=file2.dropna()
#print(ss.isnull().sum())

#Plotting
#x=ss['class']
#y=ss['mark']
#plt.bar(x,y)
#plt.show()

#exception handler
try:
    print(2/0)
except Exception as ex:
    print(ex)

#regular expression
st2="This is python Prog"
x=re.findall('p',st2)
y=re.findall("[a-z]",st2)
print(x)
print(y)
if(x==['p']):
    print("found")

#zip()
x=['c','java','arduino']
y=[110,111,112]
print(list(zip(x,y)))


import tkinter as tk

def button_clicked():
    d = entry.get()  # Retrieve the text entered by the user in the Entry widget.
    textt.config(text=f"Entered: {d}")  # Update the first label to show "Entered: [user input]".
    print("Button Clicked")  # Print "Button Clicked" to the console (for debugging purposes).
    result_label.config(text=d)  # Update the second label to display the user's input.

# Initialize the main Tkinter window.
win = tk.Tk()
win.geometry("300x300")  # Set the window size to 300x300 pixels.

# Create a label to instruct the user to enter text.
textt = tk.Label(win, text="Enter: ")
textt.pack()  # Add the label to the window.

# Create an Entry widget where the user can input text.
entry = tk.Entry(win)
entry.pack()  # Add the entry widget to the window.

# Create a button that, when clicked, calls the button_clicked() function.
b1 = tk.Button(win, text='Result', background="red", foreground="black", width=25, height=5, command=button_clicked)
b1.pack()  # Add the button to the window.

# Create a label to display the user's input after the button is clicked.
result_label = tk.Label(win, text=textt)
result_label.pack(pady=10)  # Add the label to the window with some padding at the top.

# Start the Tkinter event loop, keeping the window open and interactive.
win.mainloop()

