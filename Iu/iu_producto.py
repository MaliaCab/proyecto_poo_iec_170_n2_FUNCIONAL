def ingresar_datos_producto():
    nombre = input('Ingrese nombre del producto: ')
    precio = float(input('Ingrese precio del producto: '))
    stock = int(input('Ingrese stock disponible: '))
    descripcion = input('Ingrese descripción del producto: ')
    return (nombre, precio, stock, descripcion)