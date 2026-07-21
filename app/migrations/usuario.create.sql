create table usuario(
	id integer not null auto_increment,
    nome varchar(100) not null,
    email varchar(100) not null,
    data_nascimento date,
    primary key(id)
    );