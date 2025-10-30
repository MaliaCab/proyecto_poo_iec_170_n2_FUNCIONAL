-- EJEMPLOS DE CONSULTAS (SELECT)
SELECT nombre_cliente, total_pedido
FROM pedidos
JOIN clientes ON pedidos.id_cliente = clientes.id_cliente;

-- EJEMPLOS DE ACTUALIZACIONES (UPDATE)
UPDATE productos SET stock_producto = 45 WHERE id_producto = 1;

-- EJEMPLOS DE ELIMINACIONES (DELETE)
DELETE FROM pedidos WHERE id_pedido = 3;