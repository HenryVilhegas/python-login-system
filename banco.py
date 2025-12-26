import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'usuarios.db')

conexao = sqlite3.connect(DB_PATH)
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    senha TEXT NOT NULL
)
""")

cursor.execute("SELECT * FROM usuarios WHERE usuario = 'admin'")
existe = cursor.fetchone()

if not existe:
    cursor.execute(
        "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
        ('admin', '123')
    )

conexao.commit()
conexao.close()

print("Banco criado com sucesso!")
