
from visionrostros import *
import cv2
import sys
from Metodos import *

# Valores de entrada
#ls2(ruta = "Personas/Obama")
#ls(ruta = "Personas")
#RecorrerImagenes("Personas/Obama")
print()
print("Realizando todo el entrenamiento desde 0, Por favor espere")
print()
Eventos,Personas = AbrirImagen()
Datos(Personas,Eventos)
#rutaImagen = input("Digite el nombre de la imagen que quiere analizar \n")
print()
#rutaImagen = sys.argv[1]
#imagenAnalizar = cv2.imread(rutaImagen)

#[dataRostros, imagenesRostros] = detectarRostros(imagenAnalizar) 

#verSubRostros(imagenesRostros)
#crearRostros(imagenAnalizar, dataRostros)
#verRostosImagen(imagenAnalizar, dataRostros)
