# Creacion de la clase usuario - Entidad
class Usuario:
    def __init__(self): #Constructor
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0
        
#Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
dany = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.apellido) #Imprime: Nariyoshi
print(miyagi.email) 
print(daniel.limite_credito) 
print(miyagi.saldo_pagar) 

#Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@email.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000
print(daniel.nombre) # Imprime: Daniel

#Valores a nueva instancia
dany.nombre = "Dany"
dany.apellido = "Hernandez"
dany.email = "dany@gmail.com"
dany.limite_credito = 1000
dany.saldo_pagar = 20000

#Imprimir numbre de cada instancia
print(miyagi.nombre)
print(daniel.nombre)
print(dany.nombre)

