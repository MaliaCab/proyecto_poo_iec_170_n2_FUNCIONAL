from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from modelo.cliente import Base

class Pago(Base):
    __tablename__ = 'pagos'
    id_pago = Column(Integer, primary_key=True)
    id_pedido = Column(Integer, ForeignKey('pedidos.id_pedido'), nullable=False)
    monto_pago = Column(Float, nullable=False)
    fecha_pago = Column(Date, nullable=False)
    estado_pago = Column(String(30), nullable=False)
    metodo_pago = Column(String(20), nullable=False)

    #Métodos
    def procesar_pago(self):
        pass

    def verificar_pago(self):
        pass