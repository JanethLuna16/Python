#!/usr/bin/env phyton
# _*_ coding: cp1252 _*_           #Librerias para los acentos
# _*_ coding: 850 _*_
# _*_ coding: utf-8 _*_  

Perros = {                                                                          #Creamos un diccionario Maestro, donde aqui contiene dos diccionarios mas

"Perro1" : {
    "Raza de perro" :"Chihuaha"   ,                                                 #Creamos dos diccionarios con diferentes datos dentro del             
    "Nombre" : "Poqui",                                                             #Diccionario Principal
    "Edad":"10 años",
    "Color":"Café claro"
    } ,

"Perro2" : {
    "Raza de perro" :"Chihuaha"   , 
    "Nombre" : "Canelo",
    "Edad":"1 año",
    "Color":"Café"
    }

}

print("El diccionario Perros cuenta con  : " ,len(Perros),"Perros disponibles")             #Metodos len para contar los diccionarios que contiene el principal, pero no cuenta los elemntos que contiene
print("Los perros disponibles son: \n\n")                                                   #cada sub-diccionario
for x,y in Perros["Perro1"].items():                                                        #Muestra de forma ordenada los elementos de los sub-diccionarios
    print(x,":",y)
print("\n\n")
for x,y in Perros["Perro2"].items():
    print(x,":",y)

res= int(input("Desea eliminar algun registro de Perrito ?\n Seleccione 1 para si, de lo contrario presione cualquier tecla     "))   #Codigo con una condicional para eliminar sub-diccionarios que contiene el diccionario principal, si no desea eliminar alguno se termina ejecución
if res == 1:
    cat = int(input("Seleccione numero de  Perro quiere eliminar:\n"+"1-Perro 1\n"+ "2-Perro 2 \n"))
    if cat == 1:
            del Perros["Perro1"]
    if cat == 2:
        del Perros["Perro2"]

    print("La actualización de registro es  : \n ",Perros)                                  #Impresion de Diccionario principal solo en caso que se haya eliminado algun elemento.

else:
    print("Gracias:)")
