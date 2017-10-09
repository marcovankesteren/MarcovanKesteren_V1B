def code(invoerstring):
    encryptedString = []

    for i in invoerstring:
        encryptedString.append(chr(ord(i)+3))

    return ''.join(encryptedString)

print(code(input('Voer tekst in: ')))