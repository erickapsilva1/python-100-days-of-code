sentence = input()

word_count = {word:len(word) for word in sentence.split()}

print(word_count)

