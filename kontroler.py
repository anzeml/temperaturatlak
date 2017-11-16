from bottle import route, run, template,static_file, get, post, request, redirect

import modeli

@route('/views/<filename>')
def server_static(filename):
    return static_file(filename, root='views/')

@route('/')
def index():
    return template('domaca')

@route('/temperature/')
def temperature():
    return template('temperature', podatki = modeli.temperature())

@route('/tlaki/')
def tlaki():
    return template('tlaki', podatki = modeli.tlaki())

@route('/vnesi/', method = 'GET')
def vnesi(napaka=False):
    return template('vnesi', napaka=False, dan='', nova_temp = '', kraj = '', mesec = '', leto = '')

@route('/vnesi/', method = 'POST')
def vnesi_post():
    kraj1 = request.forms.kraj
    kraji = modeli.kraji()
    if kraj1 not in kraji:
        modeli.vstavi_kraj(kraj1)
    nova_temp1 = request.forms.nova_temp
    dan1 = request.forms.dan
    mesec1 = request.forms.mesec
    leto1 = request.forms.leto
    try:
        modeli.nova_temp(kraj1,nova_temp1,leto1,mesec1,dan1)
    except:
        return template('vnesi', dan=dan1, nova_temp = nova_temp1, kraj = kraj1, mesec = mesec1, leto = leto1, napaka = True)
    redirect('/')

@route('/vnesi2/', method = 'GET')
def vnesi2(napaka=False):
    return template('vnesi2', napaka=False, dan='', nov_tlak = '', kraj = '', mesec = '', leto = '')

@route('/vnesi2/', method = 'POST')
def vnesi_post2():
    kraj1 = request.forms.kraj
    kraji = modeli.kraji()
    if kraj1 not in kraji:
        modeli.vstavi_kraj(kraj1)
    nov_tlak1 = request.forms.nov_tlak
    dan1 = request.forms.dan
    mesec1 = request.forms.mesec
    leto1 = request.forms.leto
    try:
        modeli.nov_tlak(kraj1,nov_tlak1,leto1,mesec1,dan1)
    except:
        return template('vnesi2', dan=dan1, nov_tlak = nov_tlak1, kraj = kraj1, mesec = mesec1, leto = leto1, napaka = True)
    redirect('/')

@route('/povprecje/')
def povprecje():
    kraji = modeli.kraji()
    print(kraji)
    sez = []
    for kraj in kraji:
        print(kraj)
        temp = modeli.povprecna_temp(kraj)
        print(temp)

        tlak = modeli.povprecni_tlak(kraj)
        print(tlak)

        gost = modeli.gostota_zraka(kraj)
        print(gost)

        sez.append((kraj, temp, tlak, gost))
    print(sez)
    return template('povprecje', podatki = sez)
    

run(debug = True)
