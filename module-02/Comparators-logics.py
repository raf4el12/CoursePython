# Comparadores logicos

print (5 > 3)  # Mayor que # TRUE
print (5 < 3)  # Menor que $# FALSE
print (5 >= 3)  # Mayor o igual que # TRUE
print (5 <= 3)  # Menor o igual que # FALSE
print (5 == 3)  # Igual que # FALSE
print (5 != 3)  # Diferente de  # TRUE
print (5 > 3 and 3 < 2)  # Y lógico # FALSE
print (5 > 3 or 3 < 2)  # O lógico # TRUE
print (not(5 > 3))  # Negación lógica # FALSE
print (5 > 3 and 3 < 2 or not(5 == 3))  # Combinación de operadores lógicos # TRUE
print (5 > 3 and (3 < 2 or not(5 == 3)))  # Uso de paréntesis para controlar la precedencia # true
print (5 > 3 or (3 < 2 and not(5 == 3)))  # Uso de paréntesis para controlar la precedencia # true
print (5 > 3 and 3 < 2 or 5 == 3)  # Combinación de operadores lógicos con paréntesis # false

