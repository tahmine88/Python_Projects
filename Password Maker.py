import random
import string

def generate_password(length, keyword):
    if len(keyword) >= length:
        return "The length must be longer than the keyword length."
    
 
    remaining_length = length - len(keyword) - 1  
    

    numbers = ''.join(random.choices(string.digits, k=remaining_length))
    
    symbol = '_'
    

    password = ''.join([keyword, symbol, numbers])
    return password


length = int(input("Enter the desired length of the password: "))
website = input("Enter the website or purpose for this password (e.g., Digikala): ").strip()
keyword = website.upper()

password = generate_password(length, keyword)
print("Your new password is:", password)
