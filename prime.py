a = input("Enter number for prime test : ")
n = int(a)
if(n % 2 == 0):
    print("Number is not prime : ")
else:
    check = 0
    for index in range(2, n):
        if(n % index == 0):
            check += 1
    if(check == 0):
        print("Number is prime : ")
    else:
        print("Number is not prime : ")
