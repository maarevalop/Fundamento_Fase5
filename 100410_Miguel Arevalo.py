# Código Fuente: autoría propia
# Nombre: Miguel Angel Arevalo Poveda
# Grupo: 213022_727
# Programa: Ingeniería de Sistemas

productos = [

    ["Manzana", "Fruta", 9500],

    ["Espinaca", "Verdura", 3500],

    ["Lomo de cerdo", "Carne", 14850],

    ["Pera", "Fruta", 7500],

    ["Pechuga de pollo", "Carne", 10900],
    
    ["Brocoli", "Verdura", 4000]
]

def calcularPrecio (precioBase, categoriaBase, categoriaDescuento, precioUmbral):
    if precioBase > precioUmbral and categoriaBase == categoriaDescuento:
        precioFinal = precioBase - (precioBase * 0.15)
    else:
        precioFinal = precioBase
    return precioFinal

while True:
    print("\n*--- MENÚ DEL RESTAURANTE ---*")
    print("1. Ver menú.")
    print("2. Salir.")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        categoriaDescuento = "Fruta"
        precioUmbral = 8000

        print("*--- Lista de productos ---*")
        for elemento in productos:
            nombre = elemento[0]
            categoriaBase = elemento[1]
            precioBase = elemento[2]

            precioDescuento = calcularPrecio(precioBase, categoriaBase, categoriaDescuento, precioUmbral)
            print(f"\nnombre: {nombre}, \nprecio base: ${precioBase}, \nprecio final con descuento (si aplica): ${precioDescuento}")
            
    elif opcion == "2":
        print("Gracias por usar nuestro menú.")
        break
    else: print("Opción invalida.")
