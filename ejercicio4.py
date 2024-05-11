#Escribe un programa que solicite al usuario un número entero y calcule si es divisible por 3 y por 5.
numero = int(input("INGRESE UN NUMERO ENTERTO: "))

if numero%3==0 and numero%5==0:
    print("El numero",numero,("es divisible por 3 y por 5"))  
elif numero%3==0:
    print("El numero",numero,("es divisible solo por 3"))
elif numero%5==0:         
    print("El numero",numero,("es divisible solo por 5"))
else:
    print("El numero",numero,("no es divisible ni por 3 ni por 5"))
