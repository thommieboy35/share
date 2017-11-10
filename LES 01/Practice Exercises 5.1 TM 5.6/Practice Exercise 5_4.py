import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime('%a %d %b %y')
print(s)

naam = (input('wat is je naam?:'))
tijd = (input('wat is je tijd?:'))

text = (str(s)+ ' ' +str(tijd) + ' ' + str(naam) +"\n" + '10:46:04, Piet' )
outfile = open('hardlopers.txt', 'w')
outfile.write(text)
outfile.close()




