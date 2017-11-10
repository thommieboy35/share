#deze kant en klare dicts moeten we in onze pycharm inporteren om gebruik te kunnen maken van bepaalde functies die ddor anderen zijn gecreerd, anders moeten we deze functies zelf maken maar dit is veels te moeilijk
#tkinter zorgt er voor dat we een visuele GUI met knoppen velden en labels kunnen maken
#de massagebox van tkinter gebruiken we zodat er systeem meldingen kunnen worden gegeven bij knoppen die niet werken
#request zorgt ervoor dat onze programa verbinding kan maken met de API van de NS
#xmltodict zorgt er voor dat we de gevens in de NS API wat in XML vorm is kunnen gebruiken in onze programma/ GUI

from tkinter import *
from tkinter.messagebox import showinfo
import requests
import xmltodict

#deze functie word uitgevoerd wanneer je op VertrektijdenKnop klikt
def clicked1(master):
    #dit zorgt er voor zodra je op 'terug' klik dat de tweede window met tijden afsluit
    def close():
        losse_window.withdraw()
    #hier maak je een variable station om de invoer in de invoerveld te pakken en in de url van de NS API te plaatsen,zodat je een juiste url verwijzing (juiste station) krijgt
    station =(invoerveld.get())
    #dit is authenticatie/ om in te loggen in de NS API( Actuele trein vertrektijden en bestemmingen)
    auth_details = ('thom.dejong@student.hu.nl', 'IFuanK8OC2L30skbbKrtCSJ8_tS9a2rWp9I9nnPZKFG--83bSuJxDg')
    #verwijzing naar de webserver van de NS API, om bij de gegevens te kunnen komen ,zoals je ziet word aan het einde van de url je variable station toegevoegd dat eerder in de invoerveld is ingevuld
    api_url = 'http://webservices.ns.nl/ns-api-avt?station='+station
    response = requests.get(api_url, auth=auth_details)
    #alle gegevens worden in XML vorm geconverteerd
    VertrekXML = xmltodict.parse(response.text)
    infile = open('stations.txt', 'r')
    inhoud = infile.readlines()

    bericht= ''
    #Als het ingegeven station in het text bestand stations.txt zit gaat die door naar de for loop.
    #Is dat niet het geval Print dan wordt de else functie uitgevoerd.
    if station + '\n' in inhoud:
        #In deze for loop worden alle trein gegevens van de api toegevoegd aan de variable: bericht.
        for vertrek in VertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:


            eindbestemming = vertrek['EindBestemming']

            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[11:16]

            bericht += '\nOm ' + vertrektijd + ' Vertrekt een trein naar ' + eindbestemming
            print(bericht)
    else:
        bericht = 'Sorry dit is geen bestaand station!!!!\nLet op de applicatie is hoofdletter gevoelig!!!!'

    #Hier wordt een nieuwe window aangemaakt en ingesteld dat hij gelijk fullscreen geopend moet worden.
    losse_window = Toplevel(master)
    losse_window.overrideredirect(True)
    losse_window.geometry("{0}x{1}+0+0".format(losse_window.winfo_screenwidth(), losse_window.winfo_screenheight()))

    #Hier wordt een label aangemaakt in deze label staat wat er weergegeven moet worden om Losse_window inclusief Background foreground & font.
    label = Label(master=losse_window,
                      text=bericht,
                      background='azure',
                      foreground='gray25',
                      font=('arial', ),
                  )
    label.pack()
    label.config(justify=LEFT)

    #Hier wordt de terug button op Losse_window aangemaakt als je hier op klikt word de Losse_window afgesloten en het hoofdscherm weer geopend.
    back=Button(losse_window,text='terug', command=close)
    back.pack()



#Dit is een extratje, daarom hoeft dit niet. Als we tijd hebben zullen we dit maken

def clicked2():
    bericht = 'Sorry aan deze service wordt nog gewerkt'
    showinfo(title='popup', message=bericht)

#hoofdprogramma / menuscherm / hoofdscherm , heeft de naam root
root = Tk()
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

