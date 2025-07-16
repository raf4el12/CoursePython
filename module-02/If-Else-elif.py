edad = int(input("Introduce tu edad: "))


if edad <= 90 and edad >= 50:
    print("Adultos mayores tienen un descuento del 50%")
elif edad > 90:
    print("Eres un adulto mayor longebo, tienes un descuento del 90%")
elif edad >= 18:
    print("Eres un adulto joven, tienes un descuento del 20%")
elif edad < 18 and edad >= 13:
    print("Eres un menor de edad, tienes un descuento del 10%")

else:
    print("Eres un niño, no tienes descuento")

print("Fin del programa")  # Mensaje final para indicar el fin del flujo de control

