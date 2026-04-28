class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

    def aumentarCredito(self, aumento):    
        self.limite_credito += aumento

miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")
Jose = Usuario("Jose", "Gutierrez", "jose@gmail.com")

miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre}: ${miyagi.saldo_pagar}")
segundaCompra = 300
miyagi.hacer_compra(segundaCompra)
print(f"Segunda compra: ${miyagi.saldo_pagar}")
#Imprimir cuanto credito le queda  a Miyagi
print(f"Credito disponible ${segundaCompra - miyagi.saldo_pagar}")
print(miyagi.saldo_pagar) #Imprime: 350

#Compras Daniel 2 compras y muestra sueldo a pagar
print("------------------ Compras de Daniel --------------------")
daniel.hacer_compra(1000)
print(f"Primera compra de {daniel.nombre}: ${daniel.saldo_pagar}")
segunda_Compra = 400
daniel.hacer_compra(segundaCompra)
print(f"Segunda compra de {daniel.nombre}: ${daniel.saldo_pagar}")
#Cuanto credito le queda a Daniel
print(f"Credito disponible: ${segundaCompra - miyagi.saldo_pagar}")
print(miyagi.saldo_pagar) 
daniel.hacer_compra(45)
print(daniel.saldo_pagar) #Imprime: 45

'''
1.- Crear un nuevo método que permita aumentar el límite

'''
'''

2.- Crear un método que permita cambiar el correo de la instancia.
Mostrar el nuevo correo.

'''
Jose.aumentarCredito(800)
print


