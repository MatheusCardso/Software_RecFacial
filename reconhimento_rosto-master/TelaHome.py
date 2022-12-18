import PySimpleGUI as sg

font = ('Helvetica', 20)
sg.theme("LightBlue5")
sg.set_options(font=font)

layout = [

    [sg.Text("",pad=(600, 60))],
    [sg.Image(filename="./img/camera.png",pad=(185, 0)),sg.Image(filename="./img/aluno.png",pad=(135, 0))],
    [sg.Button("Fazer Chamada",pad=(210, 0), button_color="Blue"),sg.Button("Lista de Alunos",pad=(150, 0), button_color="green")],
    [sg.Text("",pad=(0, 60))],
    [sg.Button("Sair",pad=(550, 0), button_color="red")],


]

janela = sg.Window("Home", layout)

while True:
    evento,valores = janela.read()
    if evento == "Fazer Chamada":
        exec(open("./webcam.py").read())

    if evento == "Lista de Alunos":
        exec(open("VerAlunos2.py").read())
        #exec(open("./VerAlunos1.py").read())

    if evento == sg.WIN_CLOSED or evento == "Sair":
        break

janela.close()