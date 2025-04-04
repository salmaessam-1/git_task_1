"""
##set
x=[1,2,3,5,5,5,5]
x=set(x) ##set --->btshel el duplicate
print(x)
y=list(x) ##convert to list 3shan a2dr a3ml loop 3leha
print(y)

x.add(4)
x.remove(2)

removed_element=x.pop() ##byshel awl rkm,,msh hynf3 pop(3) el gwa pop index wna m3ndesh index f set
print(removed_element)
print(x)

===========
def test(*x): by7wlha tuble
def test(**x): ---> dict"
==========
def test(**x):
    print(x)   ##------> dict
    print(*x)  ##----->keys
    print(x["name"])

test(name="salma",age="23")  
=========

squares=[]
for x in range(1,11):
    squares.append(x**2)

print(squares)

squares=[x**2 for x in range(1,11)]   ## range 0-->10
print(squares)

l=[x**2 for x in range(10) if x%2==0]  ## range 0--->10
print(l)

==============

fruits =['apple','banana','cherry']

for index, fruit in enumerate(fruits):
    print(index,fruit)
    print(index+1,fruit)


name =['apple','banana','cherry']
for index, name in enumerate(name,start=1):
    print(f"index{index}:{name}")

===========
import re
match = re.match(r"hello",text)
"""

def valid_email(email):
    if '@' in email and '.' in email:
        username, domain = email.split('@')
        if '.' in domain and username and domain:
            return True
    return False


def get_name():
    attempts = 0  # Track the number of attempts
    while attempts < 5:
        try:
            name = input("Enter your name: ").strip()
            if name.isalpha():  # Ensure name contains only alphabetic characters
                return name
            else:
                raise ValueError("Name must contain only alphabetic characters (no numbers or spaces).")
        except ValueError as e:
            print(e)
            attempts += 1
            if attempts == 5:
                print("Too many invalid attempts. You are blocked.")
                exit()  # Exit the program if the user fails 5 times


def get_email():
    attempts = 0  # Track the number of attempts
    while attempts < 5:
        try:
            email = input("Enter your email: ").strip()
            if valid_email(email):  # Validate the email format
                return email
            else:
                raise ValueError("Please enter a valid email address with '@' and '.' correctly placed.")
        except ValueError as e:
            print(e)
            attempts += 1
            if attempts == 5:
                print("Too many invalid attempts. You are blocked.")
                exit()  # Exit the program if the user fails 5 times


# Main program execution
name = get_name()
email = get_email()

# Print the gathered information
print(f"\nName: {name}")
print(f"Email: {email}")


