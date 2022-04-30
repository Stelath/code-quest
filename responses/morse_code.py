n_inputs = int(input())

for i in range(n_inputs):
    dictionary = {i[0]: i[2:] for i in [input() for i in range(26)]}
    reverse_dictionary = {v: k for k, v in dictionary.items()}
    output = ''
    inp = input()
    for ch in inp:
        if ch == ' ':
            output += '    '
        else:
            output += dictionary[ch] + '   '
    output = output[:-3] + '\n'
    inp2 = input()
    for letter in inp2.split('   '):
        if letter == '':
            output += ' '
        elif letter[:1] == ' ':
            letter = letter[1:]
            output += reverse_dictionary[letter]
        else:
            output += reverse_dictionary[letter]
    print(output)