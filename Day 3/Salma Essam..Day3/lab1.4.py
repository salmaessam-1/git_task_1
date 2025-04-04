#Write a program that generate a multiplication table from 1 to the number passed.

def table():
    x = int(input("Enter a number: "))
    for i in range(1, x + 1):
        for j in range(1, i + 1):
         print(f"{i} * {j} = {i * j}")
    return       
            
table()