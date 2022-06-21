
# if ,elif and else statements

a = input("Enter a number : ")
check = int(a)
if(check > 0) and (check < 25):
    print("The input is valid : ")
    if(check>=12):
        print("Good Evening")
    elif(check<12):
        print("Good Morning")
else:
    print("The input is invalid : ")
    print()
var = input("Enter a number : ")
n=int(var)
if(n%2==0):
        print (" NUmber is even")
        if(n>0):
            print (" Number is positive")
        elif(n<0):
            print (" Number is negative")
else:
         print ("The number is ODD")
print()
# if and else statements 
a=input("Enter a number : ")
n=int(a)
if(n%2==0):
    print("Number is even")
else:
    print("Number is odd")
