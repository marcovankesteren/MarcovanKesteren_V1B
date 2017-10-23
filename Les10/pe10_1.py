import xmltodict

with open('producten.xml', 'r') as file:
    xmlDoc = xmltodict.parse(file.read())

    for product in xmlDoc['artikelen']['artikel']:
        print(product['naam'])