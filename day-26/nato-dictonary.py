import pandas

nato_dic = pandas.read_csv('files/nato_phonetic_alphabet.csv')

new_alphabet = {row.letter: row.code for (index, row) in nato_dic.iterrows()}

word = input('Enter a word: ').upper()

output_list = [new_alphabet[letter] for letter in word]

print(output_list)