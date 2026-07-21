create table cliente(
	id integer not null auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null,
    data_nascimento date,
    limite_credito decimal(10, 2),
    primary key(id)
);