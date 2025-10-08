-- Active: 1759773230447@@127.0.0.1@3306
CREATE TABLE autores (
    id_autor INT PRIMARY KEY,
    nome VARCHAR(100),
    nacionalidade VARCHAR(50)
);

INSERT INTO autores (id_autor, nome, nacionalidade)
VALUES (1, 'J.K. Rowling', 'Britânica');

INSERT INTO autores (id_autor, nome, nacionalidade)
VALUES (2, 'George Orwell', 'Britânica');

CREATE TABLE livros (
    id_livro INT PRIMARY KEY,
    titulo VARCHAR(100),
    ano_publicacao INT,
    id_autor INT,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
);

INSERT INTO livros (id_livro, titulo, ano_publicacao, id_autor)
VALUES (1, 'Harry Potter e a Pedra Filosofal', 1997, 1);

INSERT INTO livros (id_livro, titulo, ano_publicacao, id_autor)
VALUES (2, '1984', 1949, 2);

INSERT INTO livros (id_livro, titulo, ano_publicacao, id_autor)
VALUES (3, 'Harry Potter e a Câmara Secreta', 1998, 1);

SELECT titulo, ano_publicacao
FROM livros;

SELECT livros.titulo, autores.nome
FROM livros
JOIN autores ON livros.id_autor = autores.id_autor;

SELECT livros.titulo, autores.nome
FROM livros
JOIN autores ON livros.id_autor = autores.id_autor
WHERE autores.nacionalidade = 'Britânica';

SELECT autores.nome, COUNT(livros.id_livro) AS quantidade_livros
FROM autores
JOIN livros ON autores.id_autor = livros.id_autor
GROUP BY autores.nome;
