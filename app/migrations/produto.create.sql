create database mini_erp;
use mini_erp;

create table produto(
	id integer not null auto_increment,
    nome varchar(50) not null,
    estoque integer not null,
    preco decimal(10,2) not null,
    primary key(id)
);

create table fornecedor(
	id integer not null auto_increment,
    razao_social varchar(100) not null,
    nome_fantasia varchar(100) not null ,
    cnpj varchar(18) unique ,
    sla_atendimento integer,
    primary key(id)
);

create table cliente(
	id integer not null auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null,
    data_nascimento date,
    limite_credito decimal(10, 2),
    primary key(id)
);

create table usuario(
	id integer not null auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null,
    data_nascimento date,
    primary key(id)
    );