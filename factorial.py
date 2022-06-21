# using forloop
a=input("Enter a number for factorial  : ")
n=int(a)
fact=1
for index in range(1,n+1):
    fact=fact*index
    
print("factorial is : ",fact)
# using while loop
a=input("Enter a number for factorial  : ")
n=int(a)
i=1
fact=1
while(i<=n):
    fact *= i
    i+=1
print("factorial is : ",fact)