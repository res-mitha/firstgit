import string
import getpass
def password_check(password):
    strength=0
    if any (char.isupper() for char in password): 
        strength+1
    if any (char.islower() for char in password ):
        strength+1
    if any (char.isdigit() for char in password):
        strength+1
    if any (char in string.punctuation for char in password):
        strength+1
    if len(password)>8:
        strength+1
       
    if strength>=5:
        print("Strong")
    elif 3>= strength <=5:
        print("Medium")
    else:
        print("weak")
        
user_password=getpass.getpass("Enter your password:")
result=password_check(user_password)
print(result)
        
