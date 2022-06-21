# break (key word when executed terminates the loop and always written in if)
for letter in "pakistan":
    if(letter == "k"):
        break
    print("current letter", letter)
for index in range(1, 10):
    if(index == 4):
        break
    print("your numbers are", index)
n = 10
while (n >= 1):
    print(n)
    if(n == 5):
        break
    n -= 1
a = input("Enter a number : ")
n = int(a)
for index in range(2, n):
    if(n % index == 0):
        break
if(index >= n):
    print("The number is prime : ")
else:
    print("The number is not prime : ")

print()
# continue (will skip those statements which are true according to test ecpression)
for letter in "pakistan":
    if(letter == "t"):
        continue
    print(letter)
print()
for index in range(1, 21):
    if(index % 2 != 0):
        continue
    print(index)
