s="khan "*3 # for repetition
print(s)
tuple=(1,2,34,5)
print(9 in tuple) # show presence of element in string,tuple,list
print(9 not in tuple) # show absence of element
s=("{}, the khan of khan").format("ilyas")
print(s)
s="my name is %s and i am %d years old" %("ilyas",19) # %S is used for adding string to that position
# %d is used for adding decimal number to thah position
print(s)
s="pakis%can" %("t") # %c addng character
print(s)
s="helloo"
print(s.capitalize())# capitalize first letter
s="the black of my eyes.".center(40," ")# use to form new string by addition of characters 
print(s)
list=[3,5,6,3,4,6,7,9] # count elements in lists, tuples and strings
p=list.count(3)
print(p)
s="heloo".endswith("o") # search elements 
print(s)
s="how are you".endswith("you",8,11) # search element between given index
print(s)
s="rasha mama zwe de \t lewane de".expandtabs(50) # changing tabsize
print(s)
s="hi patloo hello patlo".find("hello",10) # finds string and gives location if user gives wrong location it reurns -1
print(s)
s="hi patloo hello patlo".index("hello",10) # similar to find but gives error by giving wrong index
print(s)
s="khan320".isalnum() # it will return true when there is alphanumeraic characters otherwise will be false space is not alphanumeraic character
print(s)
s="hello sir".isalnum()
print(s)
s="hellosir".isalpha() # show all alpha characters 
print(s)
s="hello sir".isalpha() # space is not alpha character
print(s)
n="1223".isdigit() # to show a string contain all numeraic digits or not
print(n)
n="ab123".isdigit()
print(n)
s="khan is back".islower() #to show all characters or in lower case
print(s)
s="Hello sir".islower()
print(s)
s=" ".isspace()
print(s)
# isnumeraic : to show string is made up of numbers
# isspace : to show string is only spaces 
# istitle : to show every sub string in a string is start with uppercase or not
seq =["walika","senga","yey"] # used to join sequence through a string
str=" - "
p=str.join(seq)
print(p)
s=len("ustaz") # show length of string
print(s)
s="WAWA KHan".lower() # convert upper to lowerinput
print(s)