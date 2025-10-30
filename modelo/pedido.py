from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from modelo.cliente import Base

class Pedido(Base):
    __tablename__ = 'pedidos'
    id_pedido = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'), nullable=False)
    fecha_pedido = Column(Date, nullable=False)
    estado_pedido = Column(String(30), nullable=False)
    total_pedido = Column(Float, nullable=False)
    metodo_pago = Column(String(20), nullable=False)

    #Métodos
    def calcular_total(self):
        pass

    def actualizar_estado(self):
        pass

    def agregar_producto_pedido(self):
        pass