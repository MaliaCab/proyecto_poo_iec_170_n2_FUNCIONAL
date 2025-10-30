-- CREACIÓN DE TABLAS - SISTEMA DE TIENDA BOUTIQUE

-- Eliminar la base si ya existe
DROP DATABASE IF EXISTS boutique_db;

-- Crear nueva base de datos
CREATE DATABASE boutique_db;
USE boutique_db;

-- TABLA CLIENTES
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    rut_cliente VARCHAR(15) NOT NULL,
    nombre_cliente VARCHAR(100) NOT NULL,
    correo_cliente VARCHAR(100) NOT NULL,
    telefono_cliente VARCHAR(20),
    direccion_cliente VARCHAR(150)
);
-- TABLA PRODUCTOS
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(100) NOT NULL,
    precio_producto FLOAT NOT NULL,
    stock_producto INT NOT NULL,
    descripcion_producto VARCHAR(200)
);

-- TABLA PEDIDOS
CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha_pedido DATE NOT NULL,
    estado_pedido VARCHAR(50),
    total_pedido FLOAT,
    metodo_pago VARCHAR(50),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- TABLA DETALLES_PEDIDO
CREATE TABLE detalles_pedido (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad_pedido INT NOT NULL,
    precio_unitario FLOAT NOT NULL,
    subtotal_pedido FLOAT NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- TABLA PAGOS
CREATE TABLE pagos (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    monto_pago FLOAT NOT NULL,
    fecha_pago DATE NOT NULL,
    estado_pago VARCHAR(50),
    metodo_pago VARCHAR(50),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
);
