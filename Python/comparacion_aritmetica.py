# Comparación entre funciones aritméticas

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

def realizar_operacion(a, b, operacion):
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        return a / b if b != 0 else "Error: División por cero"
    else:
        return "Operación no válida"

def main():
    operaciones = ['+', '-', '*', '/']
    print("Operaciones disponibles:", ', '.join(operaciones))
    
    operacion = input("Elija una operación: ")
    while operacion not in operaciones:
        operacion = input("Operación no válida. Elija una operación: ")

    resultado1 = realizar_operacion(
        obtener_numero("Ingrese el primer número para la primera operación: "),
        obtener_numero("Ingrese el segundo número para la primera operación: "),
        operacion
    )

    resultado2 = realizar_operacion(
        obtener_numero("Ingrese el primer número para la segunda operación: "),
        obtener_numero("Ingrese el segundo número para la segunda operación: "),
        operacion
    )

    print(f'El resultado de la primera operación es: {resultado1}')
    print(f'El resultado de la segunda operación es: {resultado2}')

    if isinstance(resultado1, str) or isinstance(resultado2, str):
        print("No se puede comparar debido a un error en una de las operaciones.")
    elif resultado1 > resultado2:
        print('El resultado de la primera operación es mayor.')
    elif resultado1 < resultado2:
        print('El resultado de la segunda operación es mayor.')
    else:
        print('Ambos resultados son iguales.')

if __name__ == "__main__":
    main()
