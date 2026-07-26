create table cidade(
    id integer not null auto_increment,
    nome varchar(100) not null,
    estado_id int not null,
    primary key(id),
    constraint fk_cidade_estado foreign key (estado_id) references estado(id)
);