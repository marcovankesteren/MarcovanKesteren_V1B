kosten = 4356

reizigers = input('Voer het aantal reizigers in: ')

try:
    print(reizigers)

    if int(reizigers) < 0:
        raise ValueError
    print(kosten / int(reizigers))

except ZeroDivisionError:
    print('Delen door nul kan niet!')

except ValueError:
    print('Negatieve getallen zijn niet toegestaan!')

except TypeError:
    print('Gebruik cijfers voor het invoeren van het aantal!')

except:
    print('Onjuiste invoer!')