num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
operacion = input("Introduce una operacion (suma, resta, multiplicacion o division): ").upper()

if operacion == "SUMA":
    resultado = num1+num2
    print(f"el resultado de la suma es:", resultado)

elif operacion == "RESTA":
    resultado = num1-num2
    print(f"El resultado de la resta es: ", resultado)

elif operacion == "MULTIPLICACION":
    resultado = num1*num2
    print(f"el resultado de la multiplicacion es: ", resultado)

elif operacion == "DIVISION":
    if num2 == 0:
        print("Error: no puedes dividir por 0")
    else:
        resultado = num1/num2
        print(f"el resultdo de la division es: ", resultado)
else:
    print("Error: Introduce una operacion valida")
