
def local():                                                    #Funcion para demostración de las variables local, solo se pueden utilizar dentro de la funcion 
    variable1 = "Variable local"
    global variable2                                            #Conversion de una variable local a una variable global
    variable2 ="Conversion de variable local a global"
    print(variable1)

    def anidada():                                              #Variable local anidada dentro de otra función
        variable1 = "Variable local anidada en una funcion"
        print(variable1)
   
    anidada()                                                   #Dentro de la función se manda a llamar la función anidada

local()                                                         #Llamar a la fuunción principal para poder imprirmir las variables que esta contiene
variable_global = "Variable global"                             #Creación de una variable global, se puede utilizar el todo el programa
print(variable_global)
print(variable2)
