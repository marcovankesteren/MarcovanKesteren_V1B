def ticker(filename):
    file = open(filename,'r')

    stockCompanies = file.readlines()

    file.close()

    tickers = {}

    for i in stockCompanies:
        index = i.index(':')
        tickers.update({i[:index]:i[index+1:-1]})
        tickers.update({i[index+1:-1]:i[:index]})
    return tickers

def find():
    tickers = ticker('Stocks.txt')

    companyName = input('Voer de ticker of de naam van het bedrijf in: ')

    if companyName in tickers:
        if len(tickers[companyName]) > len(companyName):
            print('Bedrijfsnaam: {}'.format(tickers[companyName]))

        else:
            print('Ticker symbool: {}'.format(tickers[companyName]))

    else:
        print('Bedrijfsnaam of ticker symbool niet gevonden.')

find()