"""
data = {
    "fruits":["apple","banana","cherry"],
    "vegatables":["carrot","tomato","union"]
}
print(data["fruits"][1])
print(data.items())

========
## hyshel union w add f fruits
x= data["vegatables"].pop()
data["fruits"].append(x)
========

person["age"] =31 ##change l value fo2 & add 
person["height"]=165
## delete dic
del person["height"]
person.pop("height") ##delete lazm gwa pop key
person.popitem() ##delete last elelmet
person.clear() ## remove 
persondata.update(otherdata) ##hy3ml update ll keys elmwgoda w add key elgded lw msh mwgod person data

=======
list=[{"name":"omar","pass":"123"},{"name":"salma","pass":"456"}]

=======
###function
def show():
    print("hello")
show()    

def show(x): ## x----> paramater variable
    print(x)   ##
show("hello")    

def show(x): 
    return(x) ##
y=(show("hello"))
print(y)

======
def addnum(x,y):
    z=x+y
    return z
result = addnum(2,3)
print(result)
  
### mfesh overright  python 8er btre2a de w tre2a 3la mob
def area(x,y,z=1): ##z=1----> default value
    return x*y*z
print(area(2,3,6))
print(area(2,3))
===============

def area(*x): # *---> collection of values
    z=0
    for i in x:
        z+=i
    return z
print(area(1,2,3,4,5))    "
======


def web():
   users=[{"name":"omar","pass":"123"},{"name":"salma","pass":"456"}]
   name=input("enter your name: ")

   if  name in users :
      password = input("enter you pass:")
      if password == users[name]:
        print("welcom")
      else:
        print("plz enter a valid email passs.") 
   else :
    print("plz enter a valid name.") 

web()   

"""
def multiplication_table():
    x = int(input("Enter a number: "))
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            return(f"{i} * {j} = {i * j}")

print(multiplication_table())

