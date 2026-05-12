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
    
    def __init__(self, nombre, puntos_acumulados = 0, saldo_pendiente = 0, membresia="Bronce"):
        
        self.nombre = nombre
        self.puntos_acumulados = puntos_acumulados
        self.saldo_pendiente = saldo_pendiente
        self.membresia = membresia

    def registroCliente(self, usuario):
        pass

    def realizar_compra(self, monto):
    # TODO:
    # Aumentar saldo pendiente
        total_pago = self.saldo_pendiente + monto
    # TODO:
    # Aumentar puntos
    
        print(f"{self.nombre} realizó una compra.")


usuario1 = CafeteriaCliente("Pedro")
usuario2 = CafeteriaCliente("Daniel")

usuario1.realizar_compra(14000)