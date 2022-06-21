# list = [2, 3, 4, 5, 6]
# for index in range(len(list)):
#     print("number is ", list[index])
# fruits = ['banana', 'apple',  'mango']
# for index in range(len(fruits)):
#     print('Current fruit :', fruits[index])
# # nested loop
# l = 8
# w = 4
# for length in range(l):
#     for width in range(w):
#         print("*", end="")
#     print()
# # direct
# for lenth in range(5):
#     for width in range(5):
#         print("*", end=" ")
#     print()
# input from user
a = input("Enter length : ")
l = int(a)
b = input("Enter width : ")
w = int(b)
s = input("Enter symbol : ")
for lenth in range(l):
    for width in range(w):
        print(s, end=" ")
    print()
