import csv

with open('gamescores.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')

    highScore = ['','',0]

    for row in reader:
        if int(row[2]) > int(highScore[2]):

            highScore = row

    print('De hoogste score is: {} op {} behaald door {}'.format(highScore[2],highScore[1],highScore[0]))