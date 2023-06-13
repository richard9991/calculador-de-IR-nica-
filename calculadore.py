

# calculadora basica en python 
def sumar(num1,num2):
    return num1 + num2 

def restar(num1,num2):
    return num1 - num2

def multiplicar(num1,num2):
    return num1 * num2

#funcion para dividir dos numeros 
def dividir(num1,num2):
    if num2 !=0:
        return num1 / num2
    
def main():
    operacion = input("selecciona la operacion ( +, -, *, /):")
    num1 = float(input("ingrese el primer numero : "))
    num2 = float(input("seleccione el segundo numero :"))

    resultado = 0

    if operacion == "+":
        resultado = sumar(num1, num2)
    elif operacion == "-":
        resultado = restar(num1, num2)
    elif operacion == "*":
        resultado = multiplicar(num1, num2)
    elif operacion == "/":
        resultado = dividir(num1, num2)
    else:
        print("Operación inválida")

    print("El resultado es:", resultado)

# Llamar a la función principal
main()