def email():
    trys = 0  
    while trys < 5:
        try:
            email = input("Enter your email: ")
            if '@' in email and '.' in email:
              username, domain = email.split('@')
              if '.' in domain and username and domain:
               return email
            else:
                raise ValueError("Please enter a valid email address with '@' and '.' correctly placed.")
        
        except ValueError as v:
            print(v)
            trys += 1
            if trys == 5:
                print("Too many  trys. You are blocked.")
                exit()  









