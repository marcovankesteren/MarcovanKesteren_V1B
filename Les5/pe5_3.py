def analyseerKaartnummers():
    infile = open('kaartnummers.txt')
    regels = infile.readlines()
    infile.close()
    print('Deze file telt {} regels'.format(len(regels)))

    nummers = []
    for regel in regels:
        nummers.append(int(regel.strip().split(', ')[0]))
    grootsteGetal = max(nummers)
    print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(grootsteGetal, nummers.index(grootsteGetal)+1))

analyseerKaartnummers()



