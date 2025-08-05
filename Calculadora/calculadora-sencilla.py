def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Error: División entre cero"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Error: División entre cero"
    return a % b

def sumar_tres_numeros(a, b, c):
    return a + b + c

def operaciones_complejas():
    expresion = input("Escribe una operación con 3 o más números: ")
    try:
        resultado = eval(expresion)
        return resultado
    except Exception as e:
        return f"Error en la expresión: {e}"
    
def calculadora():
    print("Bienvenido a la calculadora sencilla")
    while True:
        print("\nOperaciones disponibles:")
        print("0. Salir")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Módulo")
        print("6. Sumar tres números")
        print("7. Operaciones complejas")
    
        opcion = input("Ingresa el número de la operación que deseas realizar: ")
        
        if opcion == "0":
            print("Saliendo de la calculadora.")
            break
        
        elif opcion == "1":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {sumar(a, b)}")
        elif opcion == "2":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {restar(a, b)}")
        elif opcion == "3":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", multiplicar(a, b))
        elif opcion == "4":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", dividir(a, b))
        elif opcion == "5":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", modulo(a, b))
        elif opcion == "6":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            c = float(input("Tercer número: "))
            print("Resultado:", sumar_tres_numeros(a, b, c))
        elif opcion == "7":
            print("Resultado:", operaciones_complejas())
        else:
            print("Opción no válida.")

calculadora()