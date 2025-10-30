def ingresar_datos_cliente():
    rut = input('Ingrese RUT del cliente: ')
    nombre = input('Ingrese nombre del cliente: ')
    correo = input('Ingrese correo del cliente: ')
    telefono = input('Ingrese teléfono del cliente: ')
    direccion = input('Ingrese dirección del cliente: ')
    return (rut, nombre, correo, telefono, direccion)