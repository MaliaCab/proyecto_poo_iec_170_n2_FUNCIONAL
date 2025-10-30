def ingresar_datos_pago():
    id_pedido = int(input('Ingrese ID del pedido a pagar: '))
    monto = float(input('Ingrese monto del pago: '))
    fecha_pago = input('Ingrese fecha de pago (YYYY-MM-DD): ')
    estado_pago = input('Ingrese estado del pago: ')
    metodo_pago = input('Ingrese método de pago: ')
    procesar_pago = input('Indique si desea procesar el pago (Sí/No): ')
    verificar_pago = input('Indique si desea verificar el pago (Sí/No): ')
    return (id_pedido, monto, fecha_pago, estado_pago, metodo_pago, procesar_pago, verificar_pago)