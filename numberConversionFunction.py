# conversion functions
a=input("Enter a number : ")
n=int(a) # converts string to int type
print(type(n))
a=input("Enter a number : ")
l=int(a) # converts int to long(in python every int is of long type)
print(type(l))
a=input("Enter a number : ")
f=float(a) # converts string to float type
print(type(f))
a=input("Enter a number : ")
c=complex(a) # converts string to complex type with imaginary part = 0j
print(type(c))
print(c)
a=input("Enter a number : ")
b=input("Enter a number : ")
n=int(a)
n2=int(b)
c=complex(n,n2) # converts string to complex type with imaginary number = to 2nd input number
print(type(c))
print(c)
