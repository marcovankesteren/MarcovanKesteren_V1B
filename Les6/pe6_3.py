invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

lijst = invoer.split('-')
lijst.sort()

lijst = list(map(int, lijst))

som = sum(lijst)
grootstegetal = max(lijst)
kleinstegetal = min(lijst)
aantalgetallen = len(lijst)
gemiddelde = sum(lijst) / len(lijst)

print("Gesorteerde list van ints: ")
print(lijst)
print("Grootste getal: " + str(grootstegetal) + " en kleinste getal: " + str(kleinstegetal) + "\n"
      + "Aantal getallen: " + str(aantalgetallen) + " en som van de getallen: " + str(som) + "\n" + "Gemiddelde: " + str(gemiddelde))
