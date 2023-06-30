print("Bienvendios a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = "" # Definicion de valiables
while True: # Loops
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa la operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingresa siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Escriba de nuevo la operacion")
    
    print(f"el resultado es: {resultado}")