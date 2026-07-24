create table fornecedor(
	id integer not null auto_increment,
    razao_social varchar(100) not null,
    nome_fantasia varchar(100) not null ,
    cnpj varchar(18) unique ,
    sla_atendimento integer,
    primary key(id)
);