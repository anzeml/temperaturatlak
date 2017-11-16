import sqlite3

#funkcije

con = sqlite3.connect('baze.db')
c = con.cursor()

def temperature():
    '''vrne seznam temperatur'''
    sez = list()
    for temp in con.execute('''
    SELECT *
    FROM temperatura
    '''):
        sez.append(temp)
    return sez

def tlaki():
    '''vrne seznam tlakov'''
    sez = list()
    for tlak in con.execute('''
    SELECT *
    FROM tlak
    '''):
        sez.append(tlak)
    return sez

def nova_temp(lokacija,vrednost,l,m,d):
    '''v bazo zapiše nov podatek o temperaturi'''
    try:
        c.execute("""
        INSERT INTO temperatura (Lokacija, Vrednost, Leto, Mesec, Dan) VALUES
        ('{0}',{1},{2},{3},{4})
        """.format(lokacija,int(vrednost),int(l),int(m),int(d)))
        con.commit()
    except:
        raise Exception('Napaka')

def nov_tlak(lokacija,vrednost,l,m,d):
    '''v bazo zapiše nov podatek o tlaku'''
    try:
        c.execute("""
        INSERT INTO tlak (Lokacija, Vrednost, Leto, Mesec, Dan) VALUES
        ('{0}',{1},{2},{3},{4})
        """.format(lokacija,int(vrednost),int(l),int(m),int(d)))
        con.commit()
    except:
        raise Exception('Napaka')

def povprecna_temp(kraj):
    '''vrne povprečnih temperatur za kraj'''
    for povprecje in con.execute('''
    SELECT ROUND(AVG(Vrednost),3)
    FROM Temperatura
    WHERE Lokacija = '{0}';
    '''.format(kraj)):        
        return povprecje[0]


def povprecni_tlak(kraj):
    '''vrne povprečni tlak za kraj'''
    for povprecje in con.execute('''
    SELECT ROUND(AVG(Vrednost),3)
    FROM Tlak
    WHERE Lokacija = '{0}';
    '''.format(kraj)):
        return povprecje[0]

def kraji():
    '''izpise kraje'''
    sez = list()
    for mesto in con.execute('''
    SELECT * from Kraji
    '''):
        sez.append(mesto[0])
    return sez

def vstavi_kraj(lokacija):
    '''vstavi lokacijo v tabelo krajev'''
    c.execute("""
    INSERT INTO Kraji (Lokacija) VALUES
    ('{0}')
    """.format(lokacija))
    con.commit()


def gostota_zraka(kraj):
    '''izračuna povprečno gostoto zraka glede ne meritve v kraju'''
    if povprecni_tlak(kraj) is None:
        return
    if povprecna_temp(kraj) is None:
        return
    tlak = povprecni_tlak(kraj) * 100 #pretvorim v pascale
    temperatura = povprecna_temp(kraj) + 273 # pretvorim v kelvine
    R = 287
    return tlak/(temperatura*R)



    








