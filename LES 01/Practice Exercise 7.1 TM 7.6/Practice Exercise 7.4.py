def ticker():
    infile = open('ticker.txt', 'r')
    regels = infile.readlines()
    infile.close()
    tickerdict ={}
    for regel in regels:
        ticketregel = regel.split(':')
        sleutel = ticketregel[0]
        waarde = ticketregel[1].strip()
        tickerdict[sleutel]=waarde
        return tickerdict

print(ticker())
        