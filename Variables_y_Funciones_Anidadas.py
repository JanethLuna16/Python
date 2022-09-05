
def local():
    variable1 = "Variable local"
    global variable2 
    variable2 ="Conversion de variable local a global"
    print(variable1)

    def anidada():
        variable1 = "Variable local anidada en una funcion"
        print(variable1)
   
    anidada()

local()
variable_global = "Variable global"
print(variable_global)
print(variable2)