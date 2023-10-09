USE jogoteca2;

CREATE TABLE `jogos`(
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `nome` VARCHAR(50) NOT NULL,
        `categoria` VARCHAR(40) NOT NULL,
        `console` VARCHAR(20) NOT NULL,
        PRIMARY KEY (`id`)
)

CREATE TABLE usuarios(
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `nome` VARCHAR(20) NOT NULL,
        `nickname` VARCHAR(8) NOT NULL,
        `senha` VARCHAR(100) NOT NULL,
        PRIMARY KEY (`id`)
    )

INSERT INTO usuarios (nome, nickname, senha) 
VALUES
    ('Sebastião', 'sb', '123'),
    ('Camilla Tocafundo', 'ct', '123'),
    ('aline tocafundo', 'at', '123')

INSERT INTO jogos (nome, categoria, console) 
VALUES
    ('sonic', 'aventura', 'megadriver'),
    ('bomberman', 'aventura', 'nintendo'),
    ('need for speed', 'corrida', 'ps1')