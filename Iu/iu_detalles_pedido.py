def ingresar_datos_detalles_pedido():
    id_pedido = int(input('Ingrese ID del pedido: '))
    id_producto = int(input('Ingrese ID del producto: '))
    cantidad = int(input('Ingrese cantidad: '))
    precio_unitario = float(input('Ingrese precio unitario: '))
    return (id_pedido, id_producto, cantidad, precio_unitario)