# function of addition
x=int(input("enter the value of x "))
y=int(input("enter the value of y "))

def addition():
    print(x+y)
    
addition()


#working  with  strings
name=input("whta is your name?").strip()
def hello(name):#a memory space= the bracket can intake any value
    print("hello, ",name)#memory space=the "name"can be any value
    
hello(name)#takes the name that the user inputs


#the above code in another method
name=input("whta is your name?").strip()

def hello(z="WORLD"):
    print("hello, ",z)
    
hello(name)#when you leave the brackets empty it will output WORLD thr default value
#but with name inside it will output name
    
    
