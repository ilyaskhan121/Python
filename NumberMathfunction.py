# math function

import math
a = input("Enter a number : ")  # finding absolute of a number
n = int(a)
abs = abs(n)
print("Absolute = ", abs)
print("Float absolute = ", math.fabs(abs))
a = input("Enter a number : ")  # finding ceil of a number and floor
f = float(a)
print("Ceil = ", math.ceil(f))  # gives smallest intger not less than input
print("floor = ", math.floor(f))  # gives largest integer less than input
x = input("Enter a number : ")  # converting into exponential form
n = float(x)
print("Exponential form = ", math.exp(n))
print()
list = [100, 32324, 8648783, 546782, 5787865886]
print("Maximum number = ", max(list))
list = [123, 3, 4, 5, 6, 8, 7]  # finding minimum number in a list
print("Minimum number in list = ", min(list))
list = []
limit = int(input("Enter range for list : "))
print("Enter number for list : ")
for i in range(0, limit):
    ele = int(input())
    list.append(ele)
print("list =", list)
print("Minimum number in list = ", min(list))
print()
a = float(input("Enter base : "))  # power function
b = float(input("Enter power : "))
print("Answer = ", math.pow(a, b))
a = float(input("Enter a positive number : "))  # sqaure root function
print("Square root = ", math.sqrt(a))
a = float(input("Enter a number : "))  # rounding up function
b = int(input("Enter a number (limit of rounding up): "))
print("Rounded number = ", round(a, b))
a = float(input("Enter a number : "))  # fractional and integer part function
print("Tuple of fractional and integer part = ", math.modf(a))
