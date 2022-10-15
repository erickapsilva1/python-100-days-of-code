alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    cipher_text = ''

    for l in text:
        letter_index = alphabet.index(l)
        
        if direction == 'encode':
            new_letter = letter_index + shift
        elif direction == 'decode':
            new_letter = letter_index - shift
        
        if new_letter > 25:
            if direction == 'encode':
                letter_position = new_letter - len(alphabet)
            elif direction == 'decode':
                letter_position = new_letter + len(alphabet)
            new_letter = alphabet[letter_position]
        else:
            if direction == 'encode':
                new_letter = alphabet[letter_index + shift]
            elif direction == 'decode':
                new_letter = alphabet[letter_index - shift]
        
        cipher_text += new_letter
    
    print(f'The {direction}d is {cipher_text}')


caesar(text, shift, direction)
