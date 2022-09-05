
from tkinter import Y
from turtle import ycor


def suma(x,y):                                      #Funcion Con parametros y con retorno se muestra solo el retorno de la función pero fuera de la función tu le asignas losparametros que desees
    return x+y
total = suma (15,20)                                #Se asignan los parametros a la función
print ("Suma:\n",total)

def resta(x,y):                                     #Funcion Con parametros y sin retorno Se muestra a TODA la funcion, pero tu le asignas los parametros de cada variable
    print("Resta:\n",x-y)
resta(15,20)                                        #Se asignan los parametros a la función

def multi():                                        #Funcion sin parametros y sin retorno, cuando se llama a la función, se muestran TODA las instrucciones que esten dentro de ella
    a=15
    b=20
    print("Multiplicacion:\n" , a*b)
multi()                                             #Mandamos a llamar a la función en cualquier parte del programa

def div():                                           #Funcion sin parametros y con retorno, declaramos las variables y retorna SOLO el resultado cuando llamas la funcion
    a=15
    b=20
    return a/b

print("Division:\n", div())                         #Madamos a llamar a la función en cualquier parte del programa