urenGewerkt = input('Hoeveel uur heb je gewerkt: ')
uurLoon = input('Wat verdien je per uur: ')
salaris = float(uurLoon) * int(urenGewerkt)
berekening = str(urenGewerkt) + ' uur werken levert ' + str(salaris) + ' Euro op.'
print(berekening)