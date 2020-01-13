# Freelance
A web scraping tool that parses the french property website.

Tools used:

BeautifulSoup
Regular expressions



Example to run:
$python LaboncoinFR.py -d haute_normandie -t 1 -min 100000 -max 125000 -p 1

here,
department=haute_normandie
type=maison
min price=10000
max price=	125000
particulars=1 means particulars selected. choose p 1 if seek professionals. 


Link established by the above command line switch:

https://www.leboncoin.fr/ventes_immobilieres/offres/haute_normandie/?th=1&ret=1&ps=4&pe=5&f=p




usage: LaboncoinFR.py [-h] [-d DEPARTMENT] [-c CATEGORY] [-t TYPE] [-min MIN]
                      [-max MAX] [-p PARTICULIERS]

optional arguments:
  -h, --help            show this help message and exit
  -d DEPARTMENT, --department DEPARTMENT
                        select department/state/city eg. Alsace, Guyane
  -c CATEGORY, --category CATEGORY
                        category - default is ventes_immobilieres, use this if
                        you want some other thing here
  -t TYPE, --type TYPE  Enter number. Maison:1, Apartment:2, Terrain:3,
                        Parking:4, Autre:5
  -min MIN              minimum price( The number you enter should be integer.
                        And entry should belong in the option list in the
                        website)
  -max MAX              maximum price( The number you enter should be integer.
                        And entry should belong in the option list in the
                        website)
  -p PARTICULIERS, --particuliers PARTICULIERS
                        for particuliers:1, for professionals:2

