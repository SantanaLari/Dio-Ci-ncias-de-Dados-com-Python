create database oficina;
use oficina;

create table cliente(
	CPF int,
    nomeCliente varchar(200),
    endereco varchar(200),
    telefone int,
    email varchar(200),
    PRIMARY KEY(CPF)
);

insert into cliente values
(12345, 'Jose', 'Rua das ameixas 111', 20203030, 'jose@gmail.com'),
(11122, 'Maria', 'Rua do limoeiro 22', 30303030, 'maria@gmail.com'),
(11113, 'Carla', 'Rua das rosas 04', 70707070, 'carla@gmail.com');

create table veiculo(
	idVeiculo int,
    cpf_cliente int,
    marca varchar(100),
    modelo varchar(100),
    ano int,
    placa varchar(10),
    PRIMARY KEY(idVeiculo),
    FOREIGN KEY(cpf_cliente) references cliente(CPF)
);

insert into veiculo values
(111, 12345, 'Toyota', 'Corolla', 1999, 'bra-1234'),
(222, 11122, 'Honda', 'Civic', 2000, 'bra-9991'),
(333, 11113, 'Ford', 'Focus', 2021, 'bra-0002');

create table servico(
	idServico int,
    idVeiculo int,
    data_completa date,
    descricao varchar(200),
    custo float,
    PRIMARY KEY(idServico),
    FOREIGN KEY(idVeiculo) references veiculo(idVeiculo)
);

insert into servico values
(1000, 111, '2020-03-03', 'Troca de óleo', 200.0),
(1001, 111, '2020-03-03', 'lavagem e limpeza', 100.0),
(1002, 333, '2020-03-03', 'lavagem e limpeza', 100.0),
(1003, 222, '2020-03-03', 'Troca de óleo', 200.0),
(1004, 222, '2020-03-03', 'Reparos de colisão', 300.0);

-- Select
select * from cliente;
select * from veiculo;
select * from servico;

-- verificar cliente, modelo, serviço e custo
select cl.nomeCliente, vl.modelo, sv.descricao, sv.custo
from cliente cl, veiculo vl, servico sv
where sv.idVeiculo = vl.idVeiculo
	AND cl.CPF = vl.cpf_cliente;

-- verificar custo total 
select cl.nomeCliente, SUM(sv.custo) AS custo_total
from cliente cl, veiculo vl, servico sv
where sv.idVeiculo = vl.idVeiculo
	AND cl.CPF = vl.cpf_cliente
GROUP BY cl.nomeCliente;

-- verificar valores acima de 100
select cl.nomeCliente, SUM(sv.custo) AS custo_total
from cliente cl, veiculo vl, servico sv
where sv.idVeiculo = vl.idVeiculo
	AND cl.CPF = vl.cpf_cliente
GROUP BY cl.nomeCliente
HAVING SUM(sv.custo) > 100;


