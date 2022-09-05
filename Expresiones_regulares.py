


import datetime, locale
from pydoc import locate
import re
#!/usr/bin/env phyton
# _*_ coding: cp1252 _*_           #Librerias para los acentos
# _*_ coding: 850 _*_
# _*_ coding: utf-8 _*_  

print("LA FECHA ACTUAL ES:\n")                          #Codigo oara la impresion de fecha actual
locale.setlocale(locale.LC_ALL,"es-Es")
fecha = datetime.datetime.now()

print(fecha.strftime("%c"))                           #Impresion de fecha

texto=str(input("\n Ingrese una oracion   "))       #Ingresar una oración
letra=str(input("Ingresa letra a buscar   "))       #Letra que desees buscar en la oración
busqueda = re.findall(letra,texto)                  #Te muestra las letras encontradas en la oracioon
print(busqueda)

eliminar=str (input ("\nIngrese la palabra que quiera eliminar de la oracion principal:   "))    #Se ingresa una oración para despues eliminarla de la oracion principal
eliminado = re.split(eliminar,texto)

print("\n\tLa oracion es :",eliminado)

update =str (input ("\nIngrese la oracion que quiera reemplazar  en la oracion principal:  "))   #Metodo para actualizar y escribir una nueva palabra a reemplazar
actualizar = re.sub(eliminar,update,texto)

print("\n\tLa oracion es final es :",actualizar)
