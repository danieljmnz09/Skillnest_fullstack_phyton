#Pasar argumentos 
#Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al método __init__ y que de esta manera podamos asignarle a los atributos los valores correspondientes.

class Usuario:
    def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar

#Creacion de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la",10000,0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 50000,200000)
jimenez = Usuario("Jimenez", "Bates", "jimenezbates@gmail.com", 3000, 200)

#Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel

#-------------------

# Tarea rápida

'''
Crear una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
- Crear 3 instancias para la clase con distintos estudiantes.
- Imprimir el nombre y apellido concatenado + especialidad.

'''

# Funcion y creacion de atributos para la instancia
class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

#Instancia
Dario = Estudiante("28493693-0", "Dario", "Jimenez", "Contabilidad", "03-04-1994")
Pedro = Estudiante("24304576-0", "Pedro", "Gonzalez", "Recursos Humanos", "04-02-1992")
Amalia = Estudiante("2049532-0", "Amalia", "Vera", "Programacion", "09-14-2009")

#Imprimir valores
print(f"Hola me llamo {Dario.nombre} {Dario.apellido} y soy de la especialidad de {Dario.especialidad}")
print(f"Hola me llamo {Pedro.nombre} {Pedro.apellido} y soy de la especialidad de {Pedro.especialidad}")
print(f"Hola me llamo {Amalia.nombre} {Amalia.apellido} y soy de la especialidad de {Amalia.especialidad}")
