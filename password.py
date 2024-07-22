import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
           'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

charectors = ['!', '@', '#', '$', '%', '^', '&', '*',
              '(', ')', '-', '_', '=', '+', '{', '}',
              '[', ']', '|', '\\', ';', ':', '"', "'",
              '<', '>', ',', '.', '/', '?']

print("Welcome to the Pypassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols do you need in your password? \n"))
nr_numbers = int(input("How many numbers do you need in your password? \n"))

password = ""

'''for char in range(1, nr_letters + 1):
    password += random.choice(letters)


for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
    

for char in range(1, nr_symbols + 1):
    password += random.choice(charectors)
    
print(password)
'''
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))


for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
    

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(charectors))

random.shuffle(password_list)

for char in password_list:
    password += char

print(f"You new password is: {password}")