# recorrer con for

for i in range(4):
    print(i, i * "hola mundo ")

# for con else

buscar = int(input("Que numero desea buscar:"))

for numero in range(2):
    if numero == buscar:
        print("Encontre el numero", buscar)
        break
else:
    print("No encontre el numero", buscar)


# iterables

for char in "hola mundo":
    print(char)