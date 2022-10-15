alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypty(text, shift):
    cipher_text = ''

    for l in text:
        letter_index = alphabet.index(l)
        
        new_letter = letter_index + shift
        
        if new_letter > 25:
            letter_position = new_letter - len(alphabet)
            new_letter = alphabet[letter_position]
        else:
            new_letter = alphabet[letter_index + shift]
        
        cipher_text += new_letter
    
    print(cipher_text)


def decrypt(text, shift):
    cipher_text = ''

    for l in text:
        letter_index = alphabet.index(l)

        new_letter = letter_index - shift

        if new_letter > 25:
            letter_position = new_letter - len(alphabet)
            new_letter = alphabet[letter_position]
        else:
            new_letter = alphabet[letter_index - shift]

        cipher_text += new_letter

    print(cipher_text)

if direction == 'encode':
    encrypty(text, shift)
elif direction == 'decode':
    decrypt(text, shift)

