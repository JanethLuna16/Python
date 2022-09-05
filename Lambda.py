import math


def area(radio):                                                        #Codigo para calcular el area de un circulo sin Lambda, (Sin Lambda se utilizan mas lineas de codigo
    print("Codigo sin Lambda")
    resultado = round(math.pi * radio * radio,3)
    print(resultado)
    
    
area(2)
print("Codigo Con Lambda")                                                #Codigo para calcular el area de un circulo con Lambda, (Con Lambda se utilizan menos  lineas de codigo
area= lambda radio: round(math.pi * radio * radio,3)
print(area(2))
