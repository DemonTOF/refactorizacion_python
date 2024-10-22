productos = []
producto_detalle = {  # se inicializa el diccionario aqui, para almacenar luego los detalles del producto
                "nombre" : [],
                "precio" : [],
                "cantidad" : []
            }
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
            
            producto_detalle["nombre"].append(nombre)  # se guarda en el diccionario
            producto_detalle["precio"].append(precio)  # todos los detalles
            producto_detalle["cantidad"].append(cantidad)
            
            productos.append(nombre)    # de aca se saca el indice del producto
                                        # para buscar en el diccionario 
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
    
    long = len(producto_detalle["nombre"])    # se saca la longitud de una lista del diccionario, para poder iterar en el
    for num in range(long):
        print(f'{num+1}) Producto: {producto_detalle["nombre"][num]}. Precio: {producto_detalle["precio"][num]}. Cant.: {producto_detalle["cantidad"][num]}.')

def actualizar_producto():
    # Lógica para actualizar un producto
    while True:
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print("Ingrese el nombre del producto a actualizar: ")
        producto = input()
        
        # el producto ingresado esta en la lista?
        flag = False
        for x in productos:
            if x.lower() == producto.lower():
                flag = True
                indice = productos.index(x)
        
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
                productos[indice] = input("Nuevo producto: ")
                producto_detalle["nombre"][indice] = productos[indice]
                break
            elif opcion == "2":
                while True:
                    nuevo_precio = input("Nuevo precio: ")
                    
                    if nuevo_precio.isdecimal():
                        nuevo_precio = int(nuevo_precio)
                        producto_detalle["precio"][indice] = nuevo_precio
                        break
                    else:
                        print("Ingrese un numero.")
            elif opcion == "3":
                while True:
                    nuevo_cant = input("Nueva cantidad: ")
                    
                    if nuevo_cant.isdecimal():
                        nuevo_cant = int(nuevo_cant)
                        producto_detalle["cantidad"][indice] = nuevo_cant
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
        if producto.lower() == eliminar_producto.lower():
            indice = productos.index(producto)
            productos.remove(eliminar_producto)
            
            producto_detalle["nombre"].remove(eliminar_producto)
            producto_detalle["precio"].remove(producto_detalle["precio"][indice])
            producto_detalle["cantidad"].remove(producto_detalle["cantidad"][indice])
            
    
    print(f'No se encontro el producto: {eliminar_producto}')

def guardar_datos():
    # Lógica para guardar los datos en un archivo
    long = len(producto_detalle["nombre"])    # se saca la longitud de una lista del diccionario, para poder iterar en el
    for num in range(long):
        archivo = f'{producto_detalle["nombre"][num]},{producto_detalle["precio"][num]},{producto_detalle["cantidad"][num]}'
        
        try:
            file_pc = open("productos.txt", 'a')
            file_pc.write(f'{ archivo } \n')
            file_pc.close()
        except FileNotFoundError:
            print("Error: El archivo no se encontró.")

def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    try:
        with open("productos.txt", 'r') as file_pc:
            for linea in file_pc:
                nombre, precio, cantidad = linea.strip().split(",")
                
                # Guardar los datos en las estructuras
                producto_detalle["nombre"].append(nombre)
                producto_detalle["precio"].append(int(precio))
                producto_detalle["cantidad"].append(int(cantidad))
                
                productos.append(nombre)
                
        print("Datos cargados correctamente.")
    
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