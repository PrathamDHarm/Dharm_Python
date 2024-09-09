import numpy as np

print("------------------------------------------------")

# Define two 3x3 matrices a and b
a = np.array([[1, 33, 3], [3, 4, 5], [44, 55, 6]], dtype='float')
b = np.array([[22, 33, 44], [11, 55, 66], [77, 88, 99]])

print("Matrix a:\n", a)
print("Matrix b:\n", b)

# Perform matrix multiplication between a and b
print("\nM[a] * M[b]:")
result = a @ b
print(result)  # Prints the resulting matrix after multiplication

# Sum of all elements in array 'a'
print("\nSum of arrays: ", a.sum())

# Data type of array 'a'
print("Data Type: ",a.dtype)

# Print all rows of array 'a'
print(a[[0, 1, 2]])

# Multiplying each element of 'a' by 4
print("\nMultiplying each element with 4: \n", a * 4)

# Maximum elements along each axis
print("Max Elemnt of each row of M[a]:",a.max(axis=1))

print(np.reshape(2,4,4))
 
print("------------------------------------------------")

# Display the matrix a before and after transposing
print("Before Transpose: \n")
print(a)  # Original matrix a

print("\nAfter Transpose: \n")
print(a.T)  # Transposed matrix a

print("------------------------------------------------")

# Define matrix c with fractional values and perform element-wise sine operation
c = np.array([[1/2, 2/5, 3/1], [3/2.2, 4/3.3, 5/3.0], [4/1.8, 5/2.2, 6/6.79]])
z = np.sin(c)
print(z)  # Prints the sine of each element in matrix c

print("------------------------------------------------")

# Get the indices that would sort each row of the matrix z
sorted_indices = np.argsort(z)
print(sorted_indices)  # Prints the indices that sort each row of z

print("------------------------------------------------")

# Define a 3x3 matrix with different data types and specify a string data type
d = np.array([[1, 2, 3], ['a', 'b', 'c'], [12, 33, 44]], dtype='S')
print(d.dtype)  # Prints the data type of the array d

print("------------------------------------------------")

# Create a view and a copy of the matrix e
e = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
f = e.view()  # Creates a view of the array e
g = e.copy()  # Creates a copy of the array e

# Modify the first row of the original matrix e
e[0] = 44

# Print the base attribute of the view and the copy
print(f.base)  # Prints the base object that the view f is looking at
print(g.base)  # Prints the base object that the copy g is looking at

# Print the view f
print(f)  # Prints the contents of the view f

print("------------------------------------------------")

# Define a 1D array h and reshape it into a 3D array
h = np.array([1, 2, 3, 3, 4, 5, 6, 5, 6, 6, 4, 22])
i = h.reshape(2, 3, 2)
print(i)  # Prints the reshaped 3D array h

print("------------------------------------------------")

# Concatenate arrays e and f along axis 1
print(np.concatenate((e, f), axis=1))

print("------------------------------------------------")

# Stack arrays a and b along axis 1
a = np.array([1, 2, 3])
b = np.array([33, 44, 55])
print(np.stack((a, b), axis=1))

print("------------------------------------------------")

# Split the stacked array into 2 parts
w = np.array_split(np.stack((a, b), axis=1), 2)
print(w)       # Prints the list of split arrays
print(w[0])    # Prints the first split array

print("------------------------------------------------")

# Define a 2D array and split it horizontally into 3 parts
a = np.array([[1, 2, 3], [33, 44, 55]])
result = np.hsplit(a, 3)
print(result[0])  # Prints the first part of the horizontally split array

print("------------------------------------------------")

# Create a 1D array
a = np.array([1, 2, 5, 4, 3, 6, 8, 7])

# Apply a condition to find indices of even values
result = np.where(a % 2 == 0)
print(result)  # Prints the indices of even values

print("------------------------------------------------")

# Create a 1D array and search for the index where a value would be inserted to maintain order
a = np.array([1, 2, 5, 4, 3, 6, 7, 8])
print(np.searchsorted(a, 3, side='right'))  # Finds index where 3 would be inserted to maintain order
