
comenzar = True

while comenzar:                                                     #El while se encargara de hacer el ciclo muentras que comenzar sea true, de lo contrario se saldrá del ciclo
    try:
        num1= int(input("Introduce un numero a sumar   "))          #Introducimos los dos numeros a sumas especificando numeros enteros (Int)
        num2 = int(input("Introduce otro numero para sumar  "))
    except ValueError:                                              #La excepcion funciona que si no te ingresaste algun numero entero, para no provocar error en todo el programa
        print("Introduce un numero entero\n\n  ")                   #solo aparece un mensaje mencionando dicho error
    else:                                                           #De lo contrario, si ingresaste el numero entero continuará con el ciclo while
        print("La suma es:  ",num1+num2)                            #resultado de la suma
    finally:                                                        #El bloque finally SIEMPRE se ejecutará haya errores o no 
        opc = input("Si desea seguir con la operacion presione S/N  ") #Si el usuario presiona N, la condicion comenzar se volverá falsa, por consiguiente se saldra del while
    if opc == "N":
        comenzar = False
    else:                                                              #Si el usuario presiona otra letra que no sea N, continuará con el programa
        print("Continuemos")