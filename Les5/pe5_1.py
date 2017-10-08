def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def table():
    print("  F     C")
    for graden_celsius in range (-30, 41, 10):
        print("{:5.1f} {:5.1f}".format(convert(graden_celsius), graden_celsius))

table()