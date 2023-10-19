import random
import string
print("Welcome to the Password Generator!")

Alphabets='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Numbers='0123456789'
special_charachters='!@#$%^&'
    
pass_list=[]


def generate_password(length, complexity):
    
    if complexity == 'low':
        for i in range(0,length):
            random_pass= random.choice(Alphabets)
            pass_list.append(random_pass)
    elif complexity == 'medium':
        for i in range(0,length):
            random_pass= random.choice(Alphabets + Numbers)
            pass_list.append(random_pass)
        
    else:
        for i in range(0,length):
            random_pass= random.choice(Alphabets + Numbers + special_charachters)
            pass_list.append(random_pass)
    password=''.join(pass_list)

    print("Generated Password: " + password)



length=int(input("Enter the length of password "))
if length <= 0:
        print("Invalid password length.")
else:           
    
    complexity = input("Choose password complexity (low/medium/high): ").lower()
    if complexity not in ['low', 'medium', 'high']:
        print("Invalid complexity level.")
    else:
        generate_password(length, complexity)
        



