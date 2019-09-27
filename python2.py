import json
def carga(ruta):
    with open(ruta) as conte:
        resultado = json.load(conte)
        print(resultado)

ruta= "data/curso.json"
carga(ruta)