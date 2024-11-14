import string

letters_list = list(string.ascii_lowercase)

def encrypt(text, shift):
    enc_text = ''
    for letter in text:
        if letter not in letters_list:
            enc_text += letter
            continue
        enc_index = letters_list.index(letter) + shift
        enc_index %= len(letters_list)
        enc_text += letters_list[enc_index]
    return enc_text

def decrypt(text, shift):
    dec_text = ''
    for letter in text:
        if letter not in letters_list:
            dec_text += letter
            continue
        enc_index = letters_list.index(letter) - shift
        enc_index %= len(letters_list)
        dec_text += letters_list[enc_index]
    return dec_text

def cypher():
    is_finished = False
    while not is_finished:
        text = input("Enter the text: ").lower()
        shift = int(input("How many shift: "))
        method = ""
        result = ''
        while method not in ["encode", "decode"]:
            method = input("Please select correct method. encode/decode ")
        if method == "encode":
            result = encrypt(text, shift)

        elif method == "decode":
            result = decrypt(text, shift)
        else:
            print("Please select correct method.")
        print(result)
        is_continue = input("Do you want to continue? (y/n) ")
        if is_continue.lower() == "y": is_finished = False
        else: is_finished = True

    
print(cypher())
            
            
        