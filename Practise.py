l=8
w=4
for length in range(8):
    for width in range(4):
        print(" * ",end=" ")
    print()
l=int(input("Enter length : "))
w=int(input("Enter Width : "))
s=input("Enter Symbol : ")
for length in range(l):
    for width in range(l):
        print(s,end=" ")
    print()
a=l*w
print("Area = ",a)

n = int(input("Enter Number : "))
fact = 1
for index in range(1, n+1):
    fact = fact*index
print("Factorial of ",n," = ",fact)

n=int(input("Enter Number : "))
check=0
if(n==2):
    print("Number is prime ")
if(n%2==0):
    print("Number is not prime ")
else:
    for i in range(2,n):
        if(n%i==0):
            check+=1
    if(check==0):
        print("Number is  Prime : ")
    else:
        print("Number is not prime  : ")

a=int(input("Enter Any Natural Number : "))
sum=0
for index in range(1,a+1):
    sum=sum+index
print("sum of first",a,"Natural Numbers = ",sum)

list=[444,23,234]
min=list[0]
for e in range(len(list)):
    if(min > list[e]):
        min=list[e]
print(min)

list=[1,2,3,4,5]
max=0
for e in range(len(list)):
    if(max<list[e]):
        max=list[e]
print(max)

list=[]
a=int(input("Enter Limit for list : "))
print("Enter elements for list : ")
for i in range(a):
    ele = int(input())
    list.append(ele)
print("List = ",list)
print("Even numbers in list = ",end="")
for index in list:
    if(index%2==0):
        print(index,end=" ")