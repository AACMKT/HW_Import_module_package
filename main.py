from application.salary import calculate_salary, Q_list
from application.db.people import get_employees as get_talents

import certifi as certifi
import PySimpleGUI as sg
from datetime import date as d, datetime as dt


from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, EarthLocation
from astropy.coordinates import get_body
file_path = 'application/db/staff.json'

date_today = d.today()
print(f'Текуща дата: {date_today:%d.%m.%Y}')


def track_celestial_body(object_of_choice: str):
    certifi.where()
    t = Time(dt.now())
    loc = EarthLocation.of_site('greenwich')
    with solar_system_ephemeris.set('builtin'):
        space_body = get_body(object_of_choice.lower(), t, loc)
    return space_body


def main_menu():

    layout0 = [[sg.Button('Calculate salary', size=(15, 1), enable_events=True, key='-salary-')],
               [sg.Button('Get employees list', size=(15, 1), enable_events=True, key='-employees-')],
               [sg.Button('Get celestial body position', size=(15, 2), enable_events=True, key='-celestial-')],
               [sg.Button('Exit', size=(15, 1), key='-Exit_main-')]]
    layout1 = [[sg.Listbox(values=['Mercury', 'Venus', 'Earth', 'Moon', 'Mars', 'Jupiter', 'Saturn',
                                   'Uranus', 'Neptune', 'Pluto'], key='-listbox-', enable_events=True, size=(42, 3))],
               [sg.Text(key='-object-', size=(38, 6), expand_x=True, text_color='black',
                        background_color='white', border_width=1)],
               [sg.Button('Confirm', size=(15, 1), disabled=True, key='-confirm-'),
                sg.Button('Exit', size=(8, 1), key='-Exit_celestial-')]]

    layout = [[sg.Column(layout0, key='-Main_menu-'),
              sg.Column(layout1, visible=False, key='-Planets_data-')]]

    window1 = sg.Window('MENU', layout)

    while True:
        event, values = window1.read()

        if event in (sg.WIN_CLOSED, 'Quit') or 'Exit' in event:
            break

        if event == '-salary-':
            window1.close()
            calculate_salary(Q_list)
            break

        if event == '-employees-':
            window1.close()
            sg.popup(*get_talents(file_path), title='EMPLOYEES')
            break

        if event == '-celestial-':
            window1['-Main_menu-'].update(visible=False)
            window1['-Planets_data-'].update(visible=True)

        if event == '-listbox-':
            window1['-confirm-'].update(disabled=False)

        if event == '-confirm-':
            val = track_celestial_body(str(values['-listbox-'][0]))
            # val = str(values['-listbox-'][0])
            window1['-object-'].update(val)


if __name__ == '__main__':
    main_menu()
    # get_talents(file_path)
    # calculate_salary(Q_list)
