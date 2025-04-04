#Ask the user for his name then confirm 
# that he has entered his name(not an empty string/integers). 
# then proceed to ask him for his email and print all this data(Bonus) 
# check if it is a valid email or not

def valid_email(email):
    return '@' in email and '.' in email and email.index('.') < email.index('@')

def name():
    while True:
        name = input("Enter your name: ")
        if name.isalpha():  
            return name
        else:
            print("please enter a valid name (non-empty and not an integer).).")
                

def email():
    while True:
        email = input("Enter your email: ")
        if '@' in email and '.' in email:
         username, domain = email.split('@')
        if username and domain:
            x,y=domain.split('.')
            return email   
        else:
         print("Please enter a valid email address.")  
    
name =name()
email =email()
print(f"Name: {name}")
print(f"Email: {email}")