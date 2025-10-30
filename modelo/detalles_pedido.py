from sqlalchemy import Column, Integer, Float, ForeignKey
from modelo.cliente import Base

class DetallesPedido(Base):
    __tablename__ = 'detalles_pedido'
    id_detalle = Column(Integer, primary_key=True)
    id_pedido = Column(Integer, ForeignKey('pedidos.id_pedido'), nullable=False)
    id_producto = Column(Integer, ForeignKey('productos.id_producto'), nullable=False)
    cantidad_pedido = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    subtotal_pedido = Column(Float, nullable=False)

    #Método
    def calcular_subtotal(self):
        pass