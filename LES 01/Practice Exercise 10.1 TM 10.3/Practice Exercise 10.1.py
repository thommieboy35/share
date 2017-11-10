import xmltodict


def processXML(filename):
    with open(filename) as myXMLFIle:
        filestring = myXMLFIle.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary



voorbeeldendict = processXML('artikelen.xml')
voorbeelden = voorbeeldendict['artikelen']['artikel']

for voorbeeld in voorbeelden:
    if voorbeeld['naam'] is not None: #facultatief
        print(voorbeeld['naam'])

