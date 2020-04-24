# print frame

phrase = input('Please provide a phrase\n')
words = phrase.split(' ')

frame_width = len(max(words, key=len)) + 4

buffer_line = '*' * frame_width

print(buffer_line)

for word in words:
    to_print = '* ' + word
    to_print += ' ' * (frame_width - len(to_print) - 2) + ' *'
    print(to_print)

print(buffer_line)

