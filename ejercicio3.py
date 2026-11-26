# Ejercicio 3 Distribucion del impuesto de viaje

# Entrada de datos
costo_t_trans = float(input("Cual es el costo total del transporte: "))
costo_t_hosp = float(input("Cual es el costo total del hospedaje: "))
costo_t_alim = float(input("Cual es el costo total de la alimentacion: "))
participantes = int(input("Cual es el numero de participantes: "))
cantidad_dias = int(input("Cual es la cantidad de dias: "))

# Procesos
costo_total = costo_t_trans + costo_t_hosp + costo_t_alim
costo_participante = costo_total / participantes
costo_dia_grupo = costo_total / cantidad_dias
costo_diario_personal = costo_dia_grupo / participantes

# Salida de datos
print(f"El costo total del viaje es de: {costo_total:.2f} colones")
print(f"El costo del viaje por persona es de: {costo_participante:.2f} colones")
print(f"El costo diario del grupo es de: {costo_dia_grupo:.2f} colones")
print(f"El costo diario por persona es de: {costo_diario_personal:.2f} colones")
