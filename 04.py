#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros) 
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla 
#  frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal 
# calculado redondeado con dos decimales.


print("hola bienvenido, que bueno verte de nuevo")
print("----------------------------------------------------------------------------")
kilogramo = float(input("¿Cuál es tu peso? (en kg): "))
estatura = float(input("¿Cuál es tu estatura? (en metros, usa punto para decimales): "))
imc = kilogramo / (estatura ** 2)
print("Tu índice de masa corporal es: " + str(round(imc, 2)) + " kg/m²")

while True:
    respuesta = input("¿Quieres calcular otro IMC? (s/n): ")
    if respuesta.lower() == 's':
        kilogramo = float(input("¿Cuál es tu peso? (en kg): "))
        estatura = float(input("¿Cuál es tu estatura? (en metros, usa punto para decimales): "))
        imc = kilogramo / (estatura ** 2)
        print("Tu índice de masa corporal es: " + str(round(imc, 2)) + " kg/m²")
    elif respuesta.lower() == 'n':
        print("Gracias por usar el programa.")
        break
    else:
        print("Respuesta no válida. Por favor, ingresa 's' o 'n'.")
