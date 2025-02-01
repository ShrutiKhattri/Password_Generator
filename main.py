import random
print("Welcome to the password Generator!")
# Alphabets (Uppercase & Lowercase)
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Numbers (0-9)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Symbols (Common Password Special Characters)
symbols = [
    '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_',
    '[', ']', '{', '}', '|', ';', ':', ',', '.','?', '/'
]
let_ch = int(input("How many letters do you want in your password? : "))
num_ch = int(input("How many numbers do you want in your password? : "))
sym_ch = int(input("How many symbols do you want in you password? : "))

#Easy Level
# password =""
#
# #Add random letters in the password
#
# for i in range(0, let_ch):
#     password += random.choice(letters)
#
# for i in range(0, num_ch):
#     password += random.choice(numbers)
#
# for i in range(0, sym_ch):
#     password += random.choice(symbols)
#
# print(password)


#Hard Level (Here we will use list instead of a string)
password_list =[]

for i in range(0, let_ch):
    password_list.append(random.choice(letters))

for i in range(0, num_ch):
    password_list.append(random.choice(numbers))

for i in range(0, sym_ch):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password=""
for char in password_list:
    password += char

print(f"Your Password is : {password}")
