list=[] # int type only
l=int(input("Enter limit of list : "))
print("Enter element  for list : ")
for index in range(l):
    ele=int(input())
    list.append(ele)
print(list)
list=[] # both string and int type
l=int(input("Enter limit of list : "))
print("Enter element  for list : ")
for index in range(l):
    ele=[input(),int(input())]
    list.append(ele)
print(list)

