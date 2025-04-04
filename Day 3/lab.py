def web():
   users=[{"name":"omar","pass":"123"},{"name":"salma","pass":"456"}]
   name=input("enter your name: ")
   for dict in users:
   
         if name == dict["name"]:
             password = input("password")
             if password== dict["pass"]:
                print("authorized")
                return 1
   else:
       print("un auth")
       return 0
    
    
web()   


