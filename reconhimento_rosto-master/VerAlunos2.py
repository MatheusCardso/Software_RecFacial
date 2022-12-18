import PySimpleGUI as sg
font = ('Helvetica', 10)
sg.theme("LightBlue5")

sg.set_options(font=font)
a=[3,45,23,1,8,9]

sg.PopupScrolled(*a, title="Lista de alunos")
sg.Ok("voltar")