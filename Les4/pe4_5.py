def kwadraten_som(grondgetallen):
    return sum([positive ** 2 for positive in grondgetallen if positive > 0])

print(kwadraten_som([8, 5, -79, 4]))