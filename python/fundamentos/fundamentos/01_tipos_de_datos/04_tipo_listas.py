'''
Actividad Gestor de inventario

1.- Creacion: Crear una lista llamada inventario que contenga los siguientes
articulos: "laptop", "teclado", "raton", "monitor", "cable hdmi" 
'''

inventario = ["laptop", "teclado", "raton", "monitor", "cable hdmi"]


'''2.- Expansion: Utiliza el metodo correspondiente para agregar "impresora" y "teclado" al final de la lista '''

inventario.append("impresora")
inventario.append("teclado")



'''3.- Conteo utiliza la funcion integrada para mostrar cuantos elementos totales hay en la lista. '''

print(len(inventario))



'''4.- Acceso y modificacion: Modifica "teclado" por "teclado mecanico" '''

inventario[1]= "teclado mecanico"



'''5.- Slicing: Crea una nueva lista llamada "promocion", debe contener solo los 3 primeros elementos de la lista "inventario". '''

promocion = ["teclado", "raton", "monitor"]



'''6.- Mostrar la lista de inventario ordenado alfabeticamente. '''

inventario.sort()
print(inventario)



'''7.- Elimina el ultimo elemento de la lista inventario mostrando el elemento eliminado y la lista final '''

elemento_eliminado = inventario.pop()
print("Elemento_eliminado", elemento_eliminado)


