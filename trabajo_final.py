def main():
    print("=== Registro de Pedido - Tuya Pez ===")
    
    nombre = input("Nombre del plato: ")
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    cantidad = input("Cantidad: ")
    if cantidad.isdigit():
        cantidad = int(cantidad)
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
            return
    else:
        print("Debe ingresar un número entero válido.")
        return

    precio = input("Precio unitario: ")
    punto = False
    for i in range(len(precio)):
        if precio[i] == ".":
            punto = True
    if precio.replace(".", "").isdigit() and punto:
        precio = float(precio)
        if precio <= 0:
            print("El precio debe ser mayor que 0.")
            return
    else:
        print("Debe ingresar un número decimal válido.")
        return

    subtotal = cantidad * precio

    metodo = input("Método de pago (efectivo/POS): ").lower()
    if metodo != "efectivo" and metodo != "pos":
        print("Método de pago inválido.")
        return

    archivo = open("pedido_tuya_pez.csv", "a")
    archivo.write(nombre + "," + str(cantidad) + "," + str(precio) + "," + str(subtotal) + "," + metodo + "\n")
    archivo.close()

    print("Pedido registrado correctamente. Total: S/", subtotal)

if __name__ == "__main__":
    main()
