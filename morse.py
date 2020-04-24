morse_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1':'.---',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
    ' ': ' ',
    '.-':'A',
    '-...':'B',
    '-.-.':'C',
    '-..':'D',
    '.':'E',
    '..-.':'F',
    '--.':'G',
    '....':'H',
    '..':'I',
    '.---':'J',
    '-.-':'K',
    '.-..':'L',
    '--':'M',
    '-.':'N',
    '---':'O',
    '.--.':'P',
    '--.-':'Q',
    '.-.':'R',
    '...':'S',
    '-':'T',
    '..-':'U',
    '...-':'V',
    '.--':'W',
    '-..-':'X',
    '-.--':'Y',
    '--..':'Z',
    '.---':'1',
    '..---':'2',
    '...--':'3',
    '....-':'4',
    '.....':'5',
    '-....':'6',
    '--...':'7',
    '---..':'8',
    '----.':'9',
    '-----':'0'
}


def is_morse(phrase):
    if phrase.replace(' ','').replace('.', '').replace('-', '') == '':
        return True
    else:
        return False

# prompt the user for what phrase they want translated
print('what yall want translated, huh?')

#morse code doesn't differentiate between upper/lower case letters, so I'm using upper to match the dict
phraseToTranslate = input().upper()

translatedPhrase = ''

if is_morse(phraseToTranslate):
    for word in phraseToTranslate.split('  '): # morse words are split by two spaces
        for letter in word.split(' '): # morse letters are split by one space
            translatedPhrase += morse_dict[letter]

    translatedPhrase += ' '

else:
    # iterate over letters in user's phrase and use dict to translate
    for letter in phraseToTranslate:
        translatedPhrase += morse_dict[letter] + ' '


print(translatedPhrase)