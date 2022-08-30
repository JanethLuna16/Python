
a_marinos  = {"Pez","Cocodrilo","Tiburon","Tortuga","Medusa","Rana","Anguila","Delfin","Focas" }
a_terrestres = {"Perro","Gato","Leon","Tigre","Mamut","Cocodrilo","Tortuga","Rana","Focas"}

print("\t\tEl conjunto de animales marinos contiene:\n\t\t ", a_marinos,"\n")
print("\t\tEl conjunto de animales terrestres contiene:\n\t\t ", a_terrestres,"\n")


conjunto = set()
a_marinos.update(["Tiburon ballena","Pez payaso"])
a_terrestres.discard ("Mamut")


print("\t\t\t Los elementos actualizado son \n")
print("\t\tAnimales marinos contiene:\n\t\t ", a_marinos,"\n")
print("\t\tAnimales terrestres contiene:\n \t\t", a_terrestres,"\n")


conjunto = a_marinos & a_terrestres
print("\t Los animales en comun de ambos conjuntos son:\n ","\t\t",conjunto)

conjunto = a_marinos - a_terrestres
print("\t \nLos elementos de Animales Marinos que no tiene Animales terrestres son: \n","\t\t",conjunto)
