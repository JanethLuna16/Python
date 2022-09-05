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
    print("Numero incorrecto, especifica un numero entre 1-5")

if 1 in comprar:
    dinero=dinero - espadaniv1

if 2 in comprar:
    dinero=dinero - espadaniv2

if 3 in comprar:
    dinero=dinero - espadaniv3

if 4 in comprar:
    dinero=dinero - pisniv1

if 5 in comprar:
    dinero=dinero - pisniv2

else:
    print("Numero incorrecto, especifica un numero entre el 1-5")

if dinero <0 :
    print ("No hay suficiente dinero para realizar la compra")

if comprar ==[1] or comprar==[2] or comprar==[3] or comprar==[4] or comprar==[5]:
        print("Te quedan  ", dinero,"pesos")
        print("Se añadieron los objetos a tu inventario")