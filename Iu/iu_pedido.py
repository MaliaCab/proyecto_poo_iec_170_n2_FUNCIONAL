def ingresar_datos_pedido():
    id_cliente = int(input('Ingrese ID del cliente: '))
    fecha_pedido = input('Ingrese fecha del pedido (YYYY-MM-DD): ')
    estado_pedido = input('Ingrese estado del pedido: ')
    metodo_pago = input('Ingrese método de pago: ')
    return (id_cliente, fecha_pedido, estado_pedido, metodo_pago)