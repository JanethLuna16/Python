


import datetime, locale
from pydoc import locate
import re
#!/usr/bin/env phyton
# _*_ coding: cp1252 _*_           #Librerias para los acentos
# _*_ coding: 850 _*_
# _*_ coding: utf-8 _*_  

print("LA FECHA ACTUAL ES:\n")
locale.setlocale(locale.LC_ALL,"es-Es")
fecha = datetime.datetime.now()

print(fecha.strftime("%c"))

texto=str(input("\n Ingrese una oracion   "))
letra=str(input("Ingresa letra a buscar   "))
busqueda = re.findall(letra,texto)
print(busqueda)

eliminar=str (input ("\nIngrese la oracion que quiera eliminar de la oracion principal:   "))
eliminado = re.split(eliminar,texto)

print("\n\tLa oracion es :",eliminado)

update =str (input ("\nIngrese la oracion que quiera reemplazar  en la oracion principal:  "))
actualizar = re.sub(eliminar,update,texto)

print("\n\tLa oracion es final es :",actualizar)