PLACE_HOLDER = "[name]"

with open(".\\Input\\Names\\invited_names.txt", "r") as invited_file:
    invited_names = invited_file.readlines()

for name in invited_names:
    handled_name = name.strip()
    with open(".\\Input\\Letters\\starting_letter.txt") as letter_file:
        letter = letter_file.read()
        letter2 = letter.replace(PLACE_HOLDER, handled_name)

    with open(f'.\\Output\\ReadyToSend\\letter_for_{handled_name}.txt', "w") as letter_for:
        letter_for.write(letter2)



