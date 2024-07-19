def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def calculadora():
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        opcion = input("Ingrese su elección (1/2/3/4): ")

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == '1':
                print(f"El resultado de la suma es: {suma(num1, num2)}")
            elif opcion == '2':
                print(f"El resultado de la resta es: {resta(num1, num2)}")
            elif opcion == '3':
                print(f"El resultado de la multiplicación es: {multiplicacion(num1, num2)}")
            elif opcion == '4':
                resultado = division(num1, num2)
                if resultado == "Error: División por cero":
                    print(resultado)
                else:
                    print(f"El resultado de la división es: {resultado}")

            otra = input("¿Quieres realizar otra operación? (s/n): ")
            if otra.lower() != 's':
                break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 4.")

if __name__ == "__main__":
    calculadora()