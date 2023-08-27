use e_commerce;

-- visualização das tabelas
select * from pedido;
select * from cliente;
select * from produto;

-- visualizar pedidos do cliente de id 1, 2 e 3
select *
from pedido
where idPedidoCliente = 1;

select *
from pedido
where idPedidoCliente = 2;

select * 
from pedido
where idPedidoCliente = 3;

-- Produtos maiores e menores
select idProduto, Pname, size 
from produto
order by size DESC;

-- Valor da compra dos clientes 
select cl.Fname, SUM(pd.sendValue) AS valor_total
from cliente cl, pedido pd
where pd.idPedidoCliente = cl.idCliente
GROUP BY cl.Fname
order by valor_total DESC;

-- compras acima de 5000
select cl.Fname, SUM(pd.sendValue) AS valor_total
from cliente cl, pedido pd
where pd.idPedidoCliente = cl.idCliente
GROUP BY cl.Fname
HAVING SUM(pd.sendValue) > 5000
