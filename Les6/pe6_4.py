studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    for cijfers in studentencijfers:
        totaalStudent = sum(cijfers)
        aantal = len(cijfers)
        gemiddelde = totaalStudent / aantal
        print('Gemiddelde cijfer voor student: ', gemiddelde) # Geeft gemiddelde aan voor student

def gemiddelde_van_alle_studenten(studentencijfers):
    gemiddeldes = []

    for cijfers in studentencijfers:
        gemiddeldes.append(sum(cijfers) / len(cijfers))
    print(sum(gemiddeldes) / len(gemiddeldes))

gemiddelde_per_student(studentencijfers)
gemiddelde_van_alle_studenten(studentencijfers)
