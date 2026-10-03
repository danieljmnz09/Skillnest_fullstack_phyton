from jinja2 import Template

# 1. Creamos una plantilla de texto con variables {{ nombre }} y {{ curso }}
plantilla_texto = "¡Hola, {{ nombre }}! Bienvenido al curso de {{ curso }}."

# 2. Cargamos la plantilla en Jinja
template = Template(plantilla_texto)

# 3. Renderizamos pasando los datos reales
resultado = template.render(nombre="Floor", curso="Fullstack Python")

# 4. Imprimimos el resultado
print(resultado)