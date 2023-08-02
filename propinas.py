def calcular_propina():
    try:
        # Pedimos al usuario que ingrese el monto total de la cuenta y el porcentaje de propina.
        total_cuenta = float(input("Ingresa el monto total de la cuenta: "))
        porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dar (ejemplo: 10, 15, 20): "))

        # Verificamos que el porcentaje de propina sea un valor válido (mayor o igual a cero).
        if porcentaje_propina < 0:
            print("Error: El porcentaje de propina debe ser un valor mayor o igual a cero.")
            return

        # Calculamos el monto de la propina.
        propina = (total_cuenta * porcentaje_propina) / 100

        # Calculamos el monto total de la cuenta incluyendo la propina.
        total_con_propina = total_cuenta + propina

        # Mostramos los resultados al usuario.
        print(f"\nMonto de la propina: ${propina:.2f}")
        print(f"Monto total de la cuenta incluyendo la propina: ${total_con_propina:.2f}")

    except ValueError:
        print("Error: Ingresa un valor numérico válido para el monto total de la cuenta y el porcentaje de propina.")

if __name__ == "__main__":
    print("Calculadora de propinas")
    calcular_propina()
