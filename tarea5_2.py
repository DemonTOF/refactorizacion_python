productos = []

def añadir_producto():
    # Lógica para añadir un producto
    while True:
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        nombre = input("Ingrese nombre de producto: ")  # se pide los detalles del
        precio = input("Ingrese el precio: ")           # producto al usuario
        cantidad = input("Ingrese cantidad: ")
        
        if precio.isdecimal() and cantidad.isdecimal():
            precio = int(precio)
            cantidad = int(cantidad)

            producto = {
                "nombre" : nombre,
                "precio" : precio,
                "cantidad" : cantidad
            }
            
            productos.append(producto)     
            
            print("\nProducto añadido exitosamente...\n")
            break
        else:
            print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Ingrese valores validos.")

def ver_productos():
    # Lógica para ver todos los productos
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    
    if not productos:
        print("No hay productos registrados.")
        return
    
    i = 0
    for producto in productos:
        i += 1
        print(f'{i}) Producto: {producto["nombre"]}. Precio: {producto["precio"]}. Cantidad: {producto["cantidad"]}')

def actualizar_producto():
    # Lógica para actualizar un producto
    while True:
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("Ingrese el nombre del producto a actualizar: ")
        producto = input()
        
        # el producto ingresado esta en la lista?
        flag = False
        for x in productos:
            #print(x)
            if x["nombre"] == producto.lower():
                flag = True
                indice = productos.index(x)
                #print(indice)
                
        if not flag:
            print(f'El producto {producto} no existe en la lista')
        else:
            print("Que detalle quiere cambiar?")
            print("1: Producto.")
            print("2: Precio.")
            print("3: Cantidad.")
            print("4. Salir")
            
            opcion = input("Selecciona una opcion: ")
            if opcion == "1":
                productos[indice]["nombre"] = input("Actualizar producto: ")
                print("\nProducto actualizado exitosamente...\n")
                break
            elif opcion == "2":
                while True:
                    nuevo_precio = input("Actualizar precio: ")
                    
                    if nuevo_precio.isdecimal():
                        nuevo_precio = int(nuevo_precio)
                        productos[indice]["precio"]= nuevo_precio
                        print("\nPrecio actualizado exitosamente...\n")
                        break
                    else:
                        print("Ingrese un numero.")
            elif opcion == "3":
                while True:
                    nuevo_cant = input("Actualizar cantidad: ")
                    
                    if nuevo_cant.isdecimal():
                        nuevo_cant = int(nuevo_cant)
                        productos[indice]["cantidad"] = nuevo_cant
                        print("\nCantidad actualizada exitosamente...\n")
                        break
                    else:
                        print("Ingrese un numero.")
            elif opcion == "4":
                break
            break

def eliminar_producto():
    # Lógica para eliminar un producto
    eliminar_producto = input("Ingrese un producto que quiera eliminar: ")
    
    for producto in productos:
        if producto["nombre"].lower() == eliminar_producto.lower():
            indice = productos.index(producto)
            #print(indice)
            #print(productos[indice])
            productos.pop(indice)
            print("\nProducto eliminado exitosamente...\n")
            return
    print(f'No se encontro el producto: {eliminar_producto}')

def guardar_datos():
    # Lógica para guardar los datos en un archivo
    try:
        # Abre el archivo una sola vez en modo 'w' para sobrescribir el contenido
        with open("productos.txt", 'w') as file_pc:  
            # Itera directamente sobre la lista de productos
            for producto in productos:
                archivo = f'{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}'
                file_pc.write(f'{ archivo }\n')  # Escribe cada línea en el archivo
            print("\nGuardando y saliendo...\n")
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")

def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    try:
        with open("productos.txt", 'r') as file_pc:
            for linea in file_pc:
                nombre, precio, cantidad = linea.strip().split(",")
                
                producto = {
                    "nombre" : nombre,
                    "precio" : precio,
                    "cantidad" : cantidad
                }
            
                productos.append(producto)
    
    except FileNotFoundError:
        print("El archivo no existe, no se han cargado productos.")

def menu():
    cargar_datos()
    while True:
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")
        if opcion.isdecimal():
            
            if opcion == '1':
                añadir_producto()
            elif opcion == '2':
                ver_productos()
            elif opcion == '3':
                actualizar_producto()
            elif opcion == '4':
                eliminar_producto()
            elif opcion == '5':
                guardar_datos()
                break
            else:
                print("Por favor, selecciona una opción válida.")
        else:
            print("Introduzca una opcion del 1 al 5.")

menu()