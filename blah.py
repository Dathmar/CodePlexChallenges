#print('One for ' + (lambda name: input('give name: /n'))  + ' , one for me.')

phrase = input('give me a phrase \n')

acronym = ''
for word in phrase.split(' '):
    acronym += word[0].upper()

print(acronym)