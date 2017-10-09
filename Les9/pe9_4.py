import csv

with open('producten.csv', 'r') as file:
    reader = csv.DictReader(file)

    duursteProduct = None

    minsteVoorraad = None

    totaalAantal = 0

    for row in reader:
        if totaalAantal == 0:
            duursteProduct = minsteVoorraad = row

        if float(row['Prijs']) > float(duursteProduct['Prijs']):
            duursteProduct = row

        if int(row['Voorraad']) < int(minsteVoorraad['Voorraad']):
            minsteVoorraad = row

        totaalAantal += int(row['Voorraad'])

    print('Het duurste product is :{} en die kost: €{:2}.\n'
          'Er zijn slechts {} exemplaren op voorraad van het product met artikelnummer: {}\n'
          'In totaal hebben we {} producten in ons magazijn liggen.'
          .format(duursteProduct['Naam'], duursteProduct['Prijs'], minsteVoorraad['Voorraad'],
                  minsteVoorraad['Artikelnummer'], totaalAantal))