#!/usr/bin/env phyton
# _*_ coding: cp1252 _*_           #Librerias para los acentos
# _*_ coding: 850 _*_
# _*_ coding: utf-8 _*_  

print("Saludos... ¿Que desea compar? \n "+              #Creación de lista
      "Objetos disponibles \n \n " + 
      "\t Espadas: \n " +
      "1- Espada niv 1: 50 pesitos\n " +
      "2-Espada niv 2: 120 pesitos \n"  +
      "3-Espada niv 3: 10000 pesitos \n\n "+
      "\tArmas de fuego \n"+
      "4-Pistola nivel 1: 1600 \n"+
      "5-pistola nivel supermo: 18500\n ")

comprar=[4]                                              #Se añade en las listas lo que ingresaste



                                                

dinero=2500                                             #Se igualan las variables a numeros para poder realizar la compra y se define un valor inicial de dinero
espadaniv1=50
espadaniv2=120
espadaniv3=1000
pisniv1=1600
pisniv2=18500

if 0 in comprar or comprar==[]:
    print("Numero incorrecto, especifica un numero entre 1-5")    #Si hay un numero incorrecto o no introduces un numero, te manda un mensaje de error

if 1 in comprar:                                                  #Si el numero 1 esta en la lista, al dinero inicial se le resta el valor del primer articulo
    dinero=dinero - espadaniv1

if 2 in comprar:
    dinero=dinero - espadaniv2                                    #Si el numero 2 esta en la lista, al dinero inicial se le resta el valor del segundo articulo

if 3 in comprar:
    dinero=dinero - espadaniv3                                    #Si el numero 3 esta en la lista, al dinero inicial se le resta el valor del tercer articulo

if 4 in comprar:
    dinero=dinero - pisniv1                                       ##Si el numero 4 esta en la lista, al dinero inicial se le resta el valor del cuarto articulo

if 5 in comprar:                                                  #Si el numero 5 esta en la lista, al dinero inicial se le resta el valor del quinto articulo
    dinero=dinero - pisniv2

else:
    print("Numero incorrecto, especifica un numero entre el 1-5")

if dinero <0 :                                                         #Si el dinero es menor a 0, entonces ya no se pueden hacer compras
    print ("No hay suficiente dinero para realizar la compra")

if comprar ==[1] or comprar==[2] or comprar==[3] or comprar==[4] or comprar==[5]:      #Impresion de dinero restante 
        print("Te quedan  ", dinero,"pesos")
        print("Se añadieron los objetos a tu inventario")
