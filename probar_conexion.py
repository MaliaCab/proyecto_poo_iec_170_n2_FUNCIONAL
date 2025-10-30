from datos.conexion import Session
from modelo.cliente import Cliente

# Crear sesión
sesion = Session()

try:
    # Intentar traer todos los clientes
    clientes = sesion.query(Cliente).all()
    if clientes:
        print("Conexión exitosa. Clientes encontrados:")
        for c in clientes:
            print(f"- {c.nombre_cliente}")
    else:
        print("Conexión exitosa, pero no hay clientes en la base de datos.")
except Exception as e:
    print(f"Error al conectarse a la base de datos: {e}")
finally:
    sesion.close()
    