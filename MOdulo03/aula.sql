-- Active: 1759754331840@@127.0.0.1@3306
create table alunos (
    id integer primary key,
    nome text not null,
    idade INTEGER
);

insert into alunos (nome, idade) values('João', 20);
insert into alunos (nome, idade) values('Maria', 22);

select*FROM alunos;

select nome, idade FROM alunos;