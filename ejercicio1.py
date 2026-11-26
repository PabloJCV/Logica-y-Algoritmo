# Ejercicio 1, Preparacion de una receta

# Entrada de datos
personas = int(input("¿Para cuántas personas desea cocinar? "))

arroz_original = float(input("Gramos de arroz para 4 personas: "))
carne_original = float(input("Gramos de carne para 4 personas: "))
salsa_original = float(input("Mililitros de salsa para 4 personas: "))

# Proceso: calcular factor de ajuste
factor = personas / 4

# Calcular nuevas cantidades
arroz = arroz_original * factor
carne = carne_original * factor
salsa = salsa_original * factor

# Mostrar resultados
print("\n--- Cantidades necesarias ---")
print(f"Arroz: {arroz:.2f} gramos")
print(f"Carne: {carne:.2f} gramos")
print(f"Salsa: {salsa:.2f} mililitros")