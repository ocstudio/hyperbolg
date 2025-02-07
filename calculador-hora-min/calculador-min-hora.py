def convertir_minutos_a_horas_minutos(minutos):
    """
    Convierte minutos a formato horas:minutos.
    
    Args:
        minutos (int): Cantidad total de minutos.
    
    Returns:
        tuple: (horas, minutos_restantes)
    """
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

# Interfaz interactiva para el usuario
while True:
    entrada = input("\nIngresa los minutos (o escribe 'salir' para terminar): ")
    
    if entrada.lower() == "salir":
        print("¡Hasta luego! 😊")
        break
    
    try:
        minutos = int(entrada)
        if minutos < 0:
            print("⚠️ ¡Error! Ingresa un número positivo.")
            continue
        
        horas, minutos_restantes = convertir_minutos_a_horas_minutos(minutos)
        
        # Formatea el resultado de manera elegante
        print(f"\n✅ {minutos} minutos equivalen a: {horas}h {minutos_restantes}min")
        print(f"   En formato decimal: {horas + minutos_restantes/60:.2f} horas")
    
    except ValueError:
        print("⚠️ ¡Error! Ingresa solo números enteros.")
