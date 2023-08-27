-- criaçao do banco de dados para o cenário de E-commerce
create database e_commerce;
use e_commerce;

-- criar tabela cliente
create table cliente(
	idCliente int primary key,
    Fname varchar(10),
    Minit char(3),
    Lname varchar(20),
    CPF char(11) not null,
    Address varchar(30)
);

-- SELECT CLIENTE
insert into cliente values
(1, 'Maria', 'M', 'Silva', '123456789', 'rua silva de prata'),
(2, 'Jose', 'J', 'Castro', '123456780', 'rua limoeiro'),
(3, 'Tadeu', 'T', 'Perez', '123456781', 'rua pedro de castro');

-- criar tabela produto
create table produto (
    idProduto int primary key,
    Pname varchar(10) not null,
    classification_kid bool default false,
    category enum('Eletrônico','Vestimento','Brinquedo','Alimentos','Móveis') not null,
    avaliacao float default 0,
    size varchar(10)
);

insert into produto values
(111, 'computador', false, 'Eletrônico', 5, 100),
(112, 'bola', true, 'Brinquedo', 5, 5),
(113, 'Vestido', false, 'Vestimento', 5, 10),
(114, 'Armário', false, 'Móveis', 4, 300),
(115, 'TV', false, 'Eletrônico', 5, 200);


-- para ser continuado no desafio: termine de implementar a tabela e crie a conexão com as tabelas necessárias
-- além disso, reflita essa modificaçao no diagrama de esquema relacional
-- criar constraints relacionadas ao pagamento
create table payments(
	idCliente int,
    idPayment int,
    typePayment enum('Boleto','Cartão','Dois cartões'),
    limitAvailable float,
    primary key(idCliente, idPayment),
    foreign key (idCliente) references cliente(idCliente)
);

-- criar tabela pedido
create table pedido(
	idPedido int primary key,
    idPedidoCliente int,
    idPedidoProduto int,
    pedidoStatus enum('Cancelado','Confirmado','Em processamento') default 'Em processamento',
    pedidoDescrição varchar(255),
    sendValue float default 10,
    paymentCash bool default false,
    constraint fk_pedido_Cliente foreign key(idPedidoCliente) references cliente(idCliente),
    constraint fk_pedido_Produto foreign key(idPedidoProduto) references produto(idProduto)
);
select * from cliente;
select * from produto;
select * from pedido;

insert into pedido values
(200, 1, 111, 'Confirmado', 'Computador da acer', 3000.0, false),
(201, 2, 111, 'Confirmado', 'Computador da acer', 3000.0, false), 
(202, 3, 111, 'Confirmado', 'Computador da acer', 3000.0, false),
(203, 1, 112, 'Em processamento', 'Produto', 20, true),
(204, 1, 114, 'Cancelado', 'Produto', 1000.0, false),
(205, 1, 115, 'Confirmado', 'Produto', 2000.0, false),
(206, 2, 115, 'Confirmado', 'Produto', 2000.0, false),
(207, 1, 113, 'Em processamento', 'Produto', 15.0, true),
(208, 3, 114, 'Em processamento', 'Produto', 1000.0, false),
(209, 3, 111, 'Confirmado', 'Computador da acer', 3000.0, false);

-- criar tabela estoque
create table produtoEstoque(
	idProdEstoque int auto_increment primary key,
    localizacaoEs varchar(255),
    sendValue float default 10,
    paymentCash bool default false,
    idPedidoCliente int,
    constraint pedido_cliente foreign key(idPedidoCliente) references cliente(idCliente)
);

-- criar tabela fornecedor
create table fornecedor(
	idFornecedor int auto_increment primary key,
    nomeSocial varchar(255) not null,
    CNPJ char(15) not null,
    contato char(11) not null,
    constraint unique_supplier unique (CNPJ)
);

-- criar tabela vendedor
create table vendedor(
	idVendedor int auto_increment primary key,
    nomeSocial varchar(255) not null,
    AbsName varchar(255),
    CNPJ char(15),
    CPF char(9),
    location varchar(255),
    contato char(11) not null,
    constraint unique_cnpj_seller unique (CNPJ),
    constraint unique_cpf_seller unique (CPF)
);

create table produtoVendedor(
	idVendedor int,
    idProduto int,
    prodQTD int default 1,
    idPvendedor int,
    primary key(idVendedor, idProduto),
    constraint fk_produto_vendedor foreign key(idPvendedor) references vendedor(idVendedor),
    constraint fk_produto_produto foreign key(idProduto) references produto(idProduto)
);

create table produtoPedido(
	idPOproduct int,
    idPOorder int,
    poQuantity int default 1,
    poStatus enum('Disponivel','Sem estoque') default 'Disponivel',
    primary key (idPOproduct, idPOorder),
    constraint produto_vendedor foreign key(idPOproduct) references produto(idProduto),
    constraint produto_produto foreign key(idPOorder) references pedido(idPedido)
);

create table storageLocation(
	idLproduct int,
    idLstorage int,
    location varchar(255) not null,
    primary key(idLproduct, idLstorage),
    constraint fkproduto_vendedor foreign key(idLproduct) references produto(idProduto),
    constraint fkproduto_produto foreign key(idLstorage) references pedido(idPedido)
);


