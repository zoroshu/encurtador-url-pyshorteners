import pyshorteners


url_base  = input("Insira a url que voce deseja ser encurtada aqui:")

encurtador = pyshorteners.Shortener()

url_encurtada = encurtador.tinyurl.short(url_base)

print(f"Sua url encurtada esta aqui: {url_encurtada}")
