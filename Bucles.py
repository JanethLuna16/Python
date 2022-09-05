
a=5                                     #Se inicializa la variable A =5

while a<15:                             #El buble se realiza hasta que a sea menor a 15
    a+=1
    if(a==12 or a==13 or a==14):        #Si a llega el valor de 12,13 o 14 , no los imprime y continua con el while
        continue
    print(a)                            #Impresion de variable fuera del if


print("Bucle terminado")                


