"""
name = input("Enter your name: ")

count=0

while not name.isalpha():
    print("Not Acess defined.")
    name = input("Enter your name: ")
    count += 1
    if count==4:
        print("block user")
        exit()
else: print(f"welcom {name}")

email = input("Enter your email : ")


while "@" in email and "." in email and email.index('.') < email.index('@'):
    print("not acess defined.")
    email = input("Enter your email : ")

else:
    print("welcom")


## while true:----> infinity loop btkhls 3nd break 
## if name -----> check truthy or falsy value en fe valua f name wl la"


"""
while True:
    name = input("Enter your name: ")
    if name and not name.isdigit():
        break
    else:
        print("Please enter a valid name (non-empty and not an integer).")

# Prompt the user to enter their email and ensure it's valid
while True:
    email = input("Enter your email: ")
    if '@' in email and '.' in email:
        username, domain = email.split('@')
        if username and domain:
            x,y=domain.split('.')
            if x and y:
                break
    else:
        print("Please enter a valid email address.")

# Print the validated name and email
print(f"\nName: {name}")
print(f"Email: {email}")

