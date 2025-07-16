# While

numero = 6

while numero <= 10:
    print(numero, numero * "hola mundo ")
    numero += 1

# lo que hace while es que se repita el bloque de código mientras la condición sea verdadera
# cuando la condición se vuelve falsa, el bucle termina

# otro ejemplo

comando = ""
while comando.lower() != "salir":
    comando = input("$ Escribe un comando (escribe 'salir' para terminar): ")
    print(f"Comando recibido: {comando}")


# otro ejemplo con break
numero = 0
while True:
    numero += 1
    if numero == 5:
        print("Número alcanzado, saliendo del bucle.")
        break
    print(f"Número actual: {numero}")