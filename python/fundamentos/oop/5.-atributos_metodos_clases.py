#Atributos, métodos de clase, métodos estáticos

##DEFINICION DE LA CLASE
class Estudiante:
    #Atributo de clase
    colegio = "Liceo Vate Vicente Huidobro"
    #Lista en donde esten todos los estudiantes 
    estudiantes = []
    #Metodo CONSTRUCTOR
    def __init__(self, nombre, nota):
        #Atributos de instancia
        self.nombre = nombre
        self.nota = nota

        #Agregar elementos a la lista Estudiante (objeto)
        Estudiante.estudiantes.append(self)


#Metodo de instancia
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota {self.nota}")

#Metodo de CLASE
# Usa "CLS" porque trabaja con la informacion de la clase
    @classmethod
    def cambiar_colegio(cls, nuevo_nombre):
        cls.colegio = nuevo_nombre
    @classmethod #Contar la cantidad de estudiantes existentes
    def cantidad_estudiantes(cls):
        return len(cls.estudiantes)

#Metodo estatico
#Este no usa CLS ni SELF, solo parametros

    @staticmethod
    def aprobar(nota):
        if nota >= 4.0:
            return True
        else:
            return False
    
#Creacion de Objetos(Instancias)
e1 = Estudiante("Daniel", 5.0)
e2 = Estudiante("Randy", 5.9)
e3 = Estudiante("Marcelo", 3.9)

# Uso de métodos de instancia
print("== METODOS DE INSTANCIA==")
#Mostrar datos de estudiante
e1.mostrar_info()
print()
e2.mostrar_info()
print()

#Usar atributo de clase
print("== METODO DE INSTANCIA ==")
print(e1.colegio)
print(e2.colegio)
print()

#Uso metodo de clase
print("== METODO DE INSTANCIA")

Estudiante.cambiar_colegio("Purkuyen")
print(e1.colegio)
print(e2.colegio)
print()

#Contar Estudiantes
print("== CONTAR ESTUDIANTES ==")
print(f"Total estudiantes: {Estudiante.cantidad_estudiantes()}")

# Uso de metodo de clase
print("== METODO DE CLASE ==")

Estudiante.cambiar_colegio("Purkuyen")
e1.colegio = "VVH" #Modifica el atributo de la instancia en la clase
print(e1.colegio)
print(e2.colegio)
print()


#Metodo estatico
print("== METODO ESTATICO ==")
print(f"¿{e1.nombre} Aprueba?")
print(Estudiante.aprobar(e1.nota))
print()

print(f"¿{e2.nombre} Aprueba?")
print(Estudiante.aprobar(e3.nota))
print()

print(f"¿{e3.nombre} Aprueba?")
print(Estudiante.aprobar(e3.nota))
print()

## Funcion repaso
## Crear una funcion que valide usuario y contraseña
def validador(user, password):
    if user == "matias123" and password == "matias123":
        print(f"Bienvenido, {user}!")
        return True
    else:
        print("Acceso Denegado")
        return False
    
def enviarDatos():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    validator = validador(username, password)

enviarDatos()