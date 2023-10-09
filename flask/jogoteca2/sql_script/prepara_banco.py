import mysql.connector
from mysql.connector import errorcode

print("Conectando ...")
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")

cursor.execute("CREATE DATABASE`jogoteca`;")

cursor.execute("USE `jogoteca`;")

# Criando tabelas
TABLES = {}
TABLES['Jogos'] = ('''
    CREATE TABLE `jogos`(
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `nome` VARCHAR(50) NOT NULL,
        `categoria` VARCHAR(40) NOT NULL,
        `console` VARCHAR(20) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin; ''')

TABLES['Usuarios'] = ('''
    CREATE TABLE `usuarios`(
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `nome` VARCHAR(20) NOT NULL,
        `nickname` VARCHAR(8) NOT NULL,
        `senha` VARCHAR(100) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin; ''')

for table_nome in TABLES:
    tabela_sql = TABLES[table_nome]
    try:
        print('Criando tabela {}'.format(table_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK')

# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios(nome, nickname, senha) VALUES(%s, %s, %s)'
usuarios = [
    ("Bastião Sousa", "bs", "123"),
    ("Camilla Ferreira", "cf", "123"),
    ("Aline Tocafundo", "at", "123")
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('SELECT * FROM jogoteca.usuarios')
print('--------------------- Usuários: ---------------------')
for user in cursor.fetchall():
    print(user[1])
    
# Inserindo jogos
jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES(%s, %s, %s)'
jogos = [
    ('Tetris', 'Puzzle', 'Atari'),
    ('Sonic 1', 'Aventura', 'Mega Driver'),
    ('Sonic 2', 'Aventura', 'Mega Driver'),
    ('God Of War', 'Aventura', 'PS1'),
    ('God Of War 2', 'Luta', 'PS2')
]
cursor.executemany(jogos_sql, jogos)

print('--------------------- Jogos: ---------------------')
for jogo in cursor.fetchall():
    print(jogo[1])
                   
                   