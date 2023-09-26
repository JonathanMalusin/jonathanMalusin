# Definimos la función calcular_descuento.
def calcular_descuento(monto_total, porcentaje_descuento=12):
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento

# Llamada a la función con un monto total de compra.
monto_compra_1 = 100
descuento_1 = calcular_descuento(monto_compra_1)

# Llamada a la función con un monto total de compra y porcentaje de descuento.
monto_compra_2 = 150
porcentaje_descuento_2 = 50
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)

# Impresión de los resultados.
print(f"Una compra de ${monto_compra_1}, el descuento es de ${descuento_1}, y el monto final a pagar es de ${monto_compra_1 - descuento_1}")
print(f"Una compra de ${monto_compra_2} con un descuento del {porcentaje_descuento_2}%, el descuento es de ${descuento_2}, y el monto final a pagar es de ${monto_compra_2 - descuento_2}")
