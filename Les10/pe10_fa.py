import xmltodict #import library xmltodict

with open('stations.xml','r') as file: #open stations.xml in readmodus als file
    doc = xmltodict.parse(file.read())['Stations']['Station'] #variabele doc krijgt als waarde dat het xml bestand naar een dict moet worden gezet en dat de gelezen moet worden

    print('Dit zijn de codes en types van de {} stations:'.format(len(doc))) #

    for station in doc:
        print('{}  \t- {}'.format(station['Code'],station['Type']))

    print('\nDit zijn alle stations met één of meer synoniemen:')

    for station in doc:
        if station['Synoniemen'] != None:
            print('{}  \t- '.format(station['Code']), end='')

            for synoniem in station['Synoniemen']['Synoniem']:
                print(synoniem, end=' ')

    print('\n\nDit is de langste naam van ieder station:')

    for station in doc:
        print('{}  \t- {}'.format(station['Code'],station['Namen']['Lang']))