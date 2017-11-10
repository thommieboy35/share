import xmltodict

def processXML(filename):
    with open(filename) as myXMLFIle:
        filestring = myXMLFIle.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

voorbeeldendict = processXML('FA.xml')
stations = voorbeeldendict['Stations']['Station']

print('Dit zijn de codes en types van de 4 stations:')
for station in stations:
    print('{:4} - {}'.format(station['Code'], station['Type']))

print('Dit zijn alle Stations met één of meer synoniemen')
for station in stations:
    if station['Synoniemen'] is not None:
        print('{:4} - {}'.format(station['Code'], station['Synoniemen']))

for station in stations:
    print('{:4} - {}'.format(station['Code'], station['Namen']['Lang']))