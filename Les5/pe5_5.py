def gemiddelde():
    willekeurigeZin = input('Voer een willekeurige zin in: ')

    alleWoorden = willekeurigeZin.strip().split()

    aantalWoorden = len(alleWoorden)

    accumulator = 0

    for woord in alleWoorden:
        accumulator += len(woord)

    print('De gemiddelde lengte van de woorden in deze zin is: {}'.format(accumulator/aantalWoorden))

gemiddelde()