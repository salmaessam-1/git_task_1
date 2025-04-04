##Write a program that prints the locations of "i" character in any string you added.

def loc_i():
 x=input("x:")
 for n in range(len(x)):
        if x[n] == 'i':
         return(n)        

print(loc_i())