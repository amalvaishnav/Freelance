# -*- coding: utf-8 -*-

'''
 Use python version 2.7
First you have to install python 'pip' in your 'raspberry pi/linux-system'. A way to do this is to run command "sudo apt-get install pip"
Then you can add python package-dependencies  by going into command-line and type these:
"pip install bs4"
"pip install json"
"pip install string"
"pip install pprint"
"pip install urllib"
"pip install re"
"pip install sys"
"pip install unicodecsv"
'''
from bs4 import BeautifulSoup
import urllib2, json,time,random, string, pprint, re, sys, argparse
import unicodecsv as csv
random_time_delay=[1,10]#For random time delay, define range here eg 1 to 10
prc = {'0': '0',"25000": "1","50000": "2","75000": "3","100000": "4",
       "125000": "5","150000": "6","175000": "7","200000": "8","225000": "9",
       "250000": "10","275000": "11","300000": "12","325000": "13","350000": "14",
       "400000": "15","450000": "16","500000": "17","550000": "18","600000": "19",
       "650000": "20", "700000": "21","800000": "22","900000": "23",
       "1000000": "24","1100000": "25", "1200000": "26","1300000": "27",
       "1400000": "28","1500000": "29", "2000000": "30","2000000+": "31"}
'''
here all statements starting with 'def' are functions So you should reach directly to line number 102,
where actuall code sequence starts. 
USER AGENT GOT GOOD USING MANUAL HEADER HERE. So header would be no more 'Python 2.7/urllib'. It would be 'mozila/5.0.....'
'''


