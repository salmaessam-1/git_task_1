
arr = [] 
for i in range(5):
    num=input("enter num:")
   
    while not num.isdigit():  
      num = input("plz enter a valid num:")

arr.append(num)   
asc_numbers=sorted(arr)
des_numbers=sorted(arr,reverse=True)

print(arr)
print(asc_numbers)
print(des_numbers)