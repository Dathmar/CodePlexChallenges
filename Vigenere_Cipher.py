"""
Create a program for the Vigenere Cipher

The vigenere cipher works similar like the ceasar cipher but better. You decide a password like 'ab'
and then repeat this password until you reach the end of your text.
So how to apply a password:
Message: Hello World
Password: ab
We add the index of the password letter to the current letter, thats all.
Message:  Hello World
Password: ababa babab
Result:   Hflmo Xosle

The program should be able to encrypt and decrypt with a given password.
Alphabet: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ
"""
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = list(alphabet)

message = input('Please provide a message to cipher:\n')

# assume good password e.g. only contains alpha for now
password = input('Please provide a password for the cipher\n')

encrypted_message = ''
pass_char = 0
for c in message: # loop over all characters in message
    if c in alphabet: # don't encrypt unsupported characters
        c_index = alphabet.index(c) # find the location of c
        pass_index = alphabet.index(password[pass_char]) # get the password character location

        encrypted_location = c_index + pass_index # apply cipher

        if encrypted_location > len(alphabet): # if the cipher is out of bounds shift back
            encrypted_location -= (len(alphabet) - 1)

        encrypted_message += alphabet[encrypted_location] # get cipher letter

        # I don't like this but it handles the next password character to apply for the cipher
        pass_char += 1

        if pass_char > len(password) - 1:
            pass_char = 0

    else: # if the character isn't in the alphabet then return that character
        encrypted_message += c

print(encrypted_message)