'''
Crie duas tabelas no seu banco: (usuario e postagens)
usuario terá atributos (colunas): id, titulo, postagem e id_autor
postagens terá atributos (colunas): id, titulo, postagem e id_autor

o id_usuarios séra um id existente de usuarios

faça 5 inscrições de valores em vada tabela
'''
import sqlite3
conn = sqlite3.connect('meu_banco.db')


create table usuario (
    id integer primary key,
    nome text not null,
    sobrenome text not null,
    contato text not null,
    idade INTEGER
);
insert into usuario (nome, sobrenome, contato, idade) values('João', 'Silva', '219999999', 20);
insert into usuario (nome, sobrenome, contato, idade) values('Silva', 'Silva', '219999998', 22);
insert into usuario (nome, sobrenome, contato, idade) values('Dão', 'Silva', '219999996', 24);
insert into usuario (nome, sobrenome, contato, idade) values('Tão', 'Silva', '219999994', 26);
insert into usuario (nome, sobrenome, contato, idade) values('Tião', 'Silva', '219999992', 28);

create table postagem (
    id integer primary key,
    nome text not null,
    idade INTEGER
);

insert into postagem (nome, idade) values('Maria', 22);

select*FROM usuario;

select*FROM postagem;