import PySimpleGUI as sg

sg.theme('DarkBlue3')

def provera_pobednika(tabla):   
    for kolone in range(0, 3):
        if ((0,kolone) in tabla.keys()) and ((1, kolone) in tabla.keys()) and ((2, kolone) in tabla.keys()): #ako je popunjena kolona, pristupi elemntima matrice preko indeksa i u if pelji ispod ispitaj da li je sadrzaj jednak u koloni
            if tabla[(0, kolone)] == tabla[(1, kolone)] == tabla[(2, kolone)]: #pristupamo sadrzaju matrice, da li imamo 3 jednaka znaka u istom redu
                print(tabla[0,kolone])
                return tabla[(0, kolone)] #vraca 0 ili 1 zavisi do sadrzaja u jednom redu tj sta je isto x ili o
    
    for redovi in range(0, 3):
        if ((redovi, 0) in tabla.keys()) and ((redovi, 1) in tabla.keys()) and ((redovi, 2) in tabla.keys()):
            if tabla[(redovi, 0)] == tabla[(redovi, 1)] == tabla[(redovi, 2)]:
                return tabla[(redovi, 0)] #vraca 1 ili 0. ako je xxx vraca 1 ako je ooo vraca 0

    if ((0,0) in tabla.keys()) and ((1,1) in tabla.keys()) and ((2,2) in tabla.keys()):
        if tabla[(0,0)] == tabla[(1,1)] == tabla[(2,2)]:
            return tabla[(1,1)] #vraca 1 ili 0. xxx 1, ooo 0. GLAVNA DIJAGONALA

    if ((2,0) in tabla.keys()) and ((1,1) in tabla.keys()) and ((0,2) in tabla.keys()):
        if tabla[(2,0)] == tabla[(1,1)] == tabla[(0,2)]:
            return tabla[(2, 0)] #vraca 1 ili 0. xxx 1, ooo 0. SPOREDNA DIJAGONALA   

def zapocni_igru(players):
    tabla = {} #tabla pamti kombinacije i smesta ih u dict
    player = 1 #player je x, jer je tako dato u glavnom dokumentu
    layout = [[sg.Text('Trenutni igrac: ' + players[player], key='_TRENUTNI_', size=(16,1))]]
    for redovi in range(3):
        new_redovi = []
        for kolone in range(3):
            new_redovi.append(sg.Button(size=(3, 2), key=(redovi, kolone)))
        layout.append(new_redovi)
    layout.append([sg.Button('Resetuj'), sg.Button('Izadji')])

    window = sg.Window('IKS-OKS', layout, icon=('./x-o.ico'))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Izadji':
            break
        
        if event == 'Resetuj':
            tabla = {}
            for redovi in range(3):
                for kolone in range(3):
                    window[(redovi, kolone)].update('') #isprazni cijelu matricu

        elif event not in tabla:
            tabla[event] = player #tu gde pritisnes neka bude x ili o zavisi da li je takmicar 0 ili 1
            window[event].update('X' if player else 'O') #ako je player 0 update o, ako je player 1 update x
            pobednik = provera_pobednika(tabla)
            if pobednik is not None:
                sg.popup("Pobednik je: "+ players[player])
                break
            player = (player + 1) % 2 #da se stalno menja 0 i 1 igrac.
            window['_TRENUTNI_'].update('Trenutni igrac: '+ players[player])

    window.close()
    
    """  kolone
       --|---|-- red
       --|---|-- red
       --|---|-- red
        kolone
    """