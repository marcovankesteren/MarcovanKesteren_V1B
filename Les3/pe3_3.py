age = eval(input('Geef je leeftijd: '))
paspoort = input('Nederlands paspoort: ')

if age >= 18 and paspoort.upper() == 'JA':
    print('Gefeliciteerd, je mag stemmen!')

else:
    print('Helaas, je mag nog niet stemmen...')