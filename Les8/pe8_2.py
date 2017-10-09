import random

def monopolyWorp():
    for i in range(3):
        dobbelsteen1 = random.randrange(1,7)

        dobbelsteen2 = random.randrange(1, 7)

        print('{} + {} ='.format(dobbelsteen1, dobbelsteen2),end=' ')

        if dobbelsteen1 == dobbelsteen2:

            if i == 2:

                print('(Direct naar gevangenis)')
                break

            print('{} (dubbel)'.format(dobbelsteen1 + dobbelsteen2))
            continue

        print(dobbelsteen1 + dobbelsteen2)
        break

monopolyWorp()