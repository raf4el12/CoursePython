animal = "leon feliz"  
 
print(animal.upper())   #convierte to uppercase
print(animal.title())   #convierte la primera letra de cada palabra a mayúscula
print(animal.capitalize())  #convierte la primera letra de la cadena a mayúscula
print(animal.lower()) #convierte a minúsculas
print(animal.strip())  #elimina espacios al principio y al final
print(animal.replace("leon", "gato"))  #reemplaza "leon" por "gato"
print(animal.split())  #divide la cadena en una lista de palabras
print(animal.find("feliz"))  #encuentra la posición de "feliz
print(animal.startswith("leon"))  #verifica si la cadena comienza con "leon"
print(animal.endswith("feliz"))  #verifica si la cadena termina con "feliz"
print(animal.isalpha())  #verifica si todos los caracteres son alfabéticos
print(animal.isdigit())  #verifica si todos los caracteres son dígitos
print(animal.isalnum())  #verifica si todos los caracteres son alfanuméricos
print(animal.count("e"))  #cuenta cuántas veces aparece "e"
print(animal.index("feliz"))  #devuelve el índice de la primera aparición de "feliz"
print(animal.split(" "))  #divide la cadena en una lista usando espacio como separador
print(animal.join(["Hola ", "mundo"]))  #une la lista con la cadena como separador
print(animal.center(20, '*'))  #centra la cadena en un ancho de 20 caracteres, rellenando con '*'
print(animal.ljust(20, '-'))  #justifica la cadena a la izquierda