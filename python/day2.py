# Hay diferentes tipos de datos:
# Strings
# Int
# Float
# Boolean

#Posicion 0 del string
print("Hello"[0])

#Se puede mostrar el ultimo caracter con negativo
print("Hello"[-1])


#String de numeros
print("123" + "456")

#Los numeros son integer, se ponen sin comillas dobles
print(123 + 456)

#Para poner numeros con decimales se utiliza el data type float.
#Los boolean son true or false

#Para saber el tipo de dato, se puede utilizar type, pueden ser variables, strings...
print(type("Hello"))
print(type(123))
print(type(3.1415))
print(type(True))

#Transformar string to int
print(int("123") + int("456"))

print("Number of letters in your name: " + str(len(input("Enter your name"))))

#Operaciones
print(7 - 3)
print(3 * 2)
print(9 / 3) #Por defecto aparece en formato float, si se quiere solamente el entero se utilizan dos //

#Se puede usar round para redondear al entero mas proximo o al decimal que se quiere
print(round(3.1415,2))

#Se pueden convertir en strings todo lo de una frase y meter las variables dentro de las ""
print(f"El string entero {variable1} y tambien la {variable2}")
