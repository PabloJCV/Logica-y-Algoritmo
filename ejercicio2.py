#Ejercicio 2 costo de impresion de materiales

# Entrada de datos
cant_afiches = int(input("Cuantos afiches desea imprimir: "))
precio_imp_afiches = float(input("Precio de impresion de los afiches: "))
cant_volantes = int(input("Cuantos volantes desea imprimir: "))
precio_imp_volantes = float(input("Precio de impresion de los volantes: "))
porc_impuesto = float(input("Porcentaje de Impuesto: "))

# Procesos
costo_afiches = cant_afiches * precio_imp_afiches
costo_volantes = cant_volantes * precio_imp_volantes
subtotal = costo_afiches + costo_volantes
impuesto = subtotal * porc_impuesto
total = subtotal + impuesto

# Salida de datos
print(f"El costo total de los afiches es de: {costo_afiches:.2f} colones")
print(f"El costo total de los volantes es de: {costo_volantes:.2f} colones")
print(f"El subtotal es de: {subtotal:.2f} colones")
print(f"El impuesto es de: {impuesto:.2f} colones")
print(f"El total a pagar es de: {total:.2f} colones")
