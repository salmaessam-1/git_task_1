##Write a program that counts up the number of 
# vowels [a, e, i, o, u]contained in the string.


def count():
    V = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    C = 0
    X = input("x: ")
    for i in X:
        if i in V:
            C +=1

    print(f"number of vowels : {C}")   
    return    
        
count()




