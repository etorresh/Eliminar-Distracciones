import time
from datetime import datetime as dt
import sys, traceback, os

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirrecionar = "127.0.0.1"

# Convierte un texto separado por lineas a una lista
def texto_lista(archivo_txt):
    archivo = open(archivo_txt)
    lista = []
    for linea in archivo:
        linea = linea.replace("\n", "")
        lista.append(linea)
    return lista
# remplazar por .readlines()
    

# Recuerda: agregar extension a nombre del proceso
def matar_proceso(nombre_del_proceso):
    try:
        asesinado = os.system("taskkill /im " + nombre_del_proceso + " /f")
    except:
        asesinado = 0
    return asesinado
    
paginas_lista = texto_lista("bloquear_paginas.txt")
apps_lista = texto_lista("bloquear_apps.txt")

def activar():
    with open(hosts_path, "r+") as archivo:
        contenido = archivo.read()
        for pagina in paginas_lista:
            if pagina in contenido:
                pass
            else:
                archivo.write("\n" + redirrecionar + " " + pagina)
    for app in apps_lista:
        matar_proceso(app)

def desactivar():
    with open(hosts_path, "r+") as archivo:
        contenido = archivo.readlines()
        archivo.seek(0)
        for linea in contenido:
            if not any(pagina in linea for pagina in paginas_lista):
               archivo.write(linea) 
        archivo.truncate()
print("--------------------")
print("----MadreNodriza----")
print("--------------------\n")
while(True):
    opcion = input("0: Desactivar     1: Activar\n")
    if(opcion == "0"):
        desactivar()
    if(opcion == "1"):
        activar()
    time.sleep(1)

