import math


def area(radio):
    print("Codigo sin Lambda")
    resultado = round(math.pi * radio * radio,3)
    print(resultado)
    
    
area(2)
print("Codigo Con Lambda")
area= lambda radio: round(math.pi * radio * radio,3)
print(area(2))
