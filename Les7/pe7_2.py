woord = input('Geef een string van vier letters: ')

while True:

        if len(woord) != 4:
            woord = input('Geef een string van vier letters: ')
        else:
            print('Inlezen van correcte string: ' + woord + ' is geslaagd!')
            break
