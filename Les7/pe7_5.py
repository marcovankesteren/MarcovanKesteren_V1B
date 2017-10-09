def namen():

    studenten = {}

    while True:
        name = input('Volgende naam: ')

        if name != '':
            if name in studenten:
                studenten[name] += 1

            else:
                studenten[name] = 1

        else:
            break

    for i in sorted(studenten, key=studenten.get):

        if studenten[i] == 1:
            print('Er is 1 student met de naam {}'.format(i))

        else:
            print('Er zijn {} studenten met de naam {}'.format(studenten[i], i))

namen()