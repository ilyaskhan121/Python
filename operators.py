a=10 #addition
b=98
sum=a+b
str="the sum is {2}"
print(str.format(a,b,sum))
print("The sum  is {2}".format(a, b ,sum)) 
print("The sum of {0} and {1} is {2} ".format(a,b,sum)) 
print("The sum is ",sum)
num1 = 1.5
num2 = 6.3
sum = num1 + num2
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
num1 = input("Enter first number : ") # taking input from users
num2 = input("Enter second number : ")
sum = float(num1) + float(num2) #here the numbers are converted to float
print("The sum is {2}".format(num1,num2,sum))
#finding power
b=2
e=8 
p=b**e
print("{0} power {1} is {2}".format(b ,e , p))
print()
b=input("Enter base : ")
e=input("Enter ecponent : ")
pow=int(b)**int(e)
print("Answer is ",pow)
