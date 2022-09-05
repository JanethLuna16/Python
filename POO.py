
class Paquetes:                                 #Creación de clase padre ,podemos usar los atributos en clases hijos
    def __init__(self,nombre,fechaE,fechaS):        # funcion con parametros de nombre,fecha de entrada y fecha de salida
        self.nombre = nombre
        self.fechaE = fechaE                       #El .self funciona para mandar a llamar las variables en otras clases y pode pasarle parametros
        self.fechaS = fechaS

    def muestra_datos(self):                        #Funcion para impresion de datos
        print("\t\t\t RESERVACION BASICA \n El nombre de la reservaacion es " + self.nombre,"\nFecha de entrada" ,self.fechaE,"\nFecha de salida",self.fechaS,"\n PAQUETE SOLO PARA UNA PERSONA")

nombre = str (input( "Ingresa nombre: "))              #Variables para que el ususario llene los datos
fechaE = str (input( "Ingresa fecha de entrada: "))
fechaS = str (input( "Ingresa fecha de salida:  "))

usuario1 = Paquetes(nombre,fechaE,fechaS) #Pasar los parametros a la clase
usuario1.muestra_datos()                #Llamar a la función para mostrar datos


class Paquete2(Paquetes):                               #Creacion de padre hijo
    def __init__(self,nombre,fechaE,fechaS,Personas):     #Funcion con parametros  
        Paquetes.__init__(self, nombre,fechaE,fechaS)     
        self.Personas = Personas


    def muestra_datos2(self):     #Funcion para mostrar los datos
        print("\t\t\tRESERVACION DIAMANTE \n El nombre de la reservaacion es " + self.nombre,"\nFecha de entrada" ,self.fechaE,"\nFecha de salida",self.fechaS,"\n Personas",self.Personas)


nombre = str (input( "Ingresa nombre: "))                           #Variablespara que el usuario llene sus datos y poder pasar parametros a las funciones dentro de las clases 
fechaE = str (input( "Ingresa fecha de entrada: "))
fechaS = str (input( "Ingresa fecha de salida:  "))
Personas = str (input( "Ingresa Personas: "))


usuario2 = Paquete2(nombre,fechaE,fechaS,Personas)
usuario2.muestra_datos2()
