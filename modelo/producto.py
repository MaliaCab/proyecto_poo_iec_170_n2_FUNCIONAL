from sqlalchemy import Column, Integer, String, Float
from modelo.cliente import Base

class Producto(Base):
    __tablename__ = 'productos'
    id_producto = Column(Integer, primary_key=True)
    nombre_producto = Column(String(50), nullable=False)
    precio_producto = Column(Float, nullable=False)
    stock_producto = Column(Integer, nullable=False)
    descripcion_producto = Column(String(200), nullable=True)

    #Métodos
    def agregar_producto(self):
        pass

    def actualizar_producto(self):
        pass

    def eliminar_producto(self):
        pass

    def ver_producto(self):
        pass

    def actualizar_stock(self):
        pass