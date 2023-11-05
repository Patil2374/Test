import time
# Data Types in Python
#Intiger DT
A = 10
print(A)
print(type(A))

#Float DT
B = 123.45
print(B)
print(type(B))

#Boolean Data type
a = 100
b = 200
x = a==b
print(x)
print(type(x))
x = a!=b
print(x)
print(type(x))


#string Data Type
a = "string"
print(a)
print(type(a))

#complex data type
a = 100+200j
print(a)
print(type(a))

#List data type
L=[101,'anuj',1.11]
print(L)
print(type(L))

#Input Function
a = input("Enter the data :")
print(type(a))
print()

#eval Function
a = eval(input("Enter Data: "))
print(type(a))
print()

#Typecasting
z = 10
print(type(z))
print()
z = float(z)
print(type(z))
print()

#slicing operator
S = "Python Learning"
print("Reversing the string",S[::-1])
print()
print("string is:",S[0:])
print()

#immutable 
str1 = "Core Python"
print(str1)
str1[0] = "S"
print()
print(str1)

#mutable
L=[101,102,103]
print(L)
print()
L[0] = 555
print(L)
print()
