from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id_cliente = Column(Integer, primary_key=True)
    rut_cliente = Column(String(12), unique=True, nullable=False)
    nombre_cliente = Column(String(50), nullable=False)
    correo_cliente = Column(String(50), nullable=False)
    telefono_cliente = Column(String(15), nullable=False)
    direccion_cliente = Column(String(100), nullable=False)

    #Métodos
    def comprar(self):
        pass

    def pagar(self):
        pass

    def comentar(self):
        pass