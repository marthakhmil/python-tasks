def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list

# return ''.join('{}. {}\n'.format(i, x) for (i, x) in enumerate(animals, 1))
