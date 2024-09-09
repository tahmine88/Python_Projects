# NATO phonetic alphabet dictionary
nato_alphabet = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
}

# Function to convert a word to NATO phonetic alphabet
def phonetic_decoder(word):
    word = word.upper()
    nato_list = [nato_alphabet[letter] for letter in word if letter in nato_alphabet]
    return nato_list

# Example usage
word_input = input("Enter a word: ")
phonetic_output = phonetic_decoder(word_input)
print(f"NATO phonetic alphabet for '{word_input}': {phonetic_output}")
