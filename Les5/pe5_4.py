import datetime

def registreerTijd(hardloper):
    vandaag = datetime.datetime.today()
    s = vandaag.strftime('%a %d %b %Y, %H:%M:%S')
    s+= ', '+hardloper
    outfile = open('hardlopers.txt', 'a')
    outfile.write(s+'\n')
    outfile.close()

def registreerHardloper():
    while True:
        hardlopernaam = input('Hoe heet deze hardloper?\n')
        if hardlopernaam == "":
            break
        registreerTijd(hardlopernaam)

registreerHardloper()