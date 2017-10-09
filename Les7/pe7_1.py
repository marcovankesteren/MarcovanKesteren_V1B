def som():
    total = 0
    while True:
        nextInt = input('Next int: ')
        if int(nextInt) == 0:
            break

        total += int(nextInt)

    return(total)

print('De som van de ingevoerde getallen is:', som())