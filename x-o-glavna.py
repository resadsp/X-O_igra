import PySimpleGUI as sg
import game_window

layout = [
            [sg.Text("Unesite ime prvog takmicara:", size=(25,1)), sg.Input(key='_X_', do_not_clear=True, size=(20, 1))], #mora biti popunjeno polje
            [sg.Text("Unesite ime drugog takmicara: ", size=(25,1)), sg.Input(key='_O_', do_not_clear=True, size=(20, 1))], #mora biti popunjeno polje
            [sg.Button('Igraj', size=(15,1)), sg.Button('Izadji', size=(15,1))]
        ]

window = sg.Window('IKS-OKS', layout, icon=('./x-o.ico'))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Izadji'): #sg.WIN_CLOSED - x na datom prozoru
        break
    elif event == 'Igraj':
        players = [values['_O_'], values['_X_']] # niz napravljen od imena iz inputa na osnovu kljuca. [0] poz. - drugi takmicar, [1] poz. - prvi takmicar
        game_window.zapocni_igru(players) #zapocni igru i prosledi niz sa imenima takmicara kao parametar
window.close()