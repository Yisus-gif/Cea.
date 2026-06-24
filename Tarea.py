# 1. Hola Mundo
print("1. Hola, mundo.")

# 2. Variables
nombre = "Jesus"
edad = 17
print("\n2. Nombre:", nombre, "- Edad:", edad)

# 3. Suma de dos números
print("\n3. Suma de dos números")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("La suma es:", num1 + num2)

# 4. Promedio
print("\n4. Promedio")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print("El promedio es:", promedio)

# 5. Número par o impar
print("\n5. Número par o impar")
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

# 6. Mayor o menor de edad
print("\n6. Condicional")
edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# 7. Bucle for
print("\n7. Números del 1 al 10")
for i in range(1, 11):
    print(i)

# 8. Tabla de multiplicar
print("\n8. Tabla de multiplicar")
tabla = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{tabla} x {i} = {tabla * i}")

# 9. Lista de frutas
print("\n9. Lista de frutas")
frutas = ["Manzana", "Banana", "Naranja", "Uva", "Mango"]
for fruta in frutas:
    print(fruta)

# 10. Función saludar
print("\n10. Función")
def saludar(nombre):
    print(f"Hola, {nombre}. Bienvenido a Python.")

nombre_usuario = input("Ingrese su nombre: ")
saludar(nombre_usuario)
