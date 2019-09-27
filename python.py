import json
def cargar_datos(ruta):
  with open(ruta) as contenido:
      resultado = json.load(contenido)
      for rl in resultado:
         print(rl.get('nombre'))
        # print(rl.get('duracion', ''))# si no tiene duracion retorna un string vacio
#with se pone porque no se sabe cuan grande sera el archivo a leer      

if __name__ == '__main__':
    ruta = 'data/curso.json'
    cargar_datos(ruta)