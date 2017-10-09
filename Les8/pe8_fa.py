def inlezen_beginstation(stations):

    begin = ''

    while True:
        begin = input('Voer het beginstation in: ')

        if begin not in stations:
            print('Deze trein komt niet in {}'.format(begin))
            continue
        break

    return begin

def inlezen_eindstation(stations, beginstation):

    eind = ''

    while True:
        eind = input('Voer de eindbestemming in: ')

        if eind not in stations or stations.index(beginstation) >= stations.index(eind):
            print('Deze trein komt niet in {}'.format(eind))
            continue
        break

    return eind

def omroepen_reis(stations, beginstation, eindstation):

    print('\nHet beginstation {} is het {}e station in het traject.\n'
          'Het eindstation {} is het {}e station in het traject.\n'
          'De afstand bedraagt {} station(s).\n'
          'De prijs voor het kaartje is €{},-.'
          .format(beginstation, stations.index(beginstation) + 1, eindstation, stations.index(eindstation) + 1,
                  stations.index(eindstation) - stations.index(beginstation), (stations.index(eindstation) - stations.index(beginstation)) * 5))

    print('Je pakt de trein in: {}'.format(beginstation))

    for i in range(stations.index(beginstation) + 1,stations.index(eindstation)):
        print('\t- {}'.format(stations[i]))

    print('Je stapt uit in: {}'.format(eindstation))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar Noord', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
            'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's Hertogenbos', 'Eindhoven', 'Weert',
            'Roermond', 'Sittard', 'Maastricht']

beginstation = inlezen_beginstation(stations)

eindstation = inlezen_eindstation(stations, beginstation)

omroepen_reis(stations, beginstation, eindstation)