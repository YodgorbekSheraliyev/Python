PLACEHOLDER = "[name]"
with open('names.txt') as name_file:
    names = name_file.readlines()

with open('starting_letter.txt') as letter:
    new_letter = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_text = new_letter.replace(PLACEHOLDER, stripped_name)
        print(new_text)
        with open(f'./Letters/{stripped_name}.txt', 'w') as letter_file:
            letter_file.write(new_text)
        
 