# isogram
ascii_lowercase = 'qwertyuiopasdfghjklzxcvbnm'

def has_one_or_zero_letters(phrase):
    for c in ascii_lowercase:
        if not len(phrase) - len(phrase.replace(c, '')) < 2:
            return False

    return True


def has_one_or_zero_letters_recursive(phrase, start = 0):
    if start == len(ascii_lowercase):
        return True
    elif not len(phrase) - len(phrase.replace(ascii_lowercase[start], '')) < 2:
        return False
    else:
        return has_one_or_zero_letters_recursive(phrase, start + 1)

phrase = input('Give me a phrase: ')

print('Your phrase is a pangram: ' + str(has_one_or_zero_letters_recursive(phrase.lower())))

print(has_one_or_zero_letters_recursive('lumberjacks'))
print(has_one_or_zero_letters_recursive('background'))
print(has_one_or_zero_letters_recursive('downstream'))
print(has_one_or_zero_letters_recursive('six-year-old'))
print(has_one_or_zero_letters_recursive('isograms'))
print(has_one_or_zero_letters_recursive('blahblah'))
print(has_one_or_zero_letters_recursive('doggies'))
print(has_one_or_zero_letters_recursive('alphabets'))