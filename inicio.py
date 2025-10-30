from datos.conexion import Session

from datos.obtener_datos import (
    obtener_datos_objetos,
    obtener_cliente_por_nombre,
    obtener_producto_por_nombre,
    obtener_pedido_por_id
)
from modelo.cliente import Cliente
from modelo.producto import Producto
from modelo.pedido import Pedido
from modelo.detalles_pedido import DetallesPedido
from modelo.pago import Pago
from prettytable import PrettyTable
# ---------- LISTADOS ----------
#Falta los detalles pedido
def listado_clientes():
    tabla = PrettyTable(['ID', 'RUT','Nombre', 'Correo', 'Teléfono', 'Dirección'])
    listado = obtener_datos_objetos(Cliente)
    for c in listado:
        tabla.add_row([c.id_cliente,c.rut_cliente, c.nombre_cliente, c.correo_cliente, c.telefono_cliente, c.direccion_cliente])
    print(tabla)

def listado_productos():
    tabla = PrettyTable(['ID', 'Nombre', 'Precio', 'Stock', 'Descripción'])
    listado = obtener_datos_objetos(Producto)
    for p in listado:
        tabla.add_row([p.id_producto, p.nombre_producto, p.precio_producto, p.stock_producto, p.descripcion_producto])
    print(tabla)

def listado_pedidos():
    tabla = PrettyTable(['ID', 'ID Cliente', 'Fecha', 'Estado', 'Total'])
    listado = obtener_datos_objetos(Pedido)
    for ped in listado:
        tabla.add_row([ped.id_pedido, ped.id_cliente, ped.fecha_pedido, ped.estado_pedido, ped.total_pedido])
    print(tabla)

def listado_pagos():
    tabla = PrettyTable(['ID', 'ID Pedido', 'Monto', 'Fecha', 'Estado'])
    listado = obtener_datos_objetos(Pago)
    for pago in listado:
        tabla.add_row([pago.id_pago, pago.id_pedido, pago.monto_pago, pago.fecha_pago, pago.estado_pago])
    print(tabla)

# ---------- INSERCIONES ----------

def insertar_cliente():
    sesion = Session()
    rut = input('Ingrese RUT del cliente, con puntos: ')
    nombre = input('Ingrese nombre del cliente: ')
    correo = input('Ingrese correo del cliente: ')
    telefono = input('Ingrese teléfono del cliente: ')
    direccion = input('Ingrese dirección del cliente: ')

    if not obtener_cliente_por_nombre(nombre):
        c = Cliente(rut_cliente= rut, nombre_cliente=nombre, correo_cliente=correo, telefono_cliente=telefono, direccion_cliente=direccion)
        sesion.add(c)
        try:
            sesion.commit()
            print("Cliente insertado correctamente.")
        except Exception as e:
            sesion.rollback()
            print(f"Error al insertar el cliente: {e}")
        finally:
            sesion.close()
    else:
        print("El cliente ya existe.")
#-------------------
''' 
def insertar_producto():
    sesion = Session()
    nombre = input('Ingrese nombre del producto: ')
    precio = float(input('Ingrese precio: '))
    stock = int(input('Ingrese stock: '))
    descripcion = input('Ingrese descripción: ')

    if not obtener_producto_por_nombre(nombre):
        p = Producto(nombre_producto=nombre, precio_producto=precio, stock_producto=stock, descripcion_producto=descripcion)
        sesion.add(p)
        try:
            sesion.commit()
            print("Producto insertado correctamente.")
        except Exception as e:
            sesion.rollback()
            print(f"Error al insertar el producto: {e}")
        finally:
            sesion.close()
    else:
        print("El producto ya existe.")

def insertar_pedido():
    sesion = Session()
    id_cliente = int(input("Ingrese ID del cliente: "))
    cliente = sesion.query(Cliente).filter_by(id_cliente=id_cliente).first()
    if not cliente:
        print("Cliente no encontrado.")
        sesion.close()
        return

    pedido = Pedido(id_cliente=id_cliente, fecha_pedido='2025-10-25', estado_pedido='Pendiente', total_pedido=0)
    sesion.add(pedido)
    try:
        sesion.commit()
        print(f"Pedido creado correctamente con ID {pedido.id_pedido}")
    except Exception as e:
        sesion.rollback()
        print(f"Error al crear pedido: {e}")
        sesion.close()
        return

    # Agregar productos al pedido
    agregar_detalle = input("¿Desea agregar productos al pedido? (s/n): ").lower()
    while agregar_detalle == 's':
        id_producto = int(input("Ingrese ID del producto: "))
        cantidad = int(input("Ingrese cantidad: "))
        producto = sesion.query(Producto).filter_by(id_producto=id_producto).first()
        if not producto:
            print("Producto no encontrado.")
            continue
        subtotal = producto.precio_producto * cantidad
        detalle = DetallesPedido(id_pedido=pedido.id_pedido, id_producto=id_producto,
                                cantidad_pedido=cantidad, precio_unitario=producto.precio_producto,
                                subtotal_pedido=subtotal)
        sesion.add(detalle)
        # Actualizar stock
        producto.stock_producto -= cantidad
        pedido.total_pedido += subtotal
        sesion.commit()
        print(f"Producto {producto.nombre_producto} agregado al pedido.")
        agregar_detalle = input("¿Agregar otro producto? (s/n): ").lower()
    sesion.close()
'''
from datetime import date # Importa date

