###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("Nombre: Felipe Clavijo", "Ciudad: Bogotá", sep="\n")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))  # int
print(type(b))  # float
print(type(c))  # str
print(type(d))  # bool
print(type(e))  # NoneType

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
string = "12345"
integer = int(string)  # Convierte la cadena a entero
print(f"Cadena a entero: {integer}")  # Imprime el entero
print(f"Entero a float: {float(integer)}")  # Imprime el float
print(f"Float 3.99 a entero: {int(3.99)}")  # Convierte el float a entero, truncando la parte decimal

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
nombre = "Felipe Clavijo"
edad = 32
altura = 1.63
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
pi = 3.14159  # Asignamos el valor de PI a una variable
pi_redondeado = round(pi)  # Redondeamos el número PI
print(f"PI redondeado: {pi_redondeado} ", f"PI redondeado // 2: {pi_redondeado // 2}", sep="\n")  # División entera entre el número redondeado y 2