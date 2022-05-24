import PySimpleGUI as sg
from util import csv_data

class fileWindowLayout:
    def create_layout(self, data, headings, dictionary):

        sg.theme('SystemDefault')
        sg.set_options(font=('Arial', 13))
        headings = headings
        d_value = data

        header = [
            sg.Text('Visualizador de Datos', font=('Arial', 25),
            justification='center')
        ]

        data_table = [
            sg.Table(
                values=d_value, headings=headings, 
                size=(30,20), max_col_width=25,
                justification='center', auto_size_columns=True,
                expand_x=True, expand_y=True,
                text_color='black', enable_events=True,
                # row_colors=((0,"red"),(2,"yellow")),
                alternating_row_color=sg.theme_button_color('lightgrey')[1],
                key="-DATA TABLE-"
            )
        ]

        combobox_value = ["No Selection"]
        combobox_value.extend(headings)
        print(f"executing: {combobox_value}")


        filer_selection = [
            [sg.Text('', enable_events=True, key="-FILTER STATUS-")],
            [
                sg.Text('Filtrar por:'),
                sg.Combo(
                    combobox_value, 
                    enable_events=True, key="-FILTER-"
                    ),
                sg.Text('Mostrar solo: ', visible=False, key="-SHOW ONLY-"),
                sg.Combo(
                    [], 
                    size=(25,1),
                    enable_events=True, visible=False, 
                    key="-SHOW COMBOBOX-"
                    ),
                # sg.In(size=(25,1), enable_events=True, key="-FILTER-"),
                sg.Text('')
            ],
            [
                sg.Text('Buscar en:'),
                sg.Combo(
                    headings, enable_events=True,
                    key="-SEARCH FILTER-"
                ),
                sg.Input(size=(25,1), enable_events=True, key="-SEARCH-"),
                sg.Text(
                    '', enable_events=True, visible=False, 
                    key="-SEARCH RESULT TEXT-"
                    ),
                sg.Button('Search', button_color='royal blue'),
                sg.Button('Reset', size=(5,1), button_color='black')
            ],
        ]

        layout = [
            header,
            data_table,
            filer_selection,
        ]

        return layout