#dit is een tussenruimte zodat al onze knoppen en invoerverld niet helemaal aan de bovenkant van onze aplicatie plakt, deze ruite hebben we met een lebel gecreerd
tussenruimte = Label(master=root,
                     height=25,
                     width=97,
                     background='gray94',
                     foreground='gray25',
                     font=('arial', 7,))
#hier moeten we aangeven dat tussenruimte afsluit, zo hebben we een stuk van het scherm gesplitst
tussenruimte.pack()

#hier stellen we onze zelf gemaakte achtergrond in als een foto binnen het programma
Achtergrond_menu=PhotoImage(file="logo.png")
#nu het programma onze foto kent kunnen we van deze foto een label in foto-vorm maken
wallpaper = Label(root, image=Achtergrond_menu)
#plakken we op de achtergrond van onze aplicatie en stellen deze precies af
wallpaper.place(x=0,
                y=46,
                relwidth=1,
                relheight=1)

#invoerveld word hier op het hoofdscherm/startscherm gecreerd die 80 pixels breed is
invoerveld = Entry(master=root,
                   width=80)
#hier word invoerveld/ entry afgesloten en er wot nog een tussenruimte van 10 pixels aan de bovenkant en onderkant gecreerd (y-as) dit ziet er professioneler uit
invoerveld.pack(pady=10)

#hier ,maak je de knop vertrekrijden van 20 pixels breed en 1 pixel hoog
VertrektijdenKnop = Button(master=root,
                           text='Vertrektijden opvragen',
                           width=20,
                           height=1)

#dit is eigenlijk precies het zelfde wat 'command=' doet
VertrektijdenKnop.bind('<Button-1>',lambda event:clicked1(root))
#hier word vertrektijdenKnop afgesloten en een tussenruimte tussen VertrektijdenKnop en invoerveld van 30 pixeles gemaakt, zodat het mooier oogt
VertrektijdenKnop.pack(pady=30)

#hier worden de omkaderingen (frames van de onderste 3 extra knoppen gecreerd
kader_knop = Frame(root)
#hier beschrijven we dat ieder knop zijn eigen beschikbare ruimte helemaal vuld, dus in dit geval is dat 1/3 van het scherm
kader_knop.pack(fill=X, side=BOTTOM)

#hier worden de knoppen met behulp van de Button funtie gecreed (text= betekend de tekst die op de knopeen komt)
ExtraKnop1 = Button(kader_knop, text='Kopen Los kaartje', command=clicked2)
ExtraKnop2 = Button(kader_knop, text='Kopen OV-chipkaart', command=clicked2)
ExtraKnop3 = Button(kader_knop, text='Ik wil naar het buitenland', command=clicked2)

#hier word de dikte van de randen van de knop bepaald met behulp van de functie columnconfigure widht geeft dit aan
#0,1,2 geeft de plaatsen van de knoppen om de scherm aan. Dus 0 betekent dat knop 1 op 1/3 van de scherm begint, 2 betekend dat knop 2 op 2/3 van het scherm begint enz.
kader_knop.columnconfigure(0, weight=1)
kader_knop.columnconfigure(1, weight=1)
kader_knop.columnconfigure(2, weight=1)

#hier plaatsen we daadwerkelijk de knoppen in het scherm door ze in een soort tabel (waarin het scherm is verdeeld) te zetten. dit doen we met behulp van de gind functie.
# row/ rij moet altijd 0 zijn wat de knoppen moeten in een zelfde rij zitten (line-up). Column/ kolom is na ieder knop 1 plaats meer, omdat die steeds 1 plaats moet opschuiven
ExtraKnop1.grid(row=0, column=0, sticky=W+E)
ExtraKnop2.grid(row=0, column=1, sticky=W+E)
ExtraKnop3.grid(row=0, column=2, sticky=W+E)

#hier sluit de hoofdmenu/startscherm af, zoals je een begin en een einde bij elk programeertaal moet geven moet dit ook in python/tkinter
root.mainloop()