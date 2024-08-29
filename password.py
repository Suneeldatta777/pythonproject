import random
import string

password_length = int(input("enter the length of the password: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(password_length))

print("your generated password is:", password)