def insertar_pedido():
    sesion = Session()
    try:
        id_cliente = int(input("Ingrese ID del cliente existente: "))
        cliente = sesion.query(Cliente).filter_by(id_cliente=id_cliente).first()
        
        if not cliente:
            print("Cliente no encontrado.")
            return # Se cierra en el 'finally'
        
        # 1. Crear el objeto Pedido (sin hacer commit aún)
        pedido = Pedido(
            id_cliente=id_cliente, 
            fecha_pedido=date.today(), # Usamos la fecha actual
            estado_pedido='Pendiente', 
            total_pedido=0
        )
        sesion.add(pedido)
        
        # Opcional: El primer commit puede ser necesario para obtener el id_pedido, 
        # pero es mejor hacerlo en un solo bloque si el ORM lo permite. 
        # Asumiendo que el ORM obtiene el ID después del add.

        total_acumulado = 0.0 # Variable para el cálculo del total

        # 2. Agregar productos al pedido
        agregar_detalle = input("¿Desea agregar productos al pedido? (s/n): ").lower()
        while agregar_detalle == 's':
            id_producto = int(input("Ingrese ID del producto: "))
            cantidad = int(input("Ingrese cantidad: "))
            
            producto = sesion.query(Producto).filter_by(id_producto=id_producto).first()
            
            if not producto:
                print("Producto no encontrado.")
                continue
            
            # Validación de stock (¡importante para la integridad!)
            if cantidad > producto.stock_producto:
                print(f"Stock insuficiente. Solo quedan {producto.stock_producto} unidades de {producto.nombre_producto}.")
                continue
            
            subtotal = producto.precio_producto * cantidad
            
            # Crear y agregar DetallePedido
            detalle = DetallesPedido(
                id_pedido=pedido.id_pedido, # SQLAlchemy debería poblar este ID después del add/commit inicial
                id_producto=id_producto,
                cantidad_pedido=cantidad,
                precio_unitario=producto.precio_producto,
                subtotal_pedido=subtotal
            )
            sesion.add(detalle)
            
            # Actualizar stock y acumular total
            producto.stock_producto -= cantidad
            total_acumulado += subtotal # Acumulamos en la variable local

            print(f"Producto {producto.nombre_producto} agregado a la lista de detalles.")
            agregar_detalle = input("¿Agregar otro producto? (s/n): ").lower()
            
        # 3. Actualizar el total del pedido
        pedido.total_pedido = total_acumulado
        
        # 4. COMMIT ÚNICO: Graba el Pedido, los Detalles y las actualizaciones de Stock.
        sesion.commit() 
        print(f"\n✅ Pedido creado exitosamente con ID {pedido.id_pedido}. Total: ${pedido.total_pedido:.2f}")

    except Exception as e:
        sesion.rollback()
        print(f"\n❌ ERROR CRÍTICO al procesar el pedido. Transacción deshecha: {e}")
    
    finally:
        sesion.close()
        
# Nota: La función obtener_producto_por_nombre(nombre) no está definida en tu código, 
# pero se asume que existe y funciona correctamente en 'insertar_producto()'.




#--------------------------
def insertar_pago():
    sesion = Session()
    id_pedido = int(input("Ingrese ID del pedido a pagar: "))
    pedido = obtener_pedido_por_id(id_pedido)
    if not pedido:
        print("Pedido no encontrado.")
        sesion.close()
        return
    monto = float(input(f"Ingrese monto a pagar (total del pedido: {pedido.total_pedido}): "))
    metodo = input("Ingrese método de pago (Ej: Transferencia, Efectivo, Tarjeta): ")
    pago = Pago(id_pedido=id_pedido, 
                monto_pago=monto, 
                fecha_pago=date.today(), 
                estado_pago='Pagado', 
                metodo_pago=metodo)
    sesion.add(pago)
    try:
        sesion.commit()
        print("Pago registrado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al registrar pago: {e}")
    finally:
        sesion.close()

# ---------- MENÚ PRINCIPAL ----------

print("Bienvenida al Sistema de Gestión de Boutique de Maquillaje")
print("\nOpciones:")
print("1 - Insertar cliente")
print("2 - Insertar producto")
print("3 - Insertar pedido")
print("4 - Registrar pago")
print("5 - Listado de clientes")
print("6 - Listado de productos")
print("7 - Listado de pedidos")
print("8 - Listado de pagos")

opcion = input("Seleccione una opción: ")

if opcion == '1':
    insertar_cliente()
elif opcion == '2':
    insertar_producto()
elif opcion == '3':
    insertar_pedido()
elif opcion == '4':
    insertar_pago()
elif opcion == '5':
    listado_clientes()
elif opcion == '6':
    listado_productos()
elif opcion == '7':
    listado_pedidos()
elif opcion == '8':
    listado_pagos()
else:
    print("Opción no válida.")