##Write a program that generate a multiplication table from 1 to the number passed.
## list of lists

def table(num):
    num=int(num)
    Table1=[]
    
    for i in range(1,num+1):
        Table2 = []
        for j in range(1, i + 1):
            
            Table2.append(i*j)
            print(Table2)
        Table1.append(Table2)
        
    print(Table1)   
   
    return

table(3)


    
