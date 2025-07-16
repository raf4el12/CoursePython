# operadores logicos

# and, or, not

gas = True
encendido = True
edad = 17

if gas and encendido:
    print("Hay fuego")
else:
    print("No hay fuego")

if gas or encendido:
    print("Hay gas o fuego")
else:
    print("No hay gas ni fuego")

if gas and (encendido or edad > 18): # lo que hace el paréntesis es que primero se evalúe la condición dentro de él
    print("Puedes avanzar")
else:
    print("No puedes avanzar")


# operatores lógicos con negación
if not gas or encendido or edad < 18:
    print("No hay gas")