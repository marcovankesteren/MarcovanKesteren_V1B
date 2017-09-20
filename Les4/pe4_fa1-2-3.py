def standaardprijs(afstandKM):
    totaalPrijs = 0
    if afstandKM < 50:
        prijsKM = 0.8
        totaalPrijs += prijsKM * afstandKM
        return(totaalPrijs)

    if afstandKM > 50:
        totaalPrijs = totaalPrijs + 15
        prijsKM = 0.6
        totaalPrijs += prijsKM * afstandKM
    return totaalPrijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    totaalPrijs = 0
    totaalPrijs = standaardprijs(afstandKMInp)
    print(totaalPrijs)
    if leeftijd >= 12 and leeftijd <= 65:

        if weekendRit == 'j':
            TP2 = totaalPrijs / 0.35
            return TP2

        else:
            TP2 = totaalPrijs / 0.3
            return TP2


    else:
        if weekendRit == 'j':
            TP2 = totaalPrijs / 0.4
            return TP2

        else:
            TP2 = totaalPrijs
            return TP2

afstandKMInp = eval(input('Hoeveel kilometer gaat u reizen : '))

weekendRit = input('Reist u in het weekend: J/N? ')

leeftijd = int(input('Wat is uw leeftijd : '))

ritprijs2 = ritprijs(leeftijd, weekendRit, afstandKMInp)

print(ritprijs2)