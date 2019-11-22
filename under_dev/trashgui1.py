import PySimpleGUI as sg

def TFTGUI():

    sg.change_look_and_feel('Reddit')

    layout = [[sg.Text('TFT Bot', size=(40, 1))],
              [sg.Output(size=(127, 25), font=('Helvetica 10'))],
              [sg.Text('Enter the champion that you purchased: '),
               sg.Text('', size=(20, 3), key='history')],
              [sg.ML(size=(85, 5), enter_submits=True, key='query', do_not_clear=True),
               sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
               sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

    window = sg.Window('TFT Plugin', layout,
                       default_element_size=(30, 1),
                       no_titlebar=False,
                       resizable=True,
                       grab_anywhere=True,
                       font=('Helvetica', ' 13'),
                       default_button_element_size=(8, 2),
                       return_keyboard_events=True)

    # ---===--- Loop taking in user input and using it  --- #
    command_history = []
    history_offset = 0

    while True:
        event, value = window.read()

        if event == 'SEND':
            query = value['query'].rstrip()
            # EXECUTE YOUR COMMAND HERE
            print('You entered {}'.format(query))
            command_history.append(query)
            history_offset = len(command_history)-1
            # manually clear input because keyboard events blocks clear
            window['query'].update('')
            window['history'].update('\n'.join(command_history[-3:]))
        
        elif event in (None, 'EXIT'):            # quit if exit event or X
            break
        


TFTGUI()