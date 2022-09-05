
Lista=[ 10,"Hola",30,"Perro",50,"Ham","Ster",69]        #Crear Lista
print("\n", Lista)
print("La posicion 4 es : " , Lista [4])                #Mostrar el numero en la posición 4 (50)

print("\n La posicion -4 es :" ,Lista [-4])             #Mostrar el numero en la posicion -3 , contando de derecha a izquierda (50)

del(Lista[0])                                           #Eliminar elemento de la posicion 0 (10)
print("\n Elemento de la posicion 0 eliminado",Lista)   #Imprimir Lista con el dato eliminado

Lista.remove("Hola")                                    #Eliminar el elemento ingresando valor lit.
print("\n Elemento 'Hola' eliminado",Lista) 

Borrado=Lista.pop(1)                                    #Borrar el elemento  en la poscion 1 pero guardarlo a otra variable
print("\n", Lista) 
print(" El elemento 1 borrado de la lista es: "+ Borrado)

Lista.append(138)                                       #Con el método Append se agrega el 138 (Sin comillas porque es un numero) y
print("\n Elemento agregado al final de la lista \n", Lista) #Se añade al FINAL de la lista

Lista.insert(4,"Gato") 
print("\n Elemento agregado en la posicion 4 \n", Lista) #Con el metodo insert se añade un elemento en la posición que le asignes


print("\n Los caracteres de la lista son: ",len(Lista)) #Mostrar los caracteres de la lista
