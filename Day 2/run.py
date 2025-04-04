"""
num = input("enter num: ")  
while not num.isdigit():   ## not 3shan y3ed eloop
    num = input("plz enter a valid num:")

num = int(num) 

==========

text = "helloworld"
print(text.isalpha())  ## kolha klam mn 8er space aw num

==========
name = "salma"
age = 23
greeting = f"hello,{name}.you are {age}years old."  ## mmkn ashel name ,age w mkanhom 0,1
print(greeting)

==========

numbers = [1,2,3,4,5]
numbers[0]= 5
numbers.append(6)  ## hyzod mn elakhr
numbers.remove(3)  ##remove the first element have value 3
print(numbers)

=========
numbers = [3,5,6,9,8]
print(len(numbers))
numbers.sort()  ##sort mn sogher llkber
numbers.reverse() ##sort tnazly
numbers=sorted(numbers.reverse=True)  ## de eltreqa elas7 lw 3yzaha tsa3ody bshel part reverse
print(numbers)

=========
fruits= ["mango","apple","cherry"]
more_fruits=["s","l","w"]
fruits.extend(more_fruits)
print(fruits)

========
## remove lazm value aw pramater
## pop byshel index mn elakhr
## del btms7 mn el memory m2drsh a3ml return btakhod variable kolo ==== not defined
========

text = "hello world"
print("hello" not in text)    ## return true /false ..(not) bt3ks .. btstkhdm m3 if
print("salma" in text)

=======

authorized_users= ["salma","nada","aliaa","hala"]
user =input("name: ")

if user in authorized_users:
  print(f"welcom {user}")
else:
  print("valid")

========

for i in range(5):
    print(i)
    if i == 4:
        break
else:              ##else run yb2a el loop khlst 
    print("end")
            
"""

number = 17
#check divisibility from 2 to number-1
for i in range(2,number):
    if number % i ==0:
        print (f"{number} is not a prime number")
        break
else :
    # hytnfz if no breaks occures in loop
    print(f"{number} is a prime number")
    

### 3shan akhly el process asr3
number = 20
for i in range(2,int(number/2)+1):
    if number % i ==0:
        print (f"{number} is not a prime number")
        break
else :
    print(f"{number} is a prime number")    









