# while loop for generating numbers 
n=1
while(n<=10):
    print("The number is ",n)
    n+=1
# forloop 
# generating numbers
for index in range(1,11):
    print(index,end=" ")
print()
# tables
n=3
for index in range(1,11):
    print(n ," * " , index  ,"=" ,index*3)
# user define tables
a=input("Enter number for table : ")
n=int(a)
b=input("Enter limit  : ")
l=int(b)
for index in range(1,l):
    print(n," * ",index," = ",index*n)
# printing elements of tuples
tuple={1,2,3,4,5,6,7,8,9,10}
for numbers in tuple:
    print(numbers)
# printing elements of list
list=["ilyas ","abuzar","muba ","fahad"]
for names in list:
    print(names)
# printing alphabets of string
word="pakistan"
for i in word:
    print(i)