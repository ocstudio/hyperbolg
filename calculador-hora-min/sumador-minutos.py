def sumar_minutos():
    total_minutos = 0

    print("\n⏱️ ** Sumador de Minutos a Horas:Minutos ** ⏱️")
    print("Instrucciones:")
    print("- Ingresa cantidades de minutos (ejemplo: 90 = 1 hora y 30 minutos)")
    print("- Escribe 'fin' para calcular el resultado\n")

    while True:
        entrada = input("▶ Ingresa minutos: ")
        
        if entrada.lower() == "fin":
            break
        
        try:
            minutos = int(entrada)
            if minutos < 0:
                print("⚠️ Error: Ingresa números positivos.")
                continue
            
            total_minutos += minutos
            print(f"   ➕ Total acumulado: {total_minutos} minutos")
        
        except ValueError:
            print("⚠️ Error: Ingresa solo números enteros.")

    # Convertir a horas y minutos
    horas = total_minutos // 60
    minutos_restantes = total_minutos % 60
    horas_decimal = total_minutos / 60

    print("\n✅ ** Resultado Final **")
    print(f"Total de minutos ingresados: {total_minutos} min")
    print(f"Formato hh:mm ➡ {horas:02d}:{minutos_restantes:02d}")
    print(f"Horas decimales ➡ {horas_decimal:.2f} horas")

if __name__ == "__main__":
    sumar_minutos()
