from datos.conexion import Session
from modelo.cliente import Cliente
from modelo.producto import Producto
from modelo.pedido import Pedido
from modelo.detalles_pedido import DetallesPedido
from modelo.pago import Pago
from auxiliares.normalizar_cadena import normalizar_cadena

# Crear sesión de conexión con la base de datos
sesion = Session()

# Función genérica para obtener todos los objetos de una tabla
def obtener_datos_objetos(objeto):
    try:
        listado_objetos = sesion.query(objeto).all()
        if len(listado_objetos) > 0:
            return listado_objetos
        else:
            print("No se encontraron registros en la tabla.")
            return []
    except Exception as e:
        print(f"Error al obtener los datos: {e}")
        return []
    finally:
        sesion.close()

# Funciones específicas por cada tabla

# ---------- CLIENTE ----------
def obtener_cliente_por_nombre(nombre_cliente):
    sesion_local = Session()
    clientes = sesion_local.query(Cliente).all()
    for cliente in clientes:
        if normalizar_cadena(cliente.nombre_cliente) == normalizar_cadena(nombre_cliente):
            sesion_local.close()
            return cliente
    sesion_local.close()
    return None

# ---------- PRODUCTO ----------
def obtener_producto_por_nombre(nombre_producto):
    sesion_local = Session()
    productos = sesion_local.query(Producto).all()
    for producto in productos:
        if normalizar_cadena(producto.nombre_producto) == normalizar_cadena(nombre_producto):
            sesion_local.close()
            return producto
    sesion_local.close()
    return None

# ---------- PEDIDO ----------
def obtener_pedido_por_id(id_pedido):
    sesion_local = Session()
    pedido = sesion_local.query(Pedido).filter_by(id_pedido=id_pedido).first()
    sesion_local.close()
    return pedido

# ---------- DETALLE PEDIDO ----------
def obtener_detalle_pedido_por_id(id_detalle):
    sesion_local = Session()
    detalles = sesion_local.query(DetallesPedido).filter_by(id_detalle=id_detalle).first()
    sesion_local.close()
    return detalles

# ---------- PAGO ----------
def obtener_pago_por_id(id_pago):
    sesion_local = Session()
    pago = sesion_local.query(Pago).filter_by(id_pago=id_pago).first()
    sesion_local.close()
    return pago