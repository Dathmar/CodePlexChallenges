from string import ascii_lowercase

def has_all_letters(phrase):
    for c in ascii_lowercase:
        if len(phrase) == len(phrase.replace(c, '')):
            return False

    return True

phrase = input('Give me a phrase: ')

print('Your phrase is a pangram: ' + str(has_all_letters(phrase.lower())))