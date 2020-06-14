import cv2
import os
from os import walk, getcwd
import face_recognition
from visionrostros import *


def ls(ruta = '.'):
    dir, subdirs, archivos = next(walk(ruta))
    return subdirs

def Evento():
    ListaEventos = ls(ruta = "Eventos")
    path2 = "Eventos/"
    for a in ListaEventos:
        path2 = path2 + str(a)
        
        
def AbrirImagen():
    ListaPersonas = ls(ruta = "Personas")
    ListaEventos = ls(ruta = "Eventos")
    Obama = 0
    Daniel = 0
    Trump = 0
    Putin = 0
    DatosEventos = {}
    DatosPersonas = {}
    for a in ListaEventos:
        path = "Personas/"
        path2 = "Eventos/"
        evento = a
        evento1 = a
        evento2 = a
        evento3 = a
        numEventos = 0
        path2 = path2 + str(a)
        ArchEventos = ls2(path2)
        num = 0
        num1 = 0
        num2 = 0
        for b in ListaPersonas:
            path5 = path
            path = path + str(b)
            ArchPersonas = ls2(path)
            num = 0
            num1 = 0
            num2 = 0
            for c in ArchEventos:
                path4 = path2
                path2 = path2+ "/" + str(c)
                num = num + num1
                num1 = CrearArchivo(path2,path4)
                for d in ArchPersonas:
                        path3 = path
                        path = path+ "/" + str(d)
                        print(path)
                        
                        
                        known_image = face_recognition.load_image_file(path)
                        unknown_image = face_recognition.load_image_file(path2)
                        biden_encoding = face_recognition.face_encodings(known_image)[0]
                        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                        results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
                        
                        path = path3
                        if results[0]== True:
                            if(b == "Obama" and a == evento):
                                Obama = Obama + 1
                                evento = "1" 
                                
                                if Obama > 1:
                                    num1 = num1 - 1
                                break
                                
                            if(b == "Daniel" and evento1 == a):
                                Daniel = Daniel + 1
                                evento1 = "1"
                                
                                if Daniel > 1:
                                    num1 = num1 - 1
                                break
                                
                            if(b == "Trump" and evento2 == a):
                                Trump = Trump + 1
                                evento2 = "1" 
                                if Trump > 1:
                                    num1 = num1 - 1
                                break
                            
                            if(b == "Putin" and evento3 == a):
                                Putin = Putin + 1
                                evento3 = "1" 
                                if Putin > 1:
                                    num1 = num1 - 1
                                break
                path2 = path4
            path = path5
        DatosEventos[a] = num
    for a in ListaPersonas:
        if a == "Trump":
            DatosPersonas[a] = Trump 
        if a == "Obama":
            DatosPersonas[a] = Obama
        if a == "Daniel":
            DatosPersonas[a] = Daniel
        if a == "Putin":
            DatosPersonas[a] = Putin
    return DatosEventos,DatosPersonas

def RecorrerImagenes(NombreCarpeta):
    listaarchivos = []
    for dirpath, dirnames, filenames in os.walk(NombreCarpeta):
        listaarchivos.append(filenames)
    print(listaarchivos)
    return listaarchivos

def CrearArchivo(rutaImagen,directory):
    imagenAnalizar = cv2.imread(rutaImagen)
    [dataRostros, imagenesRostros] = detectarRostros(imagenAnalizar)
    rostros = crearRostros(imagenAnalizar, dataRostros,directory)
    return rostros
    
def ls2(ruta):
    dir, subdirs, archivos = next(walk(ruta))
    return archivos

def Datos(Personas,Eventos):
    c = len(Eventos)
    a = 0
    while True:
        print()
        Opciones = input("Digite 1 si quiere las estadisticas de las personas o digite 2 para eventos o 3 si quiere salir\n")
        if Opciones == "1":
            for key in Personas.keys():
                value = Personas[key]
                if a < value:
                    a = value
                print(str(key) + " asistio a un maximo de: " + str(a) + " Eventos")
                print("Con un Promedio de asistencia de: " + str(value/c))
                print()
            cont = 0
            a=0
        elif Opciones == "2":
                for key in Eventos.keys():
                    value = Eventos[key]
                    if a < value:
                        a = value
                    print(str(key) + " asistio a un maximo de: " + str(a) + " Personas")
                    print()
        elif Opciones == "3":
            print("Profe esto para mi es un 5, cierto que si? Nos vemos")
            break
        else:
            print("No reconozco el comando")
                    
        
        
    
    
    