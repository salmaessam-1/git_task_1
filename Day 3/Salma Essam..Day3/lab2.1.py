
def numbers():
    arr=[]
    for i in range(5):
        num=input("enter num: ")
        while not num.isdigit():  
             num = input("plz enter a valid num:")
        arr.append(int(num))
        asc_numbers=sorted(arr)
        des_numbers=sorted(arr,reverse=True)

    return(arr, asc_numbers, des_numbers)  

print(numbers())




