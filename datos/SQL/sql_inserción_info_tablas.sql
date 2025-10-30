USE boutique_db;
-- TABLA CLIENTES

INSERT INTO clientes (rut_cliente, nombre_cliente, correo_cliente, telefono_cliente, direccion_cliente)
VALUES
('11.111.111-1', 'Catalina Quezada', 'cati.quezada@gmail.com', '+56 9 1111 1111', 'Purén, Chile'),
('22.222.222-2', 'Scarlett Araya', 'scarlett.araya@gmail.com', '+56 9 2222 2222', 'Angol, Chile'),
('33.333.333-3', 'Benjamín Silva', 'benja.silva@gmail.com', '+56 9 3333 3333', 'Los Ángeles, Chile');

-- TABLA PRODUCTOS
INSERT INTO productos (nombre_producto, precio_producto, stock_producto, descripcion_producto)
VALUES
('Base de Maquillaje Hidratante', 13990, 30, 'Base líquida de cobertura media y acabado natural'),
('Labial Mate Color Intenso', 7990, 50, 'Labial de larga duración con acabado mate'),
('Paleta de Sombras Neutra', 19990, 20, 'Paleta de 12 tonos cálidos y fríos para todo tipo de look'),
('Máscara de Pestañas Voluminizadora', 9990, 40, 'Aumenta el volumen y alarga las pestañas'),
('Iluminador Compacto Glow', 10990, 25, 'Polvo iluminador con efecto natural y radiante');

-- TABLA PEDIDOS
INSERT INTO pedidos (id_cliente, fecha_pedido, estado_pedido, total_pedido, metodo_pago)
VALUES
(1, '2025-10-20', 'Completado', 27980, 'Transferencia'),
(2, '2025-10-21', 'Pendiente', 19990, 'Efectivo'),
(3, '2025-10-22', 'En proceso', 10990, 'Tarjeta');

-- TABLA DETALLES_PEDIDO
INSERT INTO detalles_pedido (id_pedido, id_producto, cantidad_pedido, precio_unitario, subtotal_pedido)
VALUES
(1, 1, 1, 13990, 13990),
(1, 2, 1, 7990, 7990),
(2, 3, 1, 19990, 19990),
(3, 5, 1, 10990, 10990);

-- TABLA PAGOS
INSERT INTO pagos (id_pedido, monto_pago, fecha_pago, estado_pago, metodo_pago)
VALUES
(1, 27980, '2025-10-20', 'Pagado', 'Transferencia'),
(2, 0, '2025-10-21', 'Pendiente', 'Efectivo'),
(3, 0, '2025-10-22', 'En proceso', 'Tarjeta');
