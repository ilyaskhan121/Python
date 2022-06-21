import random 
list=["khan","ilyas",2,3,4] # picking random element from tuple,list,string 
string="Abuzar khan"
print("Random Element = ",random.choice(list))
print("Random Alphabet = ",random.choice(string))
n=random.randrange(100,200,2) # random.randrange(start(opt),stop,step(opt))
print(n) # start	Optional. An integer specifying at which position to start.
#stop	Required. An integer specifying at which position to end.
#step	Optional. An integer specifying the incrementation.
n=random.random() # giving random number between 0 and 1
print(n)
for i in range(5):# it will generate same random numbers 
    random.seed(0)
    print(random.randrange(100,200))
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14] # reshuffling of elementa of list
for i in range(1,4):
    random.shuffle(list)
    print(i," = ",list)
x=10
y=20
for i in range(3): # giving random numbers between limits
    n=random.uniform(x,y)
    print(n)