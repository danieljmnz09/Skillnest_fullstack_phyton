class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        """Reduce el saldo pendiente según el monto pagado."""
        self.saldo_pendiente -= monto
        if self.saldo_pendiente < 0:
            self.saldo_pendiente = 0
        print(f"{self.usuario} pagó ${monto}")

    def cambiar_suscripcion(self, nuevo_tipo):
        """Cambia el tipo de suscripción y actualiza el costo mensual."""
        if nuevo_tipo in self.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
            self.saldo_pendiente = self.costo_mensual
            print(f"{self.usuario} cambió a suscripción {nuevo_tipo}")
        else:
            print("Tipo de suscripción no válido")

    def ver_contenido_exclusivo(self):
        """Permite ver contenido exclusivo según el tipo de suscripción."""
        if self.tipo_suscripcion == "Premium":
            print("Puedes ver contenido exclusivo Premium")
        elif self.tipo_suscripcion == "Estándar":
            print("Puedes ver contenido estándar")
        else:
            print("La cuenta Gratis no tiene contenido exclusivo")

    def mostrar_info_suscripcion(self):
        """Muestra la información de la suscripción del usuario."""
        print("------ INFORMACIÓN ------")
        print(f"Usuario: {self.usuario}")
        print(f"Tipo: {self.tipo_suscripcion}")
        print(f"Costo mensual: ${self.costo_mensual}")
        print(f"Saldo pendiente: ${self.saldo_pendiente}")
        print("-------------------------")

usu1 = SuscripcionStreaming("Daniel")
usu2 = SuscripcionStreaming("Jesus", "Premium")
usu3 = SuscripcionStreaming("Zárate", "Estándar")

print("=== User1 ===")
usu1.mostrar_info_suscripcion()

print("\n=== User2 ===")
usu2.mostrar_info_suscripcion()

print("\n=== User3 ===")
usu3.mostrar_info_suscripcion()

print("\n=== User2 ===")
usu2.realizar_pago(5)
usu2.mostrar_info_suscripcion()

usu3.ver_contenido_exclusivo()

usu1.cambiar_suscripcion("Premium")
usu1.mostrar_info_suscripcion()