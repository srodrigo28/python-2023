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

cursor.execute("USE `jogoteca`;")

# inserindo usuarios
# usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES(%s, %s, %s)'
# usuarios = [
#     ("Bastião Sousa", "bs", "123"),
#     ("Camilla Ferreira", "cf", "123"),
#     ("Aline Tocafundo", "at", "123")
# ]
# cursor.executemany(usuario_sql, usuarios)

cursor.execute('SELECT * FROM jogoteca.usuarios')
print('--------------------- Usuários: ---------------------')
for user in cursor.fetchall():
    print(user[1], '----', user[2])
