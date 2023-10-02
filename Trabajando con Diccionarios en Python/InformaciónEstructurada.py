# Crear un diccionario llamado informacion_personal.
informacion_personal = {
    "Nombre": "Gabriela López",
    "Edad": 30,
    "Ciudad": "Puyo",
    "Profesion": "Licenciada"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo.
informacion_personal["Ciudad"] = "Ambato"

# Agregar una nueva clave-valor al diccionario.
informacion_personal["Telefono"] = "0993767263"

# Verificar si la clave "telefono" existe y agregarla si no existe.
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0993767263"

# Eliminar la clave "edad" del diccionario.
if "Edad" in informacion_personal:
    del informacion_personal["Edad"]

# Imprimir el diccionario final
print(informacion_personal)
