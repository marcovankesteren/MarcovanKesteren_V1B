import csv
from toolbox import nowFormatted

bestand = 'inloggers.csv'

def vraagOmInput():
    while True:
        naam = input("Wat is je achternaam? ")

        if naam == '':
            break

        voorl = input("Wat zijn je voorletters? ")

        gbdatum = input("Wat is je geboortedatum? ")

        email = input("Wat is je e-mailadres? ")

        schrijfWeg(naam,voorl,gbdatum,email)


def schrijfWeg(naam, voorl, gbdatum, email):

    with open(bestand, 'a', newline='') as filetje:
        csvschrijver = csv.writer(filetje)

        csvschrijver.writerow((nowFormatted(),naam,voorl,gbdatum,email))

vraagOmInput()

#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file
