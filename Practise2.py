list=[]
a=int(input("Enter limit : "))
print("Enter Elements : ")
for i in range(a):
    ele=int(input())
    list.append(ele)
print("Elements in list = " ,list)
print("Odd Numbers in List are ",end=" ")
for e in list:
    if(e%2!=0):
        print(e,end=" ")

