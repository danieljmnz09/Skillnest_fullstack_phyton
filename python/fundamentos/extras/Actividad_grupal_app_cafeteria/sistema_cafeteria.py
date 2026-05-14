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
    
    def __init__(self, nombre, puntos_acumulados, saldo_pendiente, membresia="Bronce"):
        
        self.nombre = nombre
        self.puntos_acumulados = puntos_acumulados
        self.saldo_pendiente = saldo_pendiente
        self.membresia = membresia

    def registroCliente(self, usuario):
        pass

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
    # TODO:
    # Aumentar puntos
        self.saldo_pendiente // 1000
        self.saldo_pendiente * 10
        print(f"{self.saldo_pendiente}")
        print(f"{self.nombre} realizó una compra.")


usuario1 = CafeteriaCliente("Pedro", 0, 0)
usuario2 = CafeteriaCliente("Daniel", 0, 0)

usuario1.realizar_compra(14000)