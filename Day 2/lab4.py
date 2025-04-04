
num = int(input("num: "))
pyramid = []

for i in range(1,num+1):
    list = " "*num+"*"*i
    num-=1
    pyramid.append(list)

for list in pyramid:
 print(list)
