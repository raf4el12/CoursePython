    # esta aplicacion tiene que verificar si nosotros ya hemos ingresado un numero antes, en el caso que no
    # el usuario tiene que ingresar un numero
    # si el numero ya fue ingresado, entonces se tiene que pedir al usuario que ingrese una operacion
    # despues de ingresar la operacion otra vez pedir que ingrese otro numero
    # y como resultado final mostrar el resultado de la operacion


def calculadora_interactiva():
    numero_anterior = None  # Variable para almacenar el número ingresado previamente

    print("Bienvenido a la calculadora interactiva")
    print("Para salir, escribe 'salir' en cualquier momento.")
    print("Operaciones disponibles: +, -, *, /, %")

    while True:
        if numero_anterior is None:
            
            entrada = input("Ingresa un número: ").lower()
            if entrada == 'salir':
                break
            try:
                numero_anterior = float(entrada)
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número válido.")
                continue
        else:
            
            operacion = input(f"Ingresa una operación (+, -, *, /, %) o 'salir': ").lower()
            if operacion == 'salir':
                break
            if operacion not in ['+', '-', '*', '/', '%']:
                print("Operación inválida. Por favor, elige entre +, -, *, /, %.")
                continue

            
            entrada_siguiente_numero = input(f"Ingresa el siguiente número para {operacion} {numero_anterior}: ").lower()
            if entrada_siguiente_numero == 'salir':
                break
            try:
                siguiente_numero = float(entrada_siguiente_numero)
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número válido.")
                continue

            resultado = None
            if operacion == '+':
                resultado = numero_anterior + siguiente_numero
            elif operacion == '-':
                resultado = numero_anterior - siguiente_numero
            elif operacion == '*':
                resultado = numero_anterior * siguiente_numero
            elif operacion == '/':
                if siguiente_numero == 0:
                    print("Error: No se puede dividir por cero.")
                    
                    continue
                resultado = numero_anterior / siguiente_numero
            elif operacion == '%':
                if siguiente_numero == 0:
                    print("Error: No se puede calcular el módulo con cero.")
                    continue
                resultado = numero_anterior % siguiente_numero

            print(f"El resultado de {numero_anterior} {operacion} {siguiente_numero} es: {resultado}")
            
            numero_anterior = resultado

    print("¡Gracias por usar la calculadora!")

# Ejecutar la calculadora función
calculadora_interactiva()