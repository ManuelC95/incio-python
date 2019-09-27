import json
def cargar_datos(ruta):
  with open(ruta) as contenido:
      resultado = json.load(contenido)
      print(resultado)
#with se pone porque no se sabe cuan grande sera el archivo a leer      

if __name__ == '__main__':
    ruta = 'data/curso.json'
    cargar_datos(ruta)