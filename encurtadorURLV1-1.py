import pyshorteners
import PySimpleGUI as sg
import webbrowser

# Funçao para encurtar a url

def encurtar_url(url):
    try:
        encurtador = pyshorteners.Shortener()
        return encurtador.tinyurl.short(url)
    except Exception as e:
        return f"Erro ao encurtar url: {e}"
    
# Definindo o tema da aplicacao
sg.theme('Dark')

# Definindo o layout da janela, inputs e botões 

layout = [
    [sg.Text("Digite aqui a URL a ser encurtada:")],
    [sg.Input(key="url")],
    [sg.Button("Encurtar",button_color='grey')],
    [sg.Text("URL ENCURTADA: ", visible=False, key = "LBL_URL")],
    [sg.Input("" , key = "SHORT_URL", visible= False)],
    [sg.Button("Copiar Link", key="COPY_BTN",button_color="grey", visible=False), sg.Button("Abrir Link", key="OPN_BTN", button_color="grey", visible=False)]
]

janela = sg.Window("Encurtador de Links V1.1",layout)


while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED:
        break
    if evento == "Encurtar":
        url_base = valores["url"]
        if url_base:
            url_encurtada = encurtar_url(url_base)
            janela["SHORT_URL"].update(url_encurtada, visible = True)
            janela["LBL_URL"].update(visible = True)
            janela["COPY_BTN"].update(visible = True)
            janela["OPN_BTN"].update(visible = True)
        else:
            sg.popup("Insira uma URL Válida", title= "ERRO", button_color="grey")
    if evento == "COPY_BTN":
        sg.clipboard_set(valores["SHORT_URL"])
        sg.popup("Link copiado!", button_color="grey")
    if evento == "OPN_BTN":
         webbrowser.open(valores["SHORT_URL"])

# Fecha a janela

janela.close()