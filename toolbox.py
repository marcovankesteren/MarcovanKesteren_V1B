import datetime
import xmltodict
import dicttoxml

def nowFormatted():
    return  datetime.datetime.today().strftime('%a %d %b %Y, %H:%M:%S')

def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

def generateXML(filename, thedictionary):
    with open(filename, 'w', newline = '') as myXMLFile:
        myXMLFile.writelines(dicttoxml.dicttoxml(thedictionary,False).decode())