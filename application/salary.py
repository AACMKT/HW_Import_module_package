import PySimpleGUI as sg
import time
Q_list = ['Have you ever seen employee you are asking for in the office?',
          'Does employee know the name of the company he is working for?',
          'Can employee speak person to pearson without feeling panic?',
          'Does employee aware that working hours are scheduled?',
          'Does employee know that even if he works from home, working hours term is still applicable?',
          'Has employee ever completed assigned work on time?']


def calculate_salary(questions):
    layout1 = [[sg.Text('To calculate a salary for employee, please answer a few questions first',
                        size=(36, 2), expand_x=True, text_color='black',
                        background_color='white', border_width=1,  key='-counter-')],
               [sg.Text(questions[0], size=(36, 2), expand_x=True, text_color='black',
                        background_color='white', border_width=1, visible=False,  key='-question-')],
               [sg.Button('OK', size=(8, 1), visible=True, enable_events=True, key='-button_yes-'),
                sg.Button('NO', size=(8, 1), visible=False, enable_events=True, key='-button_no-'),
                sg.Text(size=16, key='-plug-'),
                sg.Button('Exit', size=(8, 1), key='-Exit-')]]

    window = sg.Window('Salary calculator', layout1)

    i = 0
    c_start = time.time()
    counter = 400
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Quit') or 'Exit' in event:
            break

        if event == '-button_yes-' and window['-button_yes-'].get_text() == 'OK':
            event = None
            window['-question-'].update(questions[0], visible=True)
            window['-button_yes-'].update('YES')
            window['-Exit-'].update(visible=False)
            window['-plug-'].update(visible=False)
            window['-button_no-'].update(visible=True)
            window['-plug-'].update(visible=True)
            window['-Exit-'].update(visible=True)
            window['-counter-'].update(f'Current salary counter result is: {counter} Euro',
                                       background_color=sg.DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR)
            window['-plug-'].set_size((6, 1))

        if ('-button_yes-' or '-button_no-' in event) and window['-button_yes-'].get_text() == 'YES':
            if i < len(questions):
                window['-question-'].update(questions[i])
                i += 1
                if event == '-button_yes-':
                    counter += 100
                elif event == '-button_no-':
                    counter -= 50
                window['-counter-'].update(f'Current salary counter result is: {counter} Euro')

            else:
                c_stop = time.time()
                window['-question-'].update(
                    f"Thanks for spending {round(c_stop - c_start,0)} seconds on this ridiculous activity.")
                window['-button_yes-'].update(visible=False)
                window['-button_no-'].update(visible=False)
                window['-plug-'].set_size((26, 1))


if __name__ == '__main__':
    calculate_salary(Q_list)