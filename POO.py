
class Paquetes:
    def __init__(self,nombre,fechaE,fechaS):
        self.nombre = nombre
        self.fechaE = fechaE
        self.fechaS = fechaS

    def muestra_datos(self):
        print("\t\t\t RESERVACION BASICA \n El nombre de la reservaacion es " + self.nombre,"\nFecha de entrada" ,self.fechaE,"\nFecha de salida",self.fechaS,"\n PAQUETE SOLO PARA UNA PERSONA")

nombre = str (input( "Ingresa nombre: "))
fechaE = str (input( "Ingresa fecha de entrada: "))
fechaS = str (input( "Ingresa fecha de salida:  "))

usuario1 = Paquetes(nombre,fechaE,fechaS)
usuario1.muestra_datos()


class Paquete2(Paquetes):
    def __init__(self,nombre,fechaE,fechaS,Personas):
        Paquetes.__init__(self, nombre,fechaE,fechaS)
        self.Personas = Personas


    def muestra_datos2(self):
        print("\t\t\tRESERVACION DIAMANTE \n El nombre de la reservaacion es " + self.nombre,"\nFecha de entrada" ,self.fechaE,"\nFecha de salida",self.fechaS,"\n Personas",self.Personas)


nombre = str (input( "Ingresa nombre: "))
fechaE = str (input( "Ingresa fecha de entrada: "))
fechaS = str (input( "Ingresa fecha de salida:  "))
Personas = str (input( "Ingresa Personas: "))


usuario2 = Paquete2(nombre,fechaE,fechaS,Personas)
usuario2.muestra_datos2()
