from auxiliares.info_aplicacion import nombre_aplicacion
from auxiliares.version import numero_version

def menu_principal():
    while True:
        print(f'{nombre_aplicacion} v.{numero_version}')
        print('=======================================')
        print('[1] Gestión Clientes')
        print('[2] Gestión Productos')
        print('[3] Gestión Pedidos')
        print('[4] Gestión Detalles Pedido')
        print('[5] Gestión Pagos')
        print('[0] Salir')
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_productos()
        elif opcion == '3':
            menu_pedidos()
        elif opcion == '4':
            menu_detalles_pedido()
        elif opcion == '5':
            menu_pagos()
        elif opcion == '0':
            print('Saliendo del sistema...')
            break
        else:
            print('Opción inválida. Intente nuevamente.')

def menu_clientes():
    print('--- Gestión Clientes ---')
    print('[1] Agregar Cliente')
    print('[2] Ver Clientes')
    print('[3] Actualizar Cliente')
    print('[4] Eliminar Cliente')
    print('[0] Volver')
    # Aquí se podrían llamar las funciones de IU y negocio correspondientes

def menu_productos():
    print('--- Gestión Productos ---')
    print('[1] Agregar Producto')
    print('[2] Ver Productos')
    print('[3] Actualizar Producto')
    print('[4] Eliminar Producto')
    print('[0] Volver')

def menu_pedidos():
    print('--- Gestión Pedidos ---')
    print('[1] Agregar Pedido')
    print('[2] Ver Pedidos')
    print('[3] Actualizar Pedido')
    print('[4] Eliminar Pedido')
    print('[0] Volver')

def menu_detalles_pedido():
    print('--- Gestión Detalles Pedido ---')
    print('[1] Agregar Detalle')
    print('[2] Ver Detalles')
    print('[3] Actualizar Detalle')
    print('[4] Eliminar Detalle')
    print('[0] Volver')

def menu_pagos():
    print('--- Gestión Pagos ---')
    print('[1] Agregar Pago')
    print('[2] Ver Pagos')
    print('[3] Actualizar Pago')
    print('[4] Eliminar Pago')
    print('[0] Volver')