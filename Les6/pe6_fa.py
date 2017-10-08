kluizen = open('kluizen.txt', 'r+')

aantal = kluizen.readlines()

# Opvragen van beschikbare kluisjes
def toonKluizen():
    beschikbaar = 12 - len(aantal)
    if beschikbaar <= 0:
        vrij = 'er zijn geen kluizen meer'
    elif beschikbaar == 1:
        vrij = 'er is nog 1 kluis beschikbaar'
    else:
        vrij = ('Er zijn {} kluizen beschikbaar'.format(beschikbaar))
    return vrij

def nieuweKluis():
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # Lijst van alle kluisnummers
    bezet = []  # Lijst met bezette kluisjes

    for i in aantal:
        nummers = i.split('; ') # Splitten van regels in de textfile en aanmaken lijst met iedere regel erin
        cijfers = int(nummers[0]) # Pakken van cijfers uit de lijst
        bezet.append(cijfers) # Aanvullen van het bestand met bezette kluisjes

    for x in bezet:
        kluisnummers.remove(x)

    if len(kluisnummers) > 0:
        print('Er zijn nog vrije kluizen over.')
        wachtwoord = input('Voer een wachtwoord in: ')
        kluizen.write('{}; {}\n'.format(kluisnummers[0], wachtwoord)) # Eerste kluisje in de lijst koppelen met het wachtwoord in de textfile geschreven
        return('Je staat geregistreerd op kluisnummer ' + str(kluisnummers[0]))
    else:
        return('geen kluizen meer beschikbaar')

def kluisOpenen():
    kluisID = eval(input('Geef je kluisnummer: '))
    kluisww = input('Geef je wachtwoord: ')
    for i in aantal:
        gesplit = i.split('; ') # Splitten van code en nummer
        cijfers = int(gesplit[0])   # maakt van de kluisnummers een int waarde
        ww = gesplit[1].strip('\n') # Verwijderd de newline (enter) aan het einde van de regel, zodat het wachtwoord goed ingelezen wordt en niet met enter
        if cijfers == kluisID and ww == kluisww:
            gevonden = 'Deze combinatie klopt.'
            break # For loop stopt wanneer de combinatie goed is
        else:
            gevonden = 'Niets gevonden'  # Indien er niks gevonden wordt, wordt var 'gevonden: Niets gevonden.
    return(gevonden)

while True:
    print('1: Ik wil graag weten hoeveel kluizen nog vrij zijn.')
    print('2: Ik wil graag een nieuwe kluis.')
    print('3: Ik wil graag even iets uit mijn kluis halen.')
    print('4: Ik wil graag mijn kluis teruggeven.')
    keuzes = int(input('Geef hier je keuze in, kies een getal van 1 t/m 4: '))

    if keuzes == 1:
        print(toonKluizen())
    elif keuzes == 2:
        print(nieuweKluis())
    elif keuzes == 3:
        print(kluisOpenen())
    else:
        print('Voer een geldige keuze in')
        keuzes = int(input('Geef hier je keuze in, kies een getal van 1 t/m 4: '))

    stop = input('Annuleren? Typ Ja/Nee: ')
    if stop == 'Ja':
        break
    else:
        print('\n')
        continue

kluizen.close() # Sluiten van de textfile