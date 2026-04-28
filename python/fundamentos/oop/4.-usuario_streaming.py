
'''
Define la clase UsuarioStreaming, que debe incluir:

Atributos:
nombre
email
suscripcion (Gratis, Estándar o Premium)
lista_reproduccion (lista de títulos agregados por el usuario).
Métodos:
agregar_a_lista(self, titulo) agrega un contenido a la lista de reproducción.
ver_contenido(self, titulo) simula que el usuario reproduce un contenido.
cambiar_suscripcion(self, nueva_suscripcion) modifica el tipo de suscripción del usuario.
mostrar_info_usuario(self) muestra los datos del usuario y su lista de reproducción.
Realizar las siguientes pruebas con instancias:

Crea 3 usuarios de la plataforma de streaming.
Haz que el primer usuario agregue dos títulos a su lista y los vea.
Haz que el segundo usuario agregue un título, lo vea y cambie su suscripción.
Haz que el tercer usuario agregue tres títulos, los vea y cambie su suscripción dos veces.

'''


class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []


    def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
        self.lista_reproduccion.append(titulo)
        print(f"Usuario {self.lista_reproduccion}")
        pass


    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        pass


    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        pass


    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        pass

# Todos los valores que se deban registrar debe ser con input
# Añadir un menu While para llamar a los métodos
usuario1 = UsuarioStreaming("usuario123", "user123@gmail.com" )
usuario2 = UsuarioStreaming("usuario321", "user321@gmail.com" )
usuario3 = UsuarioStreaming("usuario12345", "user12345@gmail.com")


