import random
import string

def generate_password(length):
  lowercase = string.ascii_lowercase
  uppercase = string.ascii_uppercase
  digits = string.digits
  special_chars = string.punctuation
  password_chars = lowercase + uppercase + digits + special_chars
  password = ''.join(random.choices(password_chars, k=length))
  return password

password_length = int(input("Enter desired password length: "))
password = generate_password(password_length)
print("Your generated password is:", password)