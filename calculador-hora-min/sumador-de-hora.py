def sumar_tiempos():
    total_horas = 0
    total_minutos = 0

    print("\n🕒 ** Sumador de Tiempos en Horas:Minutos ** 🕒")
    print("Instrucciones:")
    print("- Ingresa los tiempos en formato hh:mm (ejemplo: 2:30 = 2 horas y 30 minutos)")
    print("- Escribe 'fin' para calcular el resultado\n")

    while True:
        entrada = input("▶ Ingresa un tiempo (hh:mm): ")
        
        if entrada.lower() == "fin":
            break
        
        try:
            # Validar formato y convertir a números
            if ":" not in entrada:
                raise ValueError("Formato incorrecto. Usa hh:mm.")
            
            horas_str, minutos_str = entrada.split(":")
            horas = int(horas_str)
            minutos = int(minutos_str)
            
            if horas < 0 or minutos < 0 or minutos >= 60:
                raise ValueError("Horas deben ser ≥ 0 | Minutos entre 0-59")
            
            # Acumular valores
            total_horas += horas
            total_minutos += minutos
        
        except ValueError as e:
            print(f"⚠️ Error: {e}")
            continue

    # Convertir minutos acumulados a horas extras
    horas_extra = total_minutos // 60
    minutos_restantes = total_minutos % 60
    total_horas += horas_extra

    # Resultado en dos formatos
    horas_decimal = total_horas + (minutos_restantes / 60)

    print("\n✅ ** Resultado Final **")
    print(f"Formato hh:mm ➡ {total_horas:02d}:{minutos_restantes:02d}")
    print(f"Horas decimales ➡ {horas_decimal:.2f} horas")

if __name__ == "__main__":
    sumar_tiempos()
