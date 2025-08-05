
input("Hola prueba")

def operaciones_complejas():
    expresion = input("Escribe la operación que quieras realizar: ")
    try:
        resultado = eval(expresion)
        if isinstance(resultado, (int, float)):
            return f"Resultado: {resultado:.2f}"
        return resultado
    except Exception as e:
        return f"Error en la expresión: {e}"

def isiteven(num):
    return "Verdadero" if num % 2 == 0 else "Falso"

def isintaninteger(num):
    return "Verdadero" if isinstance(num, int) else "Falso"

def calculadora():
    print("Bienvenido a la calculadora sencilla")
    while True:
        print("\nOperaciones disponibles:")
        print("0. Salir")
        print("1. Operaciones complejas")
        print("2. Verificar si un número es par")
        print("3. Verificar si un número es entero")

        opcion = input("Ingresa el número de la operación que deseas realizar: ")

        if opcion == "0":
            print("Saliendo de la calculadora.")
            break
        elif opcion == "1":
            print("Resultado:", operaciones_complejas())
        elif opcion == "2":
            try:
                num = int(input("Ingresa un número entero: "))
                print("¿Es par?", isiteven(num))
            except ValueError:
                print("Entrada inválida. Por favor ingresa un número entero.")
        elif opcion == "3":
            num = input("Ingresa un número: ")
            try:
                valor = eval(num)
                print("¿Es entero?", isintaninteger(valor))
            except:
                print("Entrada inválida.")
        else:
            print("Opción no válida.")

def main():
    calculadora()

if __name__ == "__main__":
    main()