def get_url(url):
    req = urllib2.Request(url, None, {
        'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
    return urllib2.urlopen(req).read()


def beautify(url):
    source = get_url(url)
    return BeautifulSoup(source, "html.parser")


def ret_list(x, f, surf):
    plot_list = []
    val = []
    a = b =c= x
    while (True):
        try:
            ind2 = x.index('ares')
        except:
            break
        match = (re.findall('^.*?((\d*\.\d+|\d*\ \d+|\d*\,\d+|\d+) *ares)', x[ind2 - 7:]))
        if not match:
            try:
                match = re.findall(unicode('^.*?((\d*\.\d+|\d*\ \d+|\d*\,\d+|\d+) *ares)', "utf-8", errors="ignore"),
                                   x[ind - 6:])
            except:
                break
        match_temp = match[0][1]
        match_temp = match_temp.replace(' ', '')
        if match_temp.find(','):
            match_temp = str(match_temp.replace(',', '.'))

        plot_list.append(100 * float(match_temp))
        x = x[ind2 + 3:]
    while (True):
        try:
            try:
                ind4 = c.index('hectare')
            except:
                ind4 = c.index('ha ')
        except:
            break
        match4 = (re.findall('^.*?((\d*\.\d+|\d*\ \d+|\d*\,\d+|\d+) *(hectare|Hectare|ha +))', c[ind4 - 7:]))

        if not match4:
            try:
                match4 = re.findall(
                    unicode('^.*?((\d*\.\d+|\d*\ \d+|\d*\,\d+|\d+) *(hectare|Hectare|ha +))', "utf-8", errors="ignore"), c[ind - 6:])
            except:
                break
        match_temp4 = match4[0][1]
        match_temp4 = match_temp4.replace(' ', '')
        if match_temp4.find(','):
            match_temp4 = str(match_temp4.replace(',', '.'))

        plot_list.append(10000 * float(match_temp4))
        c = c[ind4 + 7:]
    while (True):
        try:
            ind3 = a.index('m2')
        except:
            break
        match2 = (re.findall('^.*?((\d*\.\d+|\d*\ \d+|\d*\,\d+|\d+) *m2)', a[ind3 - 7:]))
        if not match2:
            try:
                match2 = re.findall(unicode('^.*?((\d*\.\d+|\d*\ \d+|\d*\,\d+|\d+) *m2)', "utf-8", errors="ignore"),
                                    a[ind - 6:])
            except:
                break

        match2_temp = match2[0][1]
        match2_temp=match2_temp.replace(' ','')
        if match2_temp.find(','):
            match2_temp = match2_temp.replace(',', '')
        plot_list.append(float(match2_temp))
        a = a[ind3 + 3:]
    while (True):
        o = 'm²'
        try:
            ind = b.index(unicode(o, "utf-8", errors="ignore"))
        except:
            break
        match3 = (
            re.findall(unicode('^.*?((\d*\.\d+|\d*\ \d+|\d*\,\d+|\d+) *m²)', "utf-8", errors="ignore"), b[ind - 7:]))
        if not match3:
            try:
                match3 = re.findall(unicode('^.*?((\d*\.\d+|\d*\ \d+|\d*\,\d+|\d+) *m²)', "utf-8", errors="ignore"),
                                    b[ind - 6:])
            except:
                break
        match3_temp = match3[0][1]
        match3_temp = match3_temp.replace(' ', '')
        if match3_temp.find(','):
            match3_temp = match3_temp.replace(',', '')
        plot_list.append(float(match3_temp))
        # print 'p' + str(plot_list)
        b = b[ind + 3:]
    if plot_list:

        for io in plot_list:
            if float(io) > float(surf):
                val.append(float(io))
        if not val:
            return []
    else:
        return []
    if f == 0:
        if (len(val) > 1):
            val_list = [min(val), max(val)]
        else:
            val_list = ['', max(val)]
    else:
        val_list = [surf, max(val)]
    # print val_list
    return val_list

def pg(url):
    # url="https://www.leboncoin.fr/ventes_immobilieres/offres/poitou_charentes/?ps=5&pe=10&ret=1&f=p"
    try:
        r = beautify(url)
        pgs = r.find('span', {'class': 'total_page'}).text
        return pgs
    except:
        return 1


'''
The following code is responsible for argument command line switching
"python LaboncoinFR.py --help" will tell you these things. 
'''
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--department", default="Alsace", help="select department/state/city eg. Alsace, Guyane....(default is Alsace)", )
parser.add_argument("-c", "--category",
                    help="category - default is ventes_immobilieres, use this if you want some other thing here",
                    default="ventes_immobilieres", )
parser.add_argument("-t", "--type", type=int,
                    help="Enter number.  Maison:1, Apartment:2, Terrain:3, Parking:4, Autre:5")
parser.add_argument("-min",default='0',
                    help="minimum price( The number you enter should be integer. And entry should belong in the option list in the website(default is 0))", )
parser.add_argument("-max",default='2000000+',
                    help="maximum price( The number you enter should be integer. And entry should belong in the option list in the website(default is 2000000+))", )
parser.add_argument("-p", "--particuliers", type=int,help="for particuliers:1, for professionals:2")
args = parser.parse_args()
url = "https://www.leboncoin.fr/" + args.category + "/offres/" + args.department.lower() + "/?th=1"
#url formation by command line parameters
terrain = 0
if args.type:
    url = url + '&ret=' + str(args.type)
    if args.type == 3:
        terrain = 1
if args.min:
    url = url + '&ps=' + str(prc[str(args.min)])
if args.max:
    url = url + '&pe=' + str(prc[str(args.max)])
if args.particuliers:
    if args.particuliers == 1:
        url = url + '&f=p'
        parti="Particuliers"
    else:
        url = url + '&f=c'
        parti="Professionelles "
else:
    parti=''

print url
count = 1
num_of_entry=0

page = pg(url)#this figures out number of pages involved in the search
'''
Actual looping of every search entries starts here.
'''

for j in range(int(page)):
    url = str(url) + '&o=' + str(j + 1)
    # url= "https://www.leboncoin.fr/ventes_immobilieres/offres/aquitaine/?o="+str(j+1)+"&ps=2&pe=5&ret=2&f=p"
    data = beautify(url)
    try:
        res = data.find('section', {'class': 'tabsContent block-white dontSwitch'}).ul
    except:
        break
    for i in res:
        link1 = str(re.findall('href="//www.*?"', str(i))).lstrip("[\'href=\"//").rstrip("\"\']")
        plot_list = []
        if link1:
            dept = data.find('div', {'class': 'selectWrapper select_location'}).find('option', {'value': '1'}).text
            catg = data.find('div', {'class': 'selectWrapper selectCategory'}).find('span', {
                'id': 'searchboxToggleCategory'}).text
            uid = re.findall('([0-9]+)', link1)[0]
            data2 = beautify("https://" + link1)
            if re.findall('ispro',str(i)):
                parti='Professionnels'
            else:
                parti='Particuliers'
            try:
                typ = re.findall('"key_label":"Type de bien","value_label":"([A-Za-z0-9]+)"', str(data2))[0]
                if typ=='Terrain':
                    terrain=1
                price = data2.find('span', {'class': '_1F5u3'}).text
                price = re.findall('([0-9]+)', re.sub(r"\s+", "", price, flags=re.UNICODE))
                postal = re.findall('"zipcode":"([0-9]+)"', str(data2))[0]
            except:
                continue
            title = data2.find('h1', {'class': '_1KQme'}).text
            if re.search("€|'\u20ac'", title):
                title = title.replace('€', '')
                title = title.replace('\u20ac', '')
            datime = data2.find('div', {'class': '_3Pad-'}).text
            datime = ''.join(i for i in datime if ord(i) < 128)
            datime = string.replace(datime, 'h', ':')
            desc = data2.find('meta', {'name': 'description'})['content']
            '''Following is the surface and plot area algorithm'''
            surface = re.findall('"key_label":"Surface","value_label":"([0-9]+) m²"', str(data2))

            if surface:
                surface = surface[0]
                f = 1
                try:
                    plot = ret_list(desc, f, surface)[1]
                except:
                    plot = ''
            elif (re.findall('^.*?((\d+\.\d+|\d+\ \d+|\d+\,\d+|\d+) *m²)', title)):
                surface = (re.findall('^.*?((\d+\.\d+|\d+\ \d+|\d+\,\d+|\d+) *m²)', title))[0][1]
                surface=surface.replace(' ', '')
                f = 1
                try:
                    plot = ret_list(desc, f, surface)[1]
                except:
                    plot = ''
            elif (re.findall('^.*?((\d+\.\d+|\d+\ \d+|\d+\,\d+|\d+) *m2)', title)):
                surface = (re.findall('^.*?((\d+\.\d+|\d+\ \d+|\d+\,\d+|\d+) *m2)', title))[0][1]
                surface = surface.replace(' ', '')
                f = 1
                try:
                    plot = ret_list(desc, f, surface)[1]
                except:
                    plot = ''

            else:
                surf1 = 40
                f = 0
                try:
                    surface = ret_list(desc, f, surf1)[0]
                except:
                    surface = ''
                try:
                    plot = ret_list(desc, f, surf1)[1]
                except:
                    plot = ''
            num_of_entry = num_of_entry + 1
            mylist = [num_of_entry,title, dept, catg, typ, price[0], surface, plot, parti ,postal, datime, uid, link1]
            header = ['Num','Title', 'Department', 'Category', 'Type', 'Price', 'Surface Area', 'Plot Area','Particuliers/Professionelles', 'Postal Code',
                      'Date-time', 'User-id', 'Link']
            if terrain == 1:#if type is terrain, surface area will be empty
                if plot and surface:
                    mylist[7] = max(mylist[6], mylist[7])
                elif surface:
                    mylist[7]= mylist[6]
                mylist[6]=''

            print mylist[0], mylist[1], mylist[6], mylist[7],mylist[8]
            csvfile = "dataLAB.csv"
            with open(csvfile, 'a') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, dialect='excel', encoding='utf-8')
                if count == 1:
                    wr.writerow(header)
                    count = 0
                wr.writerow(mylist)
            time.sleep(random.uniform(random_time_delay[0], random_time_delay[1]))  # Random time sleep between 2 to 4 seconds
            terrain = 0

print '\n\n'+ str(num_of_entry) + '  entries Proccessed into CSV file.'


'''
TO Run THIS FILE, GO TO THE DIRECTORY THIS PYTHON FILE EXISTING IN, END THEN RUN THE COMMANT 'python <file-name> parameters'. Here file name is laboncoinFr.py.
The CSV FILE WILL BE STORED IN THE SAME DIRECTORY AS THIS FILE, NAMED 'dataLAB.csv'.
Perhaps you have to set the encoding of the csv file to "UTF_8" from MS excel.
because it would leave some shitty characters in place of french letters.

'''
