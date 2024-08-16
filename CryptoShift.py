def caesar_cipher(text, shift, mode):
    result_text = ""
    if mode == "decrypt":
        shift = -shift  # Reverse the shift for decryption
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26  # Normalize the shift to within 26 letters
            if char.islower():
                start = ord('a')  # ASCII value for 'a'
            else:
                start = ord('A')  # ASCII value for 'A'
            
            # Encrypt or decrypt the character
            shifted = ord(char) - start + shift_amount
            shifted %= 26  # Ensure it wraps around the alphabet
            result_text += chr(start + shifted)
        else:
            result_text += char  # Non-alphabetic characters are not changed
    return result_text

# Asking user whether to encrypt or decrypt
mode = input("Do you want to 'encrypt' or 'decrypt' the text? ").lower()
while mode not in ['encrypt', 'decrypt']:
    mode = input("Invalid option. Please choose 'encrypt' or 'decrypt': ").lower()

# Input for text and shift amount
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

# Process the text and display the result
result = caesar_cipher(text, shift, mode)
print("Result:", result)
