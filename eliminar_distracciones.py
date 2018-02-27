import time
import logging
from datetime import datetime as dt
import sys, traceback, os
from tkinter import *
import subprocess


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
    

# Recuerda: agregar extension a nombre del proceso
def matar_proceso(nombre_del_proceso):
    aseinado = subprocess.run("taskkill /im " + nombre_del_proceso + " /f", stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    
# Consigue las paginas y apps por bloquear
paginas_lista = texto_lista("bloquear_paginas.txt")
apps_lista = texto_lista("bloquear_apps.txt")

# Bloquea paginas y cierra apps
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

# Desbloquea paginas
def desactivar():
    with open(hosts_path, "r+") as archivo:
        contenido = archivo.readlines()
        archivo.seek(0)
        for linea in contenido:
            if not any(pagina in linea for pagina in paginas_lista):
               archivo.write(linea) 
        archivo.truncate()

# GUI control
def boton_control():
    if b1["text"] == "Activar":
        activar()
        b1["text"] = "Desactivar"
    else:
        desactivar()
        b1["text"] = "Activar"
# GUI
ventana = Tk()
ventana.geometry("75x75+1791+933")


b1 = Button(text = "Activar", height= 2, width = 8, fg="white", bg="grey", command = boton_control)
b1.place(relx=0.5, rely=0.5, anchor=CENTER)


ventana.mainloop()
