import random
print("Welcome to Python Password generator !")

letters = ['q','w','e','r','t','y','u','i','o','p'
           ,'a','s','d','f','g','h','j','k','l',
           'z','x','c','v','b','n','m',
           'Q','W','E','R','T','Y','U','I','O','P'
           ,'A','S','D','F','G','H','J','K','L',
           'Z','X','C','V','B','N','M']
symbols = ["!", "@", "#", "$", "^", "&", "*", "(", ")", "/"]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

no_letters = int(input("How many letters would you like to have in your password? "))
no_symb = int(input("How many symbols do you want in your password? "))
no_nums = int(input("How many numbers do you want in your passwords? "))

# password = ""

# for char in range(1, no_letters + 1):
#     x = random.choice(letters)
#     password += x

# for char in range(1, no_symb + 1):
#     y = random.choice(symbols)
#     password += y
    
# for char in range(1, no_nums + 1):
#     z = random.choice(numbers)
#     password += z
    
# print(password)

password = []
for char in range(1, no_letters + 1):
    x = random.choice(letters)
    password.append(x)
    
for char in range(1, no_symb + 1):
    x = random.choice(symbols)
    password.append(x)
    
for char in range(1, no_nums + 1):
    x = random.choice(numbers)
    password.append(x)
print(password)
random.shuffle(password)
print(password)

print("".join([i for i in password]))
