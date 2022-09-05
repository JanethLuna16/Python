
Lista = [1,5,2]
Lista2= [2,4,2]                                     #Creacion de las listas, con numeros enteros para realizar operaciones aritmeticas
Lista3= [1,2,2]

for x in Lista:                                     #Recorre primero la posición X, ejecutando todos  los  fors ( Y y z) ,para despúes continuar con X
    #print("La suma es de ", x,"+")
    for y in Lista2:                                #Como segundo paso recorre la posición Y ejecutando todos los fors de Z, para despues continuar con su ejecución
        for z in Lista3:                            #Como for final, ejecuta todas sus instrucciones 
            print( "La suma es ",x,"+",y ,"+",z)    #Imprimen las variables que se estan sumando
            print("\n Resultado: ", x+y+z,"\n")     #Imprime Resultado
            
