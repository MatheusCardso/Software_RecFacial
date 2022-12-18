import PySimpleGUI as sg

font = ('Helvetica', 10)
sg.theme("LightBlue5")
sg.set_options(font=font)

layout = [

    [sg.Text("Presentes",text_color="black",font=('Arial',25),pad=(160, 0))],
    [sg.Text("Aluno 1",font=('Helvetica',15),pad=(200, 0))],
    [sg.Text("Aluno 2",font=('Helvetica',15),pad=(200, 0))],
    [sg.Text("Aluno 3", font=('Helvetica', 15), pad=(200, 0))],
    [sg.Text("Aluno 4", font=('Helvetica', 15), pad=(200, 0))],
    [sg.Text("Aluno 5", font=('Helvetica', 15), pad=(200, 0))],
    [sg.Button("Voltar",pad=(210, 0), button_color="red")],

]

janela = sg.Window("Frequência", layout)

while True:
    evento,valores = janela.read()
    if evento == "Voltar":
        janela.hide()
        exec(open("./TelaHome.py").read())

    if evento == sg.WIN_CLOSED:
        break
janela.close()