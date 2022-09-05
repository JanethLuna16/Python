#!/usr/bin/env phyton
# _*_ coding: cp1252 _*_           #Librerias para los acentos
# _*_ coding: 850 _*_
# _*_ coding: utf-8 _*_ 

tupla = ("Perro","Gato","Pez","Iguana","León",10,"El resultado de la resta es: ",100) #A diferencia de las listas, las tuplas no se pueden modificar,Permanecen como constantes
print("Tupla: \n ",tupla)

Lista= ["Manzana", "Pera","Fresa","Kiwi"]


print("\n El elemento en la posición 0 es: " +tupla [0])                                #Accedemos a la tupla de la posición 0

print("\n\tResta entre la posicón 6 y la posición 5 \n "+ tupla[6], tupla[5] - tupla[7]) #Se concatena un string con una resta de dos numeros que se encuntran en la tupla por posiciones

print("\n\nLista : \n", Lista)

tupla= tuple(Lista)                                                                     #Convertir una lista en tupla                                       
print ("Lista convertida en tupla: \n",tupla)
 
Lista=list(tupla)
print ("Tupla convertida en lista: \n",Lista)                                           #Convertir una tupla en lista 


 

