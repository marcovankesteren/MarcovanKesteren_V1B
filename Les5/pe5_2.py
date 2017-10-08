def toonKaartnummers():
    infile = open('kaartnummers.txt', 'r')
    regels = infile.readlines()
    infile.close()

    for regel in regels:
        nummer, naam = regel.strip().split(', ')
        print('{} heeft kaartnummer: {}'.format(naam, nummer))

toonKaartnummers()