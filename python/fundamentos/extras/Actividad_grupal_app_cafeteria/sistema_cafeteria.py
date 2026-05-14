'''
Clases e instancias.
Atributos de instancia.
Atributos de clase.
Métodos de instancia.
Métodos de clase (@classmethod).
Métodos estáticos (@staticmethod).
Validaciones con estructuras if.
Uso de self y cls
'''

'''
Cada cliente deberá tener:
nombre,
puntos acumulados,
saldo pendiente,
tipo de membresía.
Además, el sistema deberá:
registrar cuántos clientes existen,
permitir registrar compras,
permitir pagos,
validar membresías.

'''

class CafeteriaCliente:
    total_clientes = 0
    tipo_membresias = ["Bronce", "Plata", "Oro"]

    def __init__(self, nombre, puntos_acumulados, saldo_pendiente, membresia="Bronce"):
        
        self.nombre = nombre
        self.puntos_acumulados = puntos_acumulados
        self.saldo_pendiente = saldo_pendiente
        self.membresia = membresia
        CafeteriaCliente.total_clientes += 1
        

    def realizar_compra(self, monto):
    # TODO:
    # Aumentar saldo pendiente
        self.saldo_pendiente += monto
        agregar_compra = input("Quieres agregar alguna compra?(si/no)\n")
        if agregar_compra == "si":
            compra = int(input("Cuantas compras quieres agregar?\n"))
            for i in range(compra):
                valor_compra = int(input("Ingrese el valor de la compra?\n"))
                self.saldo_pendiente += valor_compra
        elif agregar_compra == "no":
            pass
        else:
            print("Error: Coloque si o no.")
    # TODO:
    # Aumentar puntos
        guardar_saldo = self.saldo_pendiente
        puntos = 10 * (self.saldo_pendiente // 1000)
        
        print(f"{guardar_saldo}")
        print(f"Se aumentaron esta cantidad de puntos: {puntos}")
        print(f"{self.nombre} realizó una compra.")

    def pagar_saldo(self, monto):
        # TODO:
        # Validar el pago
        self.saldo_pendiente += monto
        saldo = self.saldo_pendiente
        print(f"Tienes un saldo pendiente de {saldo}")
        pagar = int(input("Cuanto quieres pagar de tu saldo?\n"))
        pago = self.saldo_pendiente - pagar
        if pagar < self.saldo_pendiente:
            print(f"Tenias un saldo pendiente de: {saldo}\n y te queda un saldo pendiente de: {pago}")
        elif pagar > self.saldo_pendiente:
            print(f"Error: estas pagando más de lo que debes.")
    
    @classmethod
    def mostrar_total_clientes(cls):
        # TODO
        print(f"El total de clientes es {cls.total_clientes}")

    @staticmethod
    def validar_membresia(tipo):
    # TODO
        if tipo in CafeteriaCliente.tipo_membresias:
            return True
        else:
            return False





usuario1 = CafeteriaCliente("Pedro", 0, 0)
usuario2 = CafeteriaCliente("Daniel", 0, 0)
usuario3 = CafeteriaCliente("Juan", 0, 0)

CafeteriaCliente.mostrar_total_clientes()
#usuario1.realizar_compra(14000)
#usuario1.pagar_saldo(14000)



print(usuario1.validar_membresia("Bronce"))
print(usuario2.validar_membresia("Diamante"))
