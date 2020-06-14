'''
Para instalar la libreria cv2 debe ejecutar:
>> pip install opencv-python
>> pip install opencv-contrib-python
más información en OpenCV https://pypi.org/project/opencv-python/
'''
Numero = 0
#from Metodos import ls
import cv2
from os import walk, getcwd
import os
import os.path
            
#Función que realiza la segmentación de rostros
def detectarRostros(imagenAnalizar):
    # Crear el reconocedor haar cascade
    '''
    Una cascada de Haar es un clasificador que se utiliza para
    detectar el objeto para el que ha sido entrenado
    '''
    entrenamiento = "haarcascade_frontalface_default.xml"
    clasificadorRostros = cv2.CascadeClassifier(entrenamiento)
    imagenGris = cv2.cvtColor(imagenAnalizar, cv2.COLOR_BGR2GRAY)

    # Rostros detectados imagenAnalizar
    rostros = clasificadorRostros.detectMultiScale(
        imagenGris,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    imagenesRostros = []
    for (x, y, w, h) in rostros:
        ROI = imagenAnalizar[y:y+h, x:x+w]
        imagenesRostros.append(ROI)

    return [rostros, imagenesRostros]

#==========================================================
# función que genera archivos de imagenes por cada rostro identificado

def crearRostros(imagenAnalizar, rostros, directory):
    ROI_number = 0
    cont = 0
    for (x, y, w, h) in rostros:
        ROI = imagenAnalizar[y:y+h, x:x+w]
       # cv2.imwrite(os.path.join(directory ,'ROI_{}.png'.format(ROI_number)), ROI)
        ROI_number += 1
        cont += 1
   # print("{} archivos creados...".format(len(rostros)))
    return cont
    #print(directory)
    
#=================================================================
#función que muestra los rostos identificados
def verRostosImagen(imagenAnalizar, rostros):
    print("Encontrado {0} rostros en la imagen!".format(len(rostros)))

    #dibuja un rectangulo al rededor del rostro
    #color = (255,0,0) #BGR: azul
    color = (0,255,0) #BGR: verde
    #color = (0,0,255) #BGR: rojo
    grosor = 2

    for (x, y, w, h) in rostros:
        cv2.rectangle(imagenAnalizar, (x, y), (x+w, y+h), color, grosor)

    cv2.imshow("rostros encontrado", imagenAnalizar)
    print ("[esc] en la imagen para salir...")
    cv2.waitKey(0)

#===========================================================0
# función que ver rostro por rostro (muestra 4 en este ejemplo)
def verSubRostros(imagenesRostros):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    #para instalar: pip install matplotlib

    fig = plt.figure()

    a = fig.add_subplot(2, 2, 1)
    a.set_title('Rostro 1')
    imgplot = plt.imshow(imagenesRostros[0])

    a = fig.add_subplot(2, 2, 2)
    a.set_title('Rostro 2')
    imgplot = plt.imshow(imagenesRostros[1])

    a = fig.add_subplot(2, 2, 3)
    a.set_title('Rostro 3')
    imgplot = plt.imshow(imagenesRostros[3])

    a = fig.add_subplot(2, 2, 4)
    a.set_title('Rostro 4')
    imgplot = plt.imshow(imagenesRostros[4])
    plt.show()
    

