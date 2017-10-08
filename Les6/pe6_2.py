list1 = eval(input("Geef lijst met minimaal 10 strings: "))

list2 = []

for word in list1:
    word.strip()
    if len(word) == 4:
        list2.append(word)

print(list2